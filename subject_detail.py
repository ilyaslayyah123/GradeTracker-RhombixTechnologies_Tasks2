def get_subject_details():
    print("---------------------------------------")
    subject_name = input("Enter name of subject: ")
    assignmint = int(input("Enter obtained assignmints marks: "))
    quiz = int(input("Enter your obtained quises marks: "))
    exam = int(input("Enter your obtained Exam score: "))
    total_score = quiz + assignmint + exam

    
    while total_score > 100:
        print("This score is invalid. Total should not exceed 100.")
        assignmint = int(input("Enter your obtained assignmints marks: "))
        quiz = int(input("Enter your obtained quises marks: "))
        exam = int(input("Enter your obtained Exam score: "))
        total_score = assignmint + quiz + exam
    
    return subject_name, total_score
    
