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

    # Clean text columns
    for col in ["Gender", "CourseCategory", "CourseType", "CourseLevel"]:
        if col in merged_df.columns:
            merged_df[col] = merged_df[col].astype(str).str.strip()

    if "TransactionDate" in merged_df.columns:
        merged_df["TransactionDate"] = pd.to_datetime(merged_df["TransactionDate"], errors="coerce")
        merged_df["YearMonth"] = merged_df["TransactionDate"].dt.to_period("M").astype(str)

    # Step 2: Learner Demographic Analysis (Age Bands)
    merged_df["AgeBand"] = merged_df["Age"].apply(assign_age_band)

    return merged_df

def format_summary_table(series: pd.Series, total: int, reindex_order=None) -> pd.DataFrame:
    counts = series.value_counts()
    if reindex_order is not None:
        counts = counts.reindex(reindex_order, fill_value=0)
    summary = pd.DataFrame({
        "Enrollments": counts,
        "Share (%)": ((counts / total) * 100).round(2)
    })
    return summary

if __name__ == "__main__":
    df = load_and_analyze_edupro()
    total_enr = len(df)
    unique_usr = df["UserID"].nunique()
    active_crs = df["CourseID"].nunique()

    print("=== EDUPRO VALIDATED ANALYTICAL SUMMARY ===")
    print(f"Total Enrollments: {total_enr:,}")
    print(f"Total Unique Learners: {unique_usr:,}")
    print(f"Total Active Courses: {active_crs:,}")
    print(f"Average Courses per Learner: {total_enr / unique_usr:.2f}")

    print("\n--- Enrollments by Age Band (Count & %) ---")
    print(format_summary_table(df["AgeBand"], total_enr, AGE_BAND_ORDER).to_string())

    print("\n--- Gender Participation Ratio (Count & %) ---")
    print(format_summary_table(df["Gender"], total_enr).to_string())

    print("\n--- Course Category Popularity Index (Count & %) ---")
    print(format_summary_table(df["CourseCategory"], total_enr).to_string())

    print("\n--- Course Type Distribution (Count & %) ---")
    print(format_summary_table(df["CourseType"], total_enr).to_string())

    print("\n--- Course Level Preference Distribution (Count & %) ---")
    print(format_summary_table(df["CourseLevel"], total_enr).to_string())