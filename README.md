# Learner Demographics and Course Enrollment Behavior Analysis on EduPro

## Project Overview
This project delivers an end-to-end descriptive learner intelligence system for the EduPro online learning platform. By integrating learner demographic profiles, course metadata, and enrollment transaction logs, the system evaluates demographic reach, gender inclusivity, course category demand, and skill-level progression across 10,000 enrollments and 3,000 unique learners.

## Problem Statement
Despite capturing user registration and transaction logs, EduPro lacked empirical answers regarding:
- Which age groups are most active on the platform.
- How enrollment patterns differ across gender groups.
- Which course categories attract the highest and lowest learner demand.
- How beginner, intermediate, and advanced courses perform across learner segments and pricing tiers.

## Dataset Architecture
The analysis integrates three relational sheets from `EduPro Online Platform.xlsx`:
- **Users Sheet:** `UserID`, `UserName`, `Age`, `Gender` (3,000 unique learners)
- **Courses Sheet:** `CourseID`, `CourseName`, `CourseCategory`, `CourseType`, `CourseLevel` (60 active courses across 12 categories)
- **Transactions Sheet:** `TransactionID`, `UserID`, `CourseID`, `TransactionDate` (10,000 verified enrollment transactions)

## Key Performance Indicators (KPIs) Summary
- **Total Enrollments:** 10,000 transactions across 3,000 unique learners (Average of 3.33 courses per learner).
- **Enrollments by Age Group:** Led by the 26-35 cohort with 4,799 enrollments (47.99%), followed by 18-25 with 3,732 (37.32%) and <18 with 1,469 (14.69%). Zero enrollments recorded in the 36-45 and 45+ bands.
- **Gender Participation Ratio:** Highly balanced participation with 5,078 Female enrollments (50.78%) and 4,922 Male enrollments (49.22%).
- **Category Popularity Index:** Data Science leads overall demand with 916 enrollments (9.16%), followed by Finance (864) and Web Development (844). Marketing (806) and Programming (806) represent the lowest enrollment volumes.
- **Level Preference Distribution:** Beginner courses account for 3,573 enrollments (35.73%), Advanced courses capture 3,475 (34.75%), and Intermediate courses account for 2,952 (29.52%). Free courses represent 64.03% (6,403) of total volume compared to 35.97% (3,597) for Paid courses.

## Repository Structure
- `EduPro Online Platform.xlsx`: Primary multi-sheet dataset.
- `analysis.py`: Data integration, cleaning, age-band segmentation, and statistical aggregation script.
- `app.py`: Production Streamlit interactive dashboard featuring 4 analytical modules and sidebar filter capabilities.
- `requirements.txt`: Python package dependencies for cloud deployment.
- `RESEARCH_PAPER.md`: Comprehensive technical research paper detailing EDA, methodology, findings, and recommendations.
- `EXECUTIVE_SUMMARY.md`: Policy and strategic briefing tailored for platform leadership and government stakeholders.

## Local Installation and Execution
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt