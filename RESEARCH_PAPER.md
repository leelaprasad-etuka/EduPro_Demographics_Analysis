# Technical Research Paper: Learner Demographics and Course Enrollment Behavior Analysis on EduPro

**Author:** Etuka Leela Prasad  
**Organization:** Unified Mentor Machine Learning Internship  
**Dataset:** EduPro Online Platform Relational Dataset (10,000 Transactions, 3,000 Learners, 60 Courses)

---

## 1. Abstract
Online education platforms require empirical learner intelligence to align curriculum design, accessibility initiatives, and marketing outreach with actual user behavior. This study performs a comprehensive descriptive analysis of the EduPro platform by joining 10,000 transaction records with 3,000 user demographic profiles and 60 course catalog entries. Findings demonstrate that platform engagement is heavily concentrated among young professionals aged 26-35 (47.99%) and university-age learners aged 18-25 (37.32%), with complete market absence in learners aged 36 and older (0.00%). Gender participation achieves near-exact parity at 50.78% Female and 49.22% Male. Course demand is distributed across 12 categories led by Data Science (916 enrollments), while course type distribution shows strong reliance on Free courses (64.03%) over Paid offerings (35.97%). Finally, skill-level distribution reveals a "Mid-Tier Dip," where Beginner (35.73%) and Advanced (34.75%) enrollments significantly outpace Intermediate offerings (29.52%).

---

## 2. Introduction and Problem Statement
EduPro operates a multi-disciplinary online learning portal serving diverse subjects ranging from Data Science and Artificial Intelligence to Finance and Design. While transaction logs capture enrollment velocity, platform administrators previously lacked relational visibility into how learner age, gender, and course structure interact. Specifically, this research addresses five core analytical questions:
1. What is the exact age distribution of active learners on EduPro?
2. How does course enrollment volume vary across demographic age brackets?
3. Are there statistically significant gender-based differences in course selection and difficulty preferences?
4. Which course categories attract the highest and lowest enrollment demand?
5. How do learners distribute across Beginner, Intermediate, and Advanced levels, as well as Free versus Paid tiers?

---

## 3. Analytical Methodology

### 3.1 Data Integration and Referential Integrity
The raw data resides across three separate worksheets within `EduPro Online Platform.xlsx`:
- **Users (`N = 3,000`):** Contains `UserID`, `UserName`, `Age`, and `Gender`.
- **Courses (`N = 60`):** Contains `CourseID`, `CourseName`, `CourseCategory`, `CourseType`, and `CourseLevel`.
- **Transactions (`N = 10,000`):** Contains `TransactionID`, `UserID`, `CourseID`, and `TransactionDate`.

Using inner relational joins in Python (`pandas`), `Transactions` was merged with `Users` on `UserID` and subsequently merged with `Courses` on `CourseID`. All 10,000 transactions successfully mapped to valid users and courses with zero orphaned records. String normalization (`str.strip()`) was applied across all categorical fields.

### 3.2 Demographic Segmentation
Learners were segmented into five standardized age bands prescribed by the analytical framework:
- `<18`: Pre-university / high school learners
- `18-25`: College and early-career entrants
- `26-35`: Working professionals and upskillers
- `36-45`: Mid-career professionals
- `45+`: Senior career and lifelong learners

---

## 4. Empirical Findings and Exploratory Data Analysis (EDA)

### 4.1 Platform Engagement and Enrollment Concentration
Across the platform, 3,000 unique learners generated 10,000 total enrollments, resulting in an **Average Courses per Learner of 3.33**. This indicates strong multi-course retention among registered users rather than single-course drop-off.

### 4.2 Age Band Distribution
| Age Band | Total Enrollments | Share of Enrollments (%) | Demographic Status |
| :--- | :---: | :---: | :--- |
| `<18` | 1,469 | 14.69% | Emerging Youth Segment |
| `18-25` | 3,732 | 37.32% | Core Academic / Early Career |
| `26-35` | 4,799 | 47.99% | Primary Professional Segment |
| `36-45` | 0 | 0.00% | Untapped Demographic |
| `45+` | 0 | 0.00% | Untapped Demographic |

**Key Insight:** Exactly 85.31% of all enrollments originate from learners aged 18 to 35, with the `26-35` bracket representing nearly half of all platform activity (4,799 enrollments). Conversely, EduPro records zero enrollments from learners aged 36 and above, exposing a critical demographic blind spot in mid-career and executive education.

### 4.3 Gender Participation Ratio
| Gender | Total Enrollments | Share (%) |
| :--- | :---: | :---: |
| Female | 5,078 | 50.78% |
| Male | 4,922 | 49.22% |

**Key Insight:** EduPro demonstrates exceptional gender inclusivity, with Female learners leading Male learners by a margin of 156 enrollments (1.56 percentage points). Cross-tabulation across course levels and categories confirms balanced participation across both technical and business domains.

### 4.4 Course Category Popularity Index
| Rank | Course Category | Enrollments | Share (%) |
| :---: | :--- | :---: | :---: |
| 1 | Data Science | 916 | 9.16% |
| 2 | Finance | 864 | 8.64% |
| 3 | Web Development | 844 | 8.44% |
| 4 | Business | 833 | 8.33% |
| 5 | Project Management | 829 | 8.29% |
| 6 | Artificial Intelligence | 829 | 8.29% |
| 7 | Design | 827 | 8.27% |
| 8 | Cybersecurity | 819 | 8.19% |
| 9 | Machine Learning | 819 | 8.19% |
| 10 | Digital Marketing | 808 | 8.08% |
| 11 | Marketing | 806 | 8.06% |
| 12 | Programming | 806 | 8.06% |

**Key Insight:** While **Data Science** (916), **Finance** (864), and **Web Development** (844) lead total enrollment demand, the spread between the highest category (916) and lowest categories (**Marketing** and **Programming** at 806 each) is only 110 enrollments. This indicates well-diversified curriculum demand across all 12 catalog verticals.

### 4.5 Course Level and Course Type Behavior
| Dimension | Segment | Enrollments | Share (%) |
| :--- | :--- | :---: | :---: |
| **Course Level** | Beginner | 3,573 | 35.73% |
| **Course Level** | Advanced | 3,475 | 34.75% |
| **Course Level** | Intermediate | 2,952 | 29.52% |
| **Course Type** | Free | 6,403 | 64.03% |
| **Course Type** | Paid | 3,597 | 35.97% |

**Key Insight:**
1. **The Intermediate Gap:** Learners strongly gravitate toward **Beginner** (35.73%) and **Advanced** (34.75%) courses, while **Intermediate** courses lag behind at 29.52% (523 fewer enrollments than Advanced). This suggests a curriculum bridging gap where learners either enter at the foundational level or jump directly to specialized advanced topics.
2. **Free vs. Paid Reliance:** Nearly two-thirds (64.03%) of enrollments occur in Free courses, serving as the primary acquisition funnel, while 35.97% convert into Paid enrollments.

---

## 5. Strategic Recommendations
1. **Launch Mid-Career and Executive Learning Tracks (Ages 36+):** With 0% participation in the `36-45` and `45+` brackets, EduPro should introduce executive leadership, management upskilling, and flexible modular certificates targeted at senior professionals.
2. **Bridge the Intermediate Curriculum Dip:** Restructure course pathways into guided 3-step learning tracks (Beginner -> Intermediate -> Advanced) so learners progressing from Beginner courses (3,573) naturally transition through Intermediate modules (currently 2,952) rather than skipping or dropping off.
3. **Expand High-Velocity Catalog Verticals:** Allocate additional instructional design capacity to **Data Science** (916), **Finance** (864), and **Web Development** (844), while bundling **Programming** (806) and **Marketing** (806) with top-performing tracks to lift their enrollment volume.
4. **Optimize Free-to-Paid Conversion Pathways:** Leverage the 6,403 Free course enrollments by embedding intermediate and advanced Paid capstone certifications directly at the completion of free introductory modules.