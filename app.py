import streamlit as st
import pandas as pd
import plotly.express as px
from analysis import load_and_analyze_edupro, AGE_BAND_ORDER

st.set_page_config(
    page_title="EduPro Learner Demographics and Enrollment Analysis",
    layout="wide"
)

@st.cache_data
def get_data():
    return load_and_analyze_edupro()

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# --- SIDEBAR: USER CAPABILITIES ---
st.sidebar.header("Filter Controls")

available_ages = [a for a in AGE_BAND_ORDER if a in df["AgeBand"].unique()]
selected_ages = st.sidebar.multiselect("Age Group Filters", available_ages, default=available_ages)

all_genders = sorted(df["Gender"].dropna().unique())
selected_genders = st.sidebar.multiselect("Gender Filters", all_genders, default=all_genders)

all_categories = sorted(df["CourseCategory"].dropna().unique())
selected_categories = st.sidebar.multiselect("Course Category Selector", all_categories, default=all_categories)

all_levels = sorted(df["CourseLevel"].dropna().unique())
selected_levels = st.sidebar.multiselect("Course Level Selector", all_levels, default=all_levels)

filtered_df = df[
    df["AgeBand"].isin(selected_ages) &
    df["Gender"].isin(selected_genders) &
    df["CourseCategory"].isin(selected_categories) &
    df["CourseLevel"].isin(selected_levels)
]

# --- HEADER ---
st.title("Learner Demographics and Course Enrollment Behavior Analysis on EduPro")
st.markdown("Descriptive learner intelligence dashboard analyzing age distributions, gender participation, course demand, and enrollment behavior.")

if filtered_df.empty:
    st.warning("No records match the selected filters. Adjust the sidebar filter criteria.")
    st.stop()

# --- KEY PERFORMANCE INDICATORS (5 REQUIRED KPIS) ---
total_enrollments = len(filtered_df)
unique_learners = filtered_df["UserID"].nunique()
avg_courses = round(total_enrollments / unique_learners, 2) if unique_learners > 0 else 0.0

top_age = filtered_df["AgeBand"].value_counts().idxmax()
top_age_cnt = filtered_df["AgeBand"].value_counts().max()
top_age_pct = (top_age_cnt / total_enrollments) * 100

top_gender = filtered_df["Gender"].value_counts().idxmax()
top_gender_pct = (filtered_df["Gender"].value_counts().max() / total_enrollments) * 100

top_category = filtered_df["CourseCategory"].value_counts().idxmax()
top_category_cnt = filtered_df["CourseCategory"].value_counts().max()

top_level = filtered_df["CourseLevel"].value_counts().idxmax()
top_level_pct = (filtered_df["CourseLevel"].value_counts().max() / total_enrollments) * 100

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Enrollments", f"{total_enrollments:,}", f"{unique_learners:,} Active Learners")
with col2:
    st.metric("Enrollments by Age Group", f"Top: {top_age}", f"{top_age_pct:.1f}% Share ({top_age_cnt:,})")
with col3:
    st.metric("Gender Participation Ratio", f"Lead: {top_gender}", f"{top_gender_pct:.1f}% of Enrollments")
with col4:
    st.metric("Category Popularity Index", top_category, f"{top_category_cnt:,} Enrollments")
with col5:
    st.metric("Level Preference Distribution", top_level, f"{top_level_pct:.1f}% Share | {avg_courses} Avg/User")

st.divider()

# --- 4 CORE MODULES ---
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Learner Demographic Overview",
    "2. Age-Wise Enrollment Charts",
    "3. Gender-Based Course Preferences",
    "4. Course Category Popularity & Behavior"
])

with tab1:
    st.subheader("Learner Demographic Distribution and Participation")
    c1, c2 = st.columns(2)

    with c1:
        learner_age = (
            filtered_df.groupby("AgeBand")["UserID"]
            .nunique()
            .reindex(AGE_BAND_ORDER, fill_value=0)
            .reset_index()
        )
        learner_age.columns = ["Age Group", "Unique Learners"]
        fig_u_age = px.bar(
            learner_age, x="Age Group", y="Unique Learners",
            text_auto=True,
            title="Active Unique Learners by Age Band",
            template="plotly_white"
        )
        st.plotly_chart(fig_u_age, use_container_width=True)

    with c2:
        gender_dist = filtered_df["Gender"].value_counts().reset_index()
        gender_dist.columns = ["Gender", "Enrollments"]
        fig_gen = px.pie(
            gender_dist, names="Gender", values="Enrollments",
            title="Gender Participation Ratio Across Platform",
            hole=0.4, template="plotly_white"
        )
        st.plotly_chart(fig_gen, use_container_width=True)

    st.subheader("Demographic Participation Summary Table")
    demo_summary = (
        filtered_df.groupby(["AgeBand", "Gender"], as_index=False)
        .agg(
            Unique_Learners=("UserID", "nunique"),
            Total_Enrollments=("TransactionID", "count")
        )
    )
    demo_summary["Avg_Courses_Per_Learner"] = (
        demo_summary["Total_Enrollments"] / demo_summary["Unique_Learners"]
    ).round(2)
    st.dataframe(demo_summary, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Age-Wise Enrollment Distribution and Cross-Analysis")
    c1, c2 = st.columns(2)

    with c1:
        age_enr = (
            filtered_df["AgeBand"]
            .value_counts()
            .reindex(AGE_BAND_ORDER, fill_value=0)
            .reset_index()
        )
        age_enr.columns = ["Age Group", "Total Enrollments"]
        fig_a_enr = px.bar(
            age_enr, x="Age Group", y="Total Enrollments",
            text_auto=True,
            title="Total Course Enrollments by Age Band",
            template="plotly_white"
        )
        st.plotly_chart(fig_a_enr, use_container_width=True)

    with c2:
        age_lvl = pd.crosstab(filtered_df["AgeBand"], filtered_df["CourseLevel"]).reindex(AGE_BAND_ORDER, fill_value=0).reset_index()
        age_lvl_melt = age_lvl.melt(id_vars="AgeBand", var_name="Course Level", value_name="Enrollments")
        fig_a_lvl = px.bar(
            age_lvl_melt, x="AgeBand", y="Enrollments", color="Course Level",
            barmode="group", text_auto=True,
            title="Course Level Popularity Across Age Groups",
            template="plotly_white"
        )
        st.plotly_chart(fig_a_lvl, use_container_width=True)

    st.subheader("Age Group vs. Course Category Heatmap")
    heat_df = pd.crosstab(filtered_df["AgeBand"], filtered_df["CourseCategory"]).reindex(AGE_BAND_ORDER, fill_value=0)
    fig_heat = px.imshow(
        heat_df, text_auto=True, aspect="auto",
        color_continuous_scale="Blues",
        title="Enrollment Density Matrix: Age Group vs. Course Category"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

with tab3:
    st.subheader("Gender-Based Course Selection and Level Comparisons")
    c1, c2 = st.columns(2)

    with c1:
        gen_lvl = pd.crosstab(filtered_df["Gender"], filtered_df["CourseLevel"]).reset_index()
        gen_lvl_melt = gen_lvl.melt(id_vars="Gender", var_name="Course Level", value_name="Enrollments")
        fig_g_lvl = px.bar(
            gen_lvl_melt, x="Gender", y="Enrollments", color="Course Level",
            barmode="group", text_auto=True,
            title="Gender vs. Course Level Comparison",
            template="plotly_white"
        )
        st.plotly_chart(fig_g_lvl, use_container_width=True)

    with c2:
        gen_cat = pd.crosstab(filtered_df["CourseCategory"], filtered_df["Gender"]).reset_index()
        gen_cat_melt = gen_cat.melt(id_vars="CourseCategory", var_name="Gender", value_name="Enrollments")
        fig_g_cat = px.bar(
            gen_cat_melt, x="CourseCategory", y="Enrollments", color="Gender",
            barmode="group", text_auto=True,
            title="Course Category Preferences by Gender",
            template="plotly_white"
        )
        st.plotly_chart(fig_g_cat, use_container_width=True)

    st.subheader("Gender vs. Course Type Breakdown")
    gen_type = pd.crosstab(filtered_df["Gender"], filtered_df["CourseType"]).reset_index()
    gen_type_melt = gen_type.melt(id_vars="Gender", var_name="Course Type", value_name="Enrollments")
    fig_g_type = px.bar(
        gen_type_melt, x="Gender", y="Enrollments", color="Course Type",
        barmode="group", text_auto=True,
        title="Enrollment Distribution by Gender and Course Type",
        template="plotly_white"
    )
    st.plotly_chart(fig_g_type, use_container_width=True)

with tab4:
    st.subheader("Course Category Popularity and Learner Behavioral Insights")
    c1, c2 = st.columns(2)

    with c1:
        cat_cnt = filtered_df["CourseCategory"].value_counts().sort_values(ascending=True).reset_index()
        cat_cnt.columns = ["Course Category", "Enrollments"]
        fig_cat = px.bar(
            cat_cnt, x="Enrollments", y="Course Category", orientation="h",
            text_auto=True,
            title="Most and Least Popular Course Categories",
            template="plotly_white"
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    with c2:
        lvl_type = pd.crosstab(filtered_df["CourseLevel"], filtered_df["CourseType"]).reset_index()
        lvl_type_melt = lvl_type.melt(id_vars="CourseLevel", var_name="Course Type", value_name="Enrollments")
        fig_lt = px.bar(
            lvl_type_melt, x="CourseLevel", y="Enrollments", color="Course Type",
            barmode="group", text_auto=True,
            title="Beginner vs. Advanced Preferences by Course Type",
            template="plotly_white"
        )
        st.plotly_chart(fig_lt, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        lvl_cnt = filtered_df["CourseLevel"].value_counts().reset_index()
        lvl_cnt.columns = ["Course Level", "Enrollments"]
        fig_lvl_pie = px.pie(
            lvl_cnt, names="Course Level", values="Enrollments",
            title="Overall Level Preference Distribution",
            hole=0.4, template="plotly_white"
        )
        st.plotly_chart(fig_lvl_pie, use_container_width=True)

    with c4:
        user_freq = filtered_df.groupby("UserID")["TransactionID"].count().reset_index()
        user_freq.columns = ["UserID", "Courses_Taken"]
        conc_df = user_freq["Courses_Taken"].value_counts().sort_index().reset_index()
        conc_df.columns = ["Courses Enrolled per Learner", "Number of Learners"]
        fig_conc = px.bar(
            conc_df, x="Courses Enrolled per Learner", y="Number of Learners",
            text_auto=True,
            title="Enrollment Concentration (Courses Taken per Active Learner)",
            template="plotly_white"
        )
        st.plotly_chart(fig_conc, use_container_width=True)