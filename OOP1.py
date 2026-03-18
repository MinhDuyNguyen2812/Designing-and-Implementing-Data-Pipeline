class Person:
    def __init__(self, fname, lname, age, job):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.job = job

Data = Person("Matti", "Nguyen", 25, "Student")

print(Data.fname, Data.lname, Data.age, Data.job)