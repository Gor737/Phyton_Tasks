def openFile(fileName):
    try:
      with open(fileName,"r") as file:
        fileContent=file.read()
    except FileNotFoundError:
       print(f"{fileName} file not exist.")       
       fileName=input("enter valid file name -> ")
       openFile(fileName)
    print(fileContent)
    '''return fileName'''
   

def  writeFile(fileName):
    userChoice = input("Do you want to write to the same file (yes/no)? ")
    if(userChoice.lower()=="yes"):
      with open(fileName,"w") as file:
        writeText=input("Enter the content you want to write to the file:")
        file.write(writeText)
    else: 
       newFileName=input("enter new file name : ")
       try:
         with open(newFileName, "w") as file:
            writeText = input("Enter the content you want to write to the file: ")
            file.write(writeText)
       except FileNotFoundError:
          print(f"The file {newFileName} does not exist.") 
       newFileName = input("Enter a valid file name: ")
       writeFile(newFileName)
       file.close()
       
   
fileName=input("text file name -> ")
openFile(fileName)
writeFile(fileName)
print("The file has been closed.")
