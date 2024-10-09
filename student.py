class Student:
    #class variable
    grade = 7
    print(f"I am a student of grade {grade}")
    
    #Creating constructor function
    def __init__(self, name,age,height):
        self.name = name
        self.age = age
        self.height = height

rose = Student("Rose", 14, 5.3)
nabila = Student("Nabila", 13, 5.5) 
nusaiba = Student("Nusaiba",14, 5.0) 

print(f"Name: {rose.name}\nAge:{rose.age}\nHeight: {rose.height}\n")
print(f"Name: {nabila.name}\nAge:{nabila.age}\nHeight: {nabila.height}\n") 
print(f"Name: {nusaiba.name}\nAge:{nusaiba.age}\nHeight: {nusaiba.height}\n")
  
print(f"Rose grade: {rose.grade}")
print(f"Nabila grade: {nabila.grade}")
print(f"Nusaiba grade: {nusaiba.grade}")