# GradeTracker

GradeTracker is a Python-based grading system that allows users to input their scores for different subjects, calculate grades, and view results based on a 100% scoring system. The project tracks the scores for assignments, quizzes, and exams, and provides feedback on each subject as well as an overall performance summary.

## Features

- Allows users to enter the name and scores for multiple subjects.
- Calculates the total score for each subject and displays the corresponding grade.
- Provides an overall grade based on average marks.
- Includes validation to ensure scores are within the range of 0 to 100.

## Project Structure

GradeTracker/ │ ├── main.py # Main file to run the application ├── subject_detail.py # Contains functions for entering subject details and validating input ├── grade_calculat.py # Implements the LinkedList structure and grade calculation logic └── README.md # This README file


## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/GradeTracker.git
   cd GradeTracker
   
(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Usage
# 1.Running the Project
To run the program, execute the main.py file. You can do this directly in the command line or terminal:
python main.py
# 2. Input Prompts
You will be prompted to input:

Your name
The number of subjects
For each subject: the name, assignment score, quiz score, and exam score
# Example:
Hello, this is a grading system
It uses the 100% scoring system
Enter number of subjects: 2
---------------------------------------
Enter name of subject: Math
Enter obtained assignment marks: 80
Enter your obtained quiz marks: 90
Enter your obtained Exam score: 85
---------------------------------------
Enter name of subject: Science
Enter obtained assignment marks: 70
Enter your obtained quiz marks: 75
Enter your obtained Exam score: 80
-----------------------------
Results:
------------------------------
Subject: Math, Score: 255
John, You got in Math grade A.
------------------------------
Subject: Science, Score: 225
John, You got in Science grade B.
------------------------------
Total number of subjects: 2
Total marks: 450/200
John, Your average score is 75.0. You got grade B.
Thanks for trying it out.
# 3. Grading System
The grade is calculated based on the following criteria:

100: Outstanding performance
80-100: Grade A
70-79: Grade B
60-69: Grade C
50-59: Grade D
40-49: Grade F
Below 40: Failed
# Code Explanation
# main.py
This is the entry point of the application. It collects the user input for the subjects and calls the relevant functions from subject_detail.py and grade_calculat.py to process the data and display the results.
# subject_detail.py
This file contains the get_subject_details() function that handles user input for subject names and their respective marks (assignments, quizzes, exams). It ensures the total score doesn't exceed 100 and validates individual score inputs.
# grade_calculat.py
This file implements the LinkedList data structure to store subjects and their scores. The display_results() function outputs the grades and total scores for each subject and calculates the overall average and grade.
# Improvements and Future Features
Implement file-based storage for subjects and results, so users can save their data and access it later.
Add a graphical user interface (GUI) using Tkinter or PyQt to make the system more user-friendly.
Add support for different grading systems, such as weighted grades or letter grades.
Allow the user to edit or delete previously entered subjects.
# License
This project is licensed under the MIT License - see the LICENSE file for details.
# Contact
For questions or feedback, feel free to reach out via email.
1. **Repository URL:** .
2. **Email Contact:** ilyaslayyah786@gmail.com 


