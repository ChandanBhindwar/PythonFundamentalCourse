import random

users = []

user1 = input("Please enter your name : ")
users.append(user1)


user2 = input("Please enter your name : ")
users.append(user2)

user3 = input("Please enter your name : ")
users.append(user3)

user4 = input("Please enter your name : ")
users.append(user4)

user5 = input("Please enter your name : ")
users.append(user5)

winUser = random.choice(users)
favrateNo = random.randint(0, 9)
print(winUser)
print(favrateNo)

print("Congratulations!!! you are lucky user "+winUser+" " + str(favrateNo))
