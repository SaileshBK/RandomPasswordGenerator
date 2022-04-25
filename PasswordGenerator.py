#importing necessary modules
import random
import string
import os.path

def main():
  
  print("Welcome to Password generator!")
  passNumbers = int(input('\nEnter the number of password you want: '))
  #input the length of password 
  length = int(input('\nEnter the length of each password: '))

  #our data
  #string.ascii_letters contains lower and uppercase alphabets
  # string.digits contains 0123456789
  # string.punctuation has all the symbols (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
  #use random charcaters to create the password.
  character = string.ascii_letters + string.digits + string.punctuation
  
  file_exists = os.path.exists('passwords.txt')
  try:
    if file_exists==True:
      #This removes the text file if it exists to create a new one.
      os.remove("passwords.txt")
      print(passGenerator(passNumbers,length,character))
  
    else:
       print(passGenerator(passNumbers,length,character))
  except FileNotFoundError:
    print("The 'docs' directory does not exist")


#password generator function
def passGenerator(passNumbers,length,character):
  #creating a new file.
  newFile = open('passwords.txt', 'x')
  newFile.write("\nList of " +str(passNumbers)+" passwords with "+str(length)+ " length :\n")
  # writing passwords in new text file.
  for i in range(1,passNumbers+1):
    newFile.write(str(i)+". ")
    newFile.write("".join(random.sample(character,length))+"\n")

  #Making the file readable
  newFile = open('passwords.txt', 'r')
  data = newFile.read()
  newFile.close()

  return data


#main
if __name__ =="__main__":
  main()
