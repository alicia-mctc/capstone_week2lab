from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

    def __str__(self):
        return f'Student name {self.name}, GPA: {self.gpa}'# format() gives better printout

def main():

    alice = Student('Alice', 12345, 4.0)# Student() method has three paramenters
    bob = Student('Bob', 98765, 3.8)
    
    print(alice)
    print(bob)
   

main()    
    

   
    