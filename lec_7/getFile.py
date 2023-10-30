def openFile(name):
    try:
      with open(name,"r") as file:
        fileContent=file.read()
    except FileNotFoundError:
       print(f"{name} file not exist.")       
       fileName=input("enter valid file name -> ")
       openFile(name)
    print(fileContent)
    '''return fileName'''
   

def  writeFile(name):
    userChoice = input("Do you want to write to the same file (yes/no)? ")
    if(userChoice.lower()=="yes"):
      with open(name,"w") as file:
        writeText=input("Enter the content you want to write to the file:")
        file.write(writeText)
    else: 
       newName=input("enter new file name : ")
       try:
         with open(newName, "w") as file:
            writeText = input("Enter the content you want to write to the file: ")
            file.write(writeText)
       except FileNotFoundError:
          print(f"The file {newName} does not exist.") 
       newName = input("Enter a valid file name: ")
       writeFile(newName)
       file.close()
       
   
name=input("text file name ---> ")
openFile(name)
writeFile(name)
print("The file has been closed.")
