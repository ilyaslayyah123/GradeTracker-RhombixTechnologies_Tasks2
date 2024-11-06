
print('Hello, this is a grading system ')
print("It uses the 100% scoring system")
from subject_detail import get_subject_details
import grade_calculat
subject_list = grade_calculat.LinkedList()
numsub = int(input("Enter number of subjects: "))


for _ in range(numsub):
    subject_name, total_score = get_subject_details()
    subject_list.add_subject(subject_name, total_score)

subject_list.display_results()

print("-----------------------------")
print("Thanks for trying it out.")

