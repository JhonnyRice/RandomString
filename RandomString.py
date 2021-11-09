# V 1.0 Release lol
import random
latin_l = "abcdefghijklmnopqrstuvwxyz"
latin_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb4password = "@#!£$%&"
def GenerateRandomString(lenght):
    for i in range(lenght):
        RandomString = random.choice(latin_l + latin_u)
        print(RandomString, end="")
def GenerateRandomNumber(lenght):
    for i in range(lenght):
        RandomString = random.choice(num)
        print(RandomString, end="")
def GenerateRandomLowercaseString(lenght):
    for i in range(lenght):
        RandomString = random.choice(latin_l)
        print(RandomString, end="")
def GenerateRandomUppercaseString(lenght):
    for i in range(lenght):
        RandomString = random.choice(latin_u)
        print(RandomString, end="")
def GenerateRandomPassword(lenght):
    for i in range(lenght):
        RandomString = random.choice(latin_l + latin_u + num + symb4password)
        print(RandomString, end="")
