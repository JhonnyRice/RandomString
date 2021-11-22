# V 1.1 Code compacted, now it works (weeeee)
import random
latin_l = "abcdefghijklmnopqrstuvwxyz"
latin_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb4password = "@#!£$%&"


def GenerateRandomString(lenght):
    return ''.join(random.choice(latin_l + latin_u) for i in range(lenght))
def GenerateRandomNumber(lenght):
    return ''.join(random.choice(num) for i in range(lenght))
def GenerateRandomLowercaseString(lenght):
    return ''.join(random.choice(latin_l) for i in range(lenght))
def GenerateRandomUppercaseString(lenght):
    return ''.join(random.choice(latin_u) for i in range(lenght))
def GenerateRandomPassword(lenght):
    return ''.join(random.choice(latin_l + latin_u + num + symb4password) for i in range(lenght))
