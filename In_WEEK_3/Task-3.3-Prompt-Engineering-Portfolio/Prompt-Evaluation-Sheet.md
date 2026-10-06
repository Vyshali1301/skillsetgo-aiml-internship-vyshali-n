# Task 3.3 - Prompt Engineering Portfolio

**Skill Set Go EduTech - AI/ML Internship - Week 3**

## Objective

Design and test LLM prompts across four categories - reasoning, extraction, summarization, and coding - and document how each prompt was iterated and what changed in the output.

---

## 1. Reasoning prompt

**Task:** Calculate the amount of money remaining after two sequential expenses.

| | Prompt | Output (summary) | Notes |
|---|---|---|---|
| v1 | A student has 500 rupees. She spends 20% of her money on books and then spends 25% of the remaining money on food. How much money does she have left? | The answer was 300 rupees. The response calculated the expenses and gave the final remaining amount. | The answer was correct, but the prompt did not explicitly ask for the calculation steps. |
| v2 (improved) | Solve this problem step by step. First calculate the amount spent on books, then calculate the remaining money, then calculate the amount spent on food, and finally give the remaining amount. Clearly show all calculations and the final answer. | The response clearly calculated 20% of 500 as 100, leaving 400. It then calculated 25% of 400 as 100, leaving 300 rupees. | The improved prompt gave a clearer and more structured solution because it specified the required steps. |

**Technique used to improve it:** Added step-by-step instructions and broke the problem into smaller sub-steps.

---

## 2. Extraction prompt

**Task:** Extract names, workshop details, locations, dates, and registration fees from a paragraph.

| | Prompt | Output (summary) | Notes |
|---|---|---|---|
| v1 | Extract the important information from this paragraph: Rahul attended a Python workshop in Hyderabad on 12 September 2026. He paid ₹1,500 for registration. Priya attended the same workshop in Bengaluru on 14 September 2026 and paid ₹1,200. | The response identified Rahul, Priya, the Python workshop, the two cities, dates, and registration fees. | The information was extracted correctly, but the output format was not specifically defined. |
| v2 (improved) | Extract the following information from the paragraph: person's name, workshop, city, date, and registration fee. Return the result as a table with exactly these columns: Name \| Workshop \| City \| Date \| Fee. Do not add information that is not present in the text. Text: Rahul attended a Python workshop in Hyderabad on 12 September 2026. He paid ₹1,500 for registration. Priya attended the same workshop in Bengaluru on 14 September 2026 and paid ₹1,200. | The response returned the extracted information in a structured table with Name, Workshop, City, Date, and Fee columns. | The improved prompt produced a more organized and consistent result by specifying the exact fields and output format. |

**Technique used to improve it:** Specified the exact information fields and required a structured table format.

---

## 3. Summarization prompt

**Task:** Summarize a short passage about Artificial Intelligence.

**Text used:**

Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence. These tasks include learning, reasoning, problem solving, understanding language, and recognizing images. AI is used in healthcare, education, banking, transportation, and entertainment. Machine learning is an important part of AI that allows systems to learn patterns from data without being explicitly programmed for every task. Although AI provides many benefits, it also creates challenges related to privacy, bias, security, and employment.

| | Prompt | Output (summary) | Notes |
|---|---|---|---|
| v1 | Summarize this text. | The response summarized AI as technology that allows machines to perform intelligent tasks. It mentioned applications, machine learning, and some challenges. | The summary was useful but the length, format, and important points were not specifically controlled. |
| v2 (improved) | Summarize the following text in exactly 4 bullet points using simple language suitable for a college student. Include the definition of AI, its major applications, the role of machine learning, and the main challenges. Do not add information that is not present in the original text. [Text provided above] | The response produced four concise bullet points covering the definition of AI, its applications, machine learning, and challenges such as privacy, bias, security, and employment. | The improved version was more focused, easier to read, and covered the required points because the length, audience, format, and content were specified. |

**Technique used to improve it:** Added a specific length, target audience, required points, and bullet-point format.

---

## 4. Coding prompt

**Task:** Write a Python program to find the largest number in a list.

| | Prompt | Output (summary) | Notes |
|---|---|---|---|
| v1 | Write a Python program to find the largest number in a list. | The response provided a simple Python program to find the largest value in a list. | The prompt was very general and did not specify restrictions, edge cases, test cases, or complexity. |
| v2 (improved) | Write a Python 3 program to find the largest number in a list without using the built-in `max()` function. Handle an empty list safely. Include three test cases with expected outputs and briefly explain the time complexity. | The response provided Python 3 code using iteration instead of `max()`. It included handling for an empty list, three test cases, expected outputs, and an explanation of the time complexity. | The improved prompt produced a more complete and practical solution by adding constraints, edge-case handling, tests, and complexity requirements. |

**Technique used to improve it:** Specified the programming language/version, added constraints, required edge-case handling, test cases, and time-complexity analysis.

---

## 5. Overall reflection

The experiments showed that specific prompts produced more useful and consistent results than general prompts. Adding output formats, constraints, examples, and edge-case instructions improved the quality of the responses. Breaking complex tasks into smaller steps was especially useful for reasoning and coding tasks. My first step when a prompt does not work is now to identify what is missing and add clear instructions about the expected output.