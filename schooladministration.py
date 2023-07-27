class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Grade: {self.grade})"
class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)
def main():
    school = School()
    student1 = Student("Kohli", 16, 9)
    student2 = Student("Aash", 16, 7)
    student3 = Student("Mahi", 16, 10)
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    print("List of Students:")
    school.display_students()

if __name__ == "__main__":
    main()
