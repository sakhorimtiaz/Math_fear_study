# **Math Anxiety, Exam Phobia & Math Learning Experience Survey (Phase 1\)**

&nbsp;

&nbsp;

**Problem Statement:**  
How can St. Gregory's High School and College pursue academic excellence while supporting students' confidence, well-being, and healthy engagement with mathematics?

&nbsp;

**Primary Research Question:**  
How do mathematics anxiety, examination anxiety, mathematical learning behaviour, classroom psychological safety, examination behaviour, and the student's learning environment relate to one another?

**Some hypotheses:**  
**H1:** High classroom psychological safety (specifically the absence of peer mockery) significantly reduces overall math anxiety.

**H2:** Cognitive freezing and application paralysis predict examination anxiety more strongly than a lack of mathematical memorization.

**H3:** Anticipated social shame and the fear of making classroom mistakes are primary drivers of exam phobia.

&nbsp;

**Project Initiation:**

* Obtained permission from our principal  
* Formed a research team of two teachers and 13 dedicated student volunteers.  
* Identified key stakeholders

&nbsp;

**Planning:**

* Collected consent letters from student volunteers’ parents.  
* Broke down the whole work into tasks and milestones.  
* Prepared a set of 48 questions in layers:  
  \[Survey form questions: [https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/Final%20RP%203.docx.md](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/Final%20RP%203.docx.md) \]  
  * Firstly, K M Imtiaz Hossain wrote a draft based on his mathematics teaching experience.  
  * Secondly, we asked 23 random students from classes 6, 7, and 9 (both Bangla and English) to write 5 points on “Why do you fear mathematics?”  
  * Next, student counselor Ms. Konika Akter gave her point of view on this issue and merged AMAS and the Westside Test Anxiety Scales into the survey form.  
  * After that, we put it all together and wrote the questions in very simple language that can be understood by the students from class 5 to 12\.  
  * At last, we added some suggestions from our vice principal.

&nbsp;

**Execution:**

* Team Readiness: Trained volunteers about the questions, data collection, and how to help students if anyone asks for any clarification on the questions' meaning.&nbsp;  
* Teachers’ meeting: Conducted a meeting with all the math teachers, informing them about the overview and probable outcome of the research.  
* We divided the whole work into 3 Phases.  
  * Phase 1: Collect data from two small sections (E7A and E9A)  
  * Phase 2: Collect data from classes 6, 7, and 9  
  * Phase 3: Collect data from classes 5, 8, 10, 11, and 12

&nbsp;

**Here are the steps that we followed in Phase 1:**

&nbsp;

**Step\_0: Data Alignment**&nbsp;

Action:&nbsp;

Question E5 uses reverse logic, so we needed to change the scores. The formula applied is: actual \= (6 \- recorded score).&nbsp;

\[In the future, we will use an updated survey form by renaming E5 to EN5 and putting that question in Part D: [https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/Final\_RP\_2\_updated\_Sep15.md](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/Final_RP_2_updated_Sep15.md) \]

&nbsp;

Raw Data:  
[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data.csv](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data.csv)

&nbsp;

Code:

[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_0.py](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_0.py)

&nbsp;

Output:

[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_E5\_corrected.csv](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_E5_corrected.csv)

&nbsp;

&nbsp;

**Step\_1: Data Cleaning**&nbsp;

Action:&nbsp;

Filled in the null values with the column median.&nbsp;

&nbsp;

Code:  
[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_1.py](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_1.py)

&nbsp;

Output:  
[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_no\_null.csv](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_no_null.csv)

&nbsp;

**Step\_2: Aggregation**&nbsp;  
Action: Determined the aggregated results for every student in the following categories: Avg\_B (Math Anxiety), Avg\_C (Test Anxiety), Avg\_D (Math Thinking), Avg\_E (Classroom Safety), Avg\_F (Exam Self-Reg), Avg\_G (Academic Pressure), Avg\_H (Exam Phobia).&nbsp;

&nbsp;

Code:

[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_2.py](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_2.py)

&nbsp;

Output:  
[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_aggregated.csv](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_aggregated.csv)

&nbsp;

**Step\_3: Preliminary Correlation**&nbsp;

Action: Checked the correlation of some selected questions.&nbsp;

Code:

[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_3.py](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_3.py)

&nbsp;

&nbsp;

**Step\_4: Item-Level Correlation**&nbsp;

Action: Calculated the correlation of each question with Math Anxiety and Exam Phobia.&nbsp;

Code:

[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_4.py](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_4.py)

&nbsp;

Output:  
[https://github.com/sakhorimtiaz/Math\_fear\_study/blob/Think-Python-by-Allen-B.-Downey/math\_fear\_real\_data\_item\_correlations\_summary.csv](https://github.com/sakhorimtiaz/Math_fear_study/blob/Think-Python-by-Allen-B.-Downey/math_fear_real_data_item_correlations_summary.csv)

&nbsp;

**Results and Recommendations (Phase 1\)**&nbsp;  
**Finding 1:**&nbsp;

Question E5 ("**Afraid classmates will laugh**"), which measures **Classroom safety**, shows a strong positive correlation with **both Math Anxiety** (+0.292) **and Exam Phobia** (+0.295).

**Recommendation:**  
**Enforce Zero-Tolerance for Classroom Mockery:** Establish strict disciplinary guidelines against students laughing at peers. Students should feel comfortable answering questions and making mistakes without fear of embarrassment.&nbsp;

**Finding 2:**

Question C2 ("**Mind goes blank even for known answers**") in the **Test Anxiety** section is the strongest non-diagnostic driver of **Math Anxiety** (+0.491 correlation).

&nbsp;

**Recommendation:**

**Use Simple Grounding Techniques Before Exams:** Give students two minutes of quiet breathing or relaxation before a math exam. This can help reduce initial panic and make it easier to remember formulas and concepts.&nbsp;

&nbsp;

**Finding 3:**&nbsp;

From **Exam Self-Regulation**, FN7 ("**Know the rules but don't know which one to use**") has a massive \+0.572 correlation with **Exam Phobia**.

&nbsp;

**Recommendation:**

**Focus on Understanding Problem Types:** Give students more practice in identifying what type of problem they are facing and which method or formula they should use. This will help them choose the right approach during exams.

&nbsp;

**Finding 4:**&nbsp;

Question EN3 ("**Fear of making mistakes in class**"), which measures **Classroom safety**, shows a foundational trigger for **Exam Phobia** (+0.593 correlation).

&nbsp;

**Recommendation:**

**Normalize Public Mistakes:** Encourage teachers to appreciate students who try to solve problems on the board, even when the final answer is wrong. This can help students become less afraid of making mistakes in front of others and will significantly lower long-term exam phobia.

&nbsp;

**Finding 5:**&nbsp;

From **Academic Pressure**, GN6 ("**Fear of shame if I fail**") proves the anxiety is fundamentally social, with a massive link to **Exam Phobia** (+0.514 correlation).

&nbsp;

**Recommendation:**

**Guide Parents on Academic Pressure:** Use parent-teacher meetings or workshops to discuss how excessive scolding or pressure over marks can increase students’ exam phobia and ultimately worsen future performance. Parents can be encouraged to focus more on learning and improvement.

&nbsp;

**Finding 6:**&nbsp;

Question D3 ("**Think about whether I have done such a problem before**") in the **Math Thinking** section mathematically predicts higher **Math Anxiety** (-0.239 correlation).

&nbsp;

**Recommendation:**

**Teach Students How to Approach Unfamiliar Problems:** Encourage students to break a difficult problem into smaller parts and use what they already understand. They should not panic or spend too much time trying to remember whether they have seen the same problem before.

&nbsp;

&nbsp;

**Footnote:**

Hypotheses H1, H2, and H3 are mathematically supported by the correlation data from survey items E5, C2, FN7, GN6, and EN3.&nbsp;

&nbsp;

&nbsp;**Our Team**

* Chief Patron: Bro. Placid Peter Rebeiro, CSC *(Principal, St. Gregory’s High School and College)*  
* Chief Co-patron: Bro. Leonard Chandan Rozario, CSC *(Vice-Principal, St. Gregory’s High School and College)*  
* Researchers: K. M. Imtiaz Hossain *(Lead Researcher, Mathematics Teacher, St. Gregory’s High School and College)* , Ms. Konika Akhtar *(Co-Researcher, Student Counsellor, St. Gregory’s High School and College)*  
* Advisor: Yet to be confirmed  
* Students' Research Team: Rupayan Bhuiyan, Sohail Abdullah Adib, Kashif Rayan, Shuvashis Debnath, Fardin Ahmed Fuad, Tahsinul Islam, Md. Mahbubur Rahman, Afnan Zaman, Zarif Mohammad Omar, Sheikh Zareef Ahmed, Redwan Al Mamun, Mohammud Nafiul Islam, Nuaimaan Al Ahnaf, Md. Shefaur Rahman Sadif *(Students, St. Gregory’s High School and College)*

&nbsp;
