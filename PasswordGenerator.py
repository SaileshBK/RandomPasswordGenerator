#importing necessary modules
import random
import string
import os.path


print("Welcome to Password generator!")
passNumbers = int(input('\nEnter the number of password you want: '))
#input the length of password 
length = int(input('\nEnter the length of each password: '))

#our data
#string.ascii_letters contains lower and uppercase alphabets
# string.digits contains 0123456789
# string.punctuation has all the symbols (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

character = string.ascii_letters + string.digits + string.punctuation
#use random charcaters to create the password.



file_exists = os.path.exists('passwords.txt')

try:
  if file_exists==True:
    os.remove("passwords.txt")
    newFile = open('passwords.txt', 'x')
    newFile.write("\nList of " +str(passNumbers)+" passwords with "+str(length)+ " length :\n")
    # newFile.write(password)
    for i in range(1,passNumbers+1):
      newFile.write(str(i)+". ")
      newFile.write("".join(random.sample(character,length))+"\n")
    
    newFile = open('passwords.txt', 'r')
    data = newFile.read()
    print(data)
    newFile.close()


    
    # f = open("passwords.txt")
    # print(f.read())
    # f.close()
  else:
    newFile = open('passwords.txt', 'x')
    newFile.write("\nList of " +str(passNumbers)+" passwords with "+str(length)+ " length :\n")
    # newFile.write(password)
    for i in range(1,passNumbers+1):
      newFile.write(str(i)+". ")
      newFile.write("".join(random.sample(character,length))+"\n")
    
    newFile = open('passwords.txt', 'r')
    data = newFile.read()
    print(data)
    newFile.close()
except FileNotFoundError:
    print("The 'docs' directory does not exist")