import pandas as pd
from pathlib import Path

DATA_FILE = "EduPro Online Platform.xlsx"
AGE_BAND_ORDER = ["<18", "18-25", "26-35", "36-45", "45+"]

def assign_age_band(age):
    if pd.isna(age):
        return "Unknown"
    age = float(age)
    if age < 18:
        return "<18"
    elif age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    else:
        return "45+"

def load_and_analyze_edupro(file_path: str = DATA_FILE) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset '{file_path}' not found in the project folder.")

    users_df = pd.read_excel(path, sheet_name="Users")
    courses_df = pd.read_excel(path, sheet_name="Courses")
    transactions_df = pd.read_excel(path, sheet_name="Transactions")

    users_df.columns = users_df.columns.str.strip()
    courses_df.columns = courses_df.columns.str.strip()
    transactions_df.columns = transactions_df.columns.str.strip()

    # Step 1: Data Integration (Users <-> Transactions <-> Courses)
    merged_df = transactions_df.merge(users_df, on="UserID", how="inner")
    merged_df = merged_df.merge(courses_df, on="CourseID", how="inner")

    # Clean text columns to avoid trailing-space mismatches
    for col in ["Gender", "CourseCategory", "CourseType", "CourseLevel"]:
        if col in merged_df.columns:
            merged_df[col] = merged_df[col].astype(str).str.strip()

    if "TransactionDate" in merged_df.columns:
        merged_df["TransactionDate"] = pd.to_datetime(merged_df["TransactionDate"], errors="coerce")

    # Step 2: Learner Demographic Analysis (Age Bands)
    merged_df["AgeBand"] = merged_df["Age"].apply(assign_age_band)

    return merged_df

if __name__ == "__main__":
    df = load_and_analyze_edupro()
    print("=== EDUPRO ANALYTICAL SUMMARY ===")
    print(f"Total Enrollments: {len(df):,}")
    print(f"Total Unique Learners: {df['UserID'].nunique():,}")
    print(f"Total Active Courses: {df['CourseID'].nunique():,}")
    print(f"Average Courses per Learner: {len(df) / df['UserID'].nunique():.2f}")

    print("\n--- Enrollments by Age Band ---")
    print(df["AgeBand"].value_counts().reindex(AGE_BAND_ORDER, fill_value=0).to_string())

    print("\n--- Gender Participation ---")
    print(df["Gender"].value_counts().to_string())

    print("\n--- Course Category Popularity ---")
    print(df["CourseCategory"].value_counts().to_string())

    print("\n--- Course Type Distribution ---")
    print(df["CourseType"].value_counts().to_string())

    print("\n--- Course Level Distribution ---")
    print(df["CourseLevel"].value_counts().to_string())