**1.a. Evidence for running the Tool:**

This section demonstrates the successful execution of the PyGGI tool for automatic program repair. The process includes cloning the repository, installing prerequisites, and running PyGGI on example programs.

**Cloning the Repository**

Run the following command to clone the PyGGI repository:

_git clone <https://github.com/coinse/pyggi.git>_

![cloning report](image.png)

**Installing prerequisites:**

_Pip install pytest_

![Installing pytest](image-1.png)

**Installing pyggi**

&nbsp;_python setup.py install_

![Installing pyggi](image-2.png)


**Testing the tool:**

Script 1 demonstrates how to run PyGGI for repairing bugs in the Triangle_bug_python directory. The test cases ensure the correct classification of triangles (e.g., scalene, isosceles, equilateral) based on their side lengths.

**Results:**

The fitness value of the original program was 2.0. - After running PyGGI, the fitness improved to 1.0, demonstrating the tool's ability to generate valid patches.

![console showing output](image-3.png)

![console showing output](image-4.png)


**Log file:**

The log files generated during the repair process contain:

\- Mutations applied to the code (e.g., LineInsertion, LineDeletion).

\- Fitness values for each mutation.

\- Best patch identified during the run.

Example Log Entry:

SUCCESS 1.0 LineDeletion({'target': ('triangle.py', 16)})

![log file](c:\Users\shuva\OneDrive\Desktop\winter-2025\SOEN_691\Triangle_fast_python_1737757663.log)

![logfile](image-5.png)


**1.b. Provided test case and experiments:**

**Extent of Success:**

**We have successfully reproduced key aspects of the tool’s functionality, including:**

**i) Bug Repair:**

- Ran PyGGI on the Triangle_bug_python program to generate patches aimed at fixing errors in triangle classification.
- Observed improvements in the fitness value, indicating partial success in repairing the program.
- Evidence:
  - Logs showing fitness evaluations and mutations applied by PyGGI.
  - Test case results before and after applying the best patch.

**Command used:**

_python repair_python.py --project_path ../sample/Triangle_bug_python --mode line --epoch 10 --iter 50_

![alt text](image-6.png)

**Log files generated:**

![alt text](image-7.png)

![log file](c:\Users\shuva\OneDrive\Desktop\winter-2025\SOEN_691\Triangle_bug_python_1737943066.log)

![log file](image-8.png)

**Before applying patch:**

- The original program failed test cases due to incorrect triangle classification logic.
- Initial fitness value: High (indicating poor performance).
- Screenshot of pytest showing failing test cases.

![alt text](image-9.png)

![alt text](image-10.png)

**After applying patch:**

- The patch suggested by PyGGI improved fitness by passing additional test cases.
- Screenshot of pytest showing more test cases passing.

![alt text](image-11.png)

**ii) Performance Improvement:**

- Used PyGGI on the Triangle_fast_python example to optimize runtime performance.
- Achieved a measurable reduction in fitness value, reflecting incremental runtime improvement.
- Evidence:
- Logs showing the best patch identified by PyGGI.
- Runtime comparisons for the original and optimized versions.

**Command used:**

_python improve_python.py --project_path ../sample/Triangle_fast_python --mode line --epoch 5 --iter 20_

![alt text](image-12.png)

![alt text](image-13.png)

**Log file generated:**

![](c:\Users\shuva\OneDrive\Desktop\winter-2025\SOEN_691\Triangle_fast_python_1737945979.log)

![alt text](image-14.png)

**Before Applying the Patch :**

The original program exhibited higher runtime due to unnecessary operations and inefficient logic.

![alt text](image-15.png)

**After Applying the Patch:**

PyGGI identified a mutation (removing an unused import) that slightly reduced runtime.

![alt text](image-16.png)

**Run time improvement:**

The total runtime before and after applying the patch was recorded, showing a slight improvement due to the removal of an unused import statement.

![alt text](image-17.png)

**Challenges Faced:**

1. Parse Errors:
    - Many mutations caused syntax errors (PARSE_ERROR), limiting the success rate of patches.
    - Example: Deleting critical lines like variable initialization.
2. Small Program Size:
    - The simplicity of triangle.py increased the likelihood of critical errors from random mutations.
3. Fitness Function Limitations:
    - The reliance on test case results led to misleading improvements.
    - Example: Removing unused imports improved runtime but had no significant impact on program functionality.

**2\. Why do you select the tool?**

I selected PyGGI because it is a Python-based automated program repair (APR) tool that aligns with my learning goals and assignment requirements. Since I am new to APR and Python, I wanted a lightweight, modifiable tool that allows for hands-on experimentation. PyGGI is specifically designed to enable researchers and students to understand and explore the principles of APR without the complexity of more advanced tools.

**Does it represent the state-of-the-art or is it a classical tool?**

While PyGGI is not state-of-the-art in terms of using advanced machine learning techniques, it represents a modern and flexible approach to APR, particularly for Python programs. Unlike classical tools such as GenProg, which are designed primarily for C programs, PyGGI focuses on simplicity, allowing users to easily modify and extend its capabilities.

**Any reason that helped formulate the research questions?**

The design and functionalities of PyGGI inspired the following research questions:

**1\. Fitness Function:**

- **Observation**: PyGGI’s success depends heavily on the fitness function, which evaluates patches based on test case outcomes.
- **Research Question**: What are the limitations of PyGGI’s fitness function, especially when test cases are incomplete or ambiguous?

**2\. Parameter Tuning:**

- **Observation**: Parameters like iterations and epochs directly impact PyGGI’s performance.
- **Research Question**: How does the number of iterations and epochs in PyGGI affect repair quality and efficiency?

**3\. Mutation Operators:**

- **Observation**: PyGGI generates patches using mutation operators (e.g., insertion, deletion, replacement). Their effectiveness varies depending on the program and context.
- **Research Question**: Which mutation operators are most effective for generating valid patches in Python programs?

**3\. Research Questions:**

1\. Limitations of the Fitness Function in PyGGI

- Research Question: What are the limitations of PyGGI's fitness function in evaluating program patches, especially with incomplete or ambiguous test cases?
- Rationale:
  - The fitness function is central to PyGGI's operation, guiding the tool to identify the best patches. However, its reliance on test cases introduces challenges:
    - **Ambiguity**: Test cases might pass but fail to cover all program functionalities, leading to incorrect fitness evaluations.
    - **Incomplete Test Coverage**: Missing edge cases may cause PyGGI to produce patches that pass tests but break program logic.
  - Investigating this limitation will provide insights into improving the fitness function to handle real-world scenarios where test cases are often incomplete or imperfect.

2\. Impact of Iterations and Epochs on Repair Quality

- Research Question: How does the number of iterations and epochs in PyGGI affect the quality and efficiency of program repair?
- Rationale:

• PyGGI uses a search-based approach, refining patches over iterations and epochs. Understanding the trade-offs between:

- - Computational Cost: Increasing epochs/iterations consumes more resources.
    - Repair Quality: More iterations might find better patches but risk diminishing returns.

• Exploring this question provides:

- - Guidelines for optimal parameter tuning in varying scenarios.
    - Insights into the relationship between search depth and repair effectiveness, balancing runtime efficiency with repair accuracy.

3\. Effectiveness of Mutation Operators in PyGGI

- Research Question: Which mutation operators (e.g., line insertion, deletion, replacement) are most effective in generating valid patches for Python programs?
- Rationale:
  - PyGGI’s patch generation relies on mutation operators, which introduce changes to the program. These operators vary in impact:
    - Line Deletion: Risky for small programs but can simplify code.
    - Line Insertion: Useful for adding missing logic but may introduce redundancy.
    - Line Replacement: Balances flexibility and risk by altering existing code.
  - This question evaluates the effectiveness of each operator, identifying their strengths and weaknesses in different repair contexts. The findings can guide future development, emphasizing operators that yield the best results.

**4.Evaluation Plan:**

| **Research Question** | **Metrics/Steps** | **Dataset/Benchmark** | **Timeline** |
| --- | --- | --- | --- |
| **1\. Limitations of the Fitness Function in PyGGI** | \- Success rate: % of patches passing all test cases. | triangle.py with complete test cases. | Week 1 |
| \- Fitness values: Compare scores with incomplete or ambiguous test cases. | \- Create incomplete/ambiguous test cases. | &nbsp; |
| \- Analyze behavior: Check if patches are valid or introduce unexpected behavior. | &nbsp; | &nbsp; |
| **2\. Impact of Iterations and Epochs on Repair Quality** | \- Fitness improvement: Measure best fitness scores for different epoch and iteration configurations. | triangle.py test cases. | Week 2 |
| \- Runtime: Record the time taken for each configuration. | &nbsp; | &nbsp; |
| \- Observe diminishing returns: Compare fitness improvements as epochs/iterations increase. | &nbsp; | &nbsp; |
| **3\. Effectiveness of Mutation Operators in PyGGI** | \- Success rate: % of patches passing test cases for each mutation operator (insertion, deletion, replacement). | triangle.py test cases. | Week 3 |
| \- Fitness values: Measure how each operator affects fitness improvements. | &nbsp; | &nbsp; |
| \- Operator frequency: Analyze which operators are most frequently present in successful patches. | &nbsp; | &nbsp; |