name = input("Enter your name: ") 
class SubjectNode:

    def __init__(self, subject_name, score):
        self.subject_name = subject_name
        self.score = score
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_subject(self, subject_name, score):
        new_node = SubjectNode(subject_name,score)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display_results(self):
        current = self.head
        print("\nResults:")
        
        a=0
        total_marks=0
        while current:
            total_marks=total_marks+current.score
            print("------------------------------")
            print(f"Subject: {current.subject_name}, Score: {current.score}")
            if current.score == 100:
                print(f"{name}, Congratulations! This is an outstanding performance. Your total is {current.score}")
            elif current.score >= 80:
                print(f"{name}, You got in {current.subject_name} grade A.")
            elif current.score >= 70:
                print(f"{name}, You got in {current.subject_name} grade B. ")
            elif current.score >= 60:
                print(f"{name}, You got in {current.subject_name} grade C. ")
            elif current.score >= 50:
                print(f"{name}, You got in {current.subject_name} grade D. ")
            elif current.score >= 40:
                print(f"{name}, You got in {current.subject_name} grade f. ")
            else:
                print(f"{name}, You have in {current.subject_name} failed. ")
            current = current.next
            a+=1
        print("------------------------------")
        print(f"Total number of subjects: {a}")
        print(f"Total marks: {total_marks}/{a*100}")
        average=total_marks/a
        if average >= 80:
            print(f"{name}, You got in {average} grade A.")
        elif average >= 70:
            print(f"{name}, You got in {average} grade B. ")
        elif average >= 60:
            print(f"{name}, You got in {average} grade C. ")
        elif average >= 50:
            print(f"{name}, You got in {average} grade D. ")
        elif average >= 40:
            print(f"{name}, You got in {average} grade f. ")
        else:
            print(f"{name}, You have in {average} failed. ")

                  
            

        

            
        


