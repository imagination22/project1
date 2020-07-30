class Coder:
    def __init__(self, name, rollno, role):
        self.name = name
        self.rollno = rollno
        self.role = role

    def guide(self):
        print("i know pretty much manny things")

    def frontend(self):
        if self.role == "frontend":
            print("i am responsible for ui,ux and flutter work")
        else:
            print("there is a mistake in my role")

    def backend(self):
        print("i dont know what to do")


if __name__ == "__main__":
    student1 = Coder("Shubham", 50, "frontend")
    student2 = Coder("yash", 50, "backend")
    student3 = Coder("Shubham", 50, "frontend")
    student4 = Coder("Shubham", 50, "frontend")
    student1.frontend()
    student2.backend()

