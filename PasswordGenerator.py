#importing necessary modules
import random
import string


print("Welcome to Password generator!")
#input the length of password 
length = int(input('\nEnter the length of password: '))

#our data
#string.ascii_letters contains lower and uppercase alphabets
# string.digits contains 0123456789
# string.punctuation has all the symbols (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

character = string.ascii_letters + string.digits + string.punctuation
#use random charcaters to create the password.
password = "".join(random.sample(character,length))
#print the password
print(password)