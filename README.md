# Learner Demographics and Course Enrollment Behavior Analysis on EduPro

**Live Streamlit Application:** [https://course-enrollment-edupro.streamlit.app/](https://course-enrollment-edupro.streamlit.app/)  
**Author:** Etuka Leela Prasad  

## 1. Project Overview
This project delivers an end-to-end descriptive learner intelligence dashboard and research study for the EduPro online learning platform. By integrating 10,000 transaction records with 3,000 unique user profiles and 60 courses across 12 subject categories, the application evaluates demographic reach, gender inclusivity, course demand, time-based enrollment trends, and skill-level progression.

## 2. Validated Key Performance Indicators & Formulas
| KPI Metric | Mathematical Formula | Verified Value | Key Insight |
| :--- | :--- | :---: | :--- |
| **Total Enrollments** | `Count(TransactionID)` | **10,000** | 3,000 Unique Learners (3.33 Avg Courses/Learner) |
| **Enrollments by Age Group** | `(AgeBand Enrollments / Total) * 100` | **26-35: 47.99% (4,799)** | 18-25: 37.32% (3,732), <18: 14.69% (1,469), 36+: 0.00% (0) |
| **Gender Participation Ratio** | `(Gender Enrollments / Total) * 100` | **Female: 50.78% (5,078)** | Male: 49.22% (4,922) — Verified gender parity |
| **Category Popularity Index** | `(Category Enrollments / Total) * 100` | **Data Science: 9.16% (916)** | Followed by Finance (864) and Web Development (844) |
| **Level Preference Distribution** | `(Level Enrollments / Total) * 100` | **Beginner: 35.73% (3,573)** | Advanced: 34.75% (3,475), Intermediate: 29.52% (2,952) |
| **Course Type Split** | `(Type Enrollments / Total) * 100` | **Free: 64.03% (6,403)** | Paid: 35.97% (3,597) |

## 3. Streamlit Dashboard Architecture (5 Core Modules)
- **Top KPI Scorecards & Formula Reference Expander:** Complete, non-truncated KPI metrics paired with an expandable mathematical formula and validation table.
- **Tab 1 — Demographic Overview:** Unique learners by age band (with % share labels), gender participation donut chart, and validated demographic summary table.
- **Tab 2 — Age-Wise Enrollment Analysis:** Total enrollments by age group, Age vs. Course Level grouped comparison, and Age Group vs. Course Category density heatmap.
- **Tab 3 — Gender Preference Analysis:** Gender vs. Course Level, Gender vs. Course Type (Free/Paid), Category demand by gender, and normalized percentage share table.
- **Tab 4 — Category, Level & Time Trends:** Horizontal ranking of all 12 categories, Beginner vs. Advanced by course type, courses taken per learner concentration, and monthly time-series enrollment trends (`TransactionDate`).
- **Tab 5 — Executive Summary & Recommendations:** Built-in empirical findings, quantified target thresholds, and a Category-Level Decision Matrix.

## 4. Repository Deliverables
- `app.py`: Production 5-tab Streamlit web application.
- `analysis.py`: Data integration, cleaning, age-band segmentation, and statistical verification script.
- `EduPro Online Platform.xlsx`: Raw multi-sheet relational dataset (`Users`, `Courses`, `Transactions`).
- `RESEARCH_PAPER.md`: Full technical research paper with methodology, formulas, EDA tables, and recommendations.
- `EXECUTIVE_SUMMARY.md`: Executive policy and strategy briefing for government and platform stakeholders.
- `requirements.txt`: Python dependencies (`streamlit`, `pandas`, `openpyxl`, `plotly`).