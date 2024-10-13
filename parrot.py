class Dog:
    animal = "Dog"
    
    def __init__(self, breed, color, angerLevel, sillyLevel, ):
        self.breed = breed
        self.color = color
        self.angerLevel = angerLevel
        self.sillyLevel = sillyLevel
        
lucy = Dog("Golden retriver", "golden", 3, 8)
jacky = Dog("Pitbull", "Black and white", 5, 7)
leo =  Dog("German shepherd", "golden and black", 5, 6)
tommy = Dog("Bulldog", "grey", 7, 4)
todo = Dog("American eskimo dog", "white", 2, 9)

name = input("Chose one of them (Lucy/Jacky/Leo/Tommy/Todo):  ")

if name == 'Lucy' or name == 'lucy':
     print(f"Lucy is a {lucy.animal} and her breed is {lucy.breed}! Her anger level is {lucy.angerLevel} and silly level is {lucy.sillyLevel}!!! :3")

elif name == 'Jacky' or name == 'jacky':
    print(f"Jacky is a {jacky.animal} and his breed is {jacky.breed}! his anger level is {jacky.angerLevel} and silly level is {jacky.sillyLevel}!!! :3")
elif name == 'Leo' or name == 'leo':
    print(f"Leo is a {leo.animal} and his breed is {leo.breed}! his anger level is {leo.angerLevel} and silly level is {leo.sillyLevel}!!! :3")
elif name == 'Tommy' or name == 'tommy':
    print(f"Tommy is a {tommy.animal} and his breed is {tommy.breed}! his anger level is {tommy.angerLevel} and silly level is {tommy.sillyLevel}!!! :3")
elif name == 'Todo' or name == 'todo':
     print(f"Todo is a {todo.animal} and her breed is {todo.breed}! Her anger level is {todo.angerLevel} and silly level is {todo.sillyLevel}!!! :3")
