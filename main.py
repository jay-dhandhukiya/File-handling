from pathlib import Path
import os
# Function to read and list all files and folders in the current directory
def readfileandfolder():
     path = Path('')
     items = list(path.rglob('*'))
     for index,items in enumerate(items):
          print(f"{index+1} : {items}")

# Function to create a file
def createfile():
     try:
          readfileandfolder()
          name = input("Enter the name of the file to create: ")
          path = Path(name)
          if not path.exists():
               with path.open('w') as file:
                    write = input("Enter the content to write in the file: ")
                    file.write(write)

               print(f"File '{name}' created successfully.")
          else:
               print(f"File '{name}' already exists.")
     except Exception as err:
          print(f"An error occurred: {err}")
     pass

# Function to read a file
def readfile():
     try:
          readfileandfolder()
          name = input("Enter the name of the file to read: ")
          path = Path(name)
          if path.exists() and path.is_file():
               with path.open('r') as file:
                    Data = file.read()
                    print(Data)
               print(f"File '{name}' read successfully.")
          else:
               print(f"File '{name}' does not exist or is not a file.")
     except Exception as err:
          print(f"An error occurred: {err}")

# Function to update a file
def updatefile():
     try:
          readfileandfolder()
          name = input("Enter the name of the file to update: ")
          path = Path(name)
          if path.exists() and path.is_file():
               print("press 1 for changing filename :- ")
               print("press 2 for overwriting file :- ")
               print("press 3 for appending file :- ")

               res = int(input("Enter your choice: "))

               if res == 1:
                    newname = input("Enter the new name of the file: ")
                    path.rename(newname)

               elif res == 2:
                    with path.open('w') as file:
                         write = input("Enter the content to write in the file: ")
                         file.write(write)

               elif res == 3:
                    with path.open('a') as file:
                         append = input("Enter the content to append in the file: ")
                         file.write(" " + append)

               print(f"File '{name}' updated successfully.")
          else:
               print(f"File '{name}' does not exist or is not a file.")
     except Exception as err:
          print(f"An error occurred: {err}")

# Function to delete a file
def deletefile():
     try:
          readfileandfolder()
          name = input("Enter the name of the file to delete: ")
          path = Path(name)
          if path.exists() and path.is_file():
               os.remove(name)
               print(f"File '{name}' deleted successfully.")
          else:
               print(f"File '{name}' does not exist or is not a file.")
     except Exception as err:
          print(f"An error occurred: {err}")

print("press 1 for createing a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
     readfile()

if check == 3:
     updatefile()

if check == 4:
     deletefile()

    