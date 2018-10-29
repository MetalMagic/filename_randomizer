from random import randint
import os
import sys

print("WARNING: This program randomizes all of the filenames in a directory.",
      "\nIf you use this in the wrong directory you could mess something up.")

print("\n*Note* This program cannot properly identify all file extensions with multiple '.' characters.",
      "\nTherefore any filenames with multiple '.' characters will not be randomized.\n")

characters = [] #list of characters we'll use to randomize the filenames

#add lowercase alphabet a-z to the characters list
for i in range(97,123): 
    characters.append(chr(i))

#add numbers from 0-9 to the characters list
for i in range(48,58): 
    characters.append(chr(i))

#add the uppcase alphabet A-Z to the characters list
for i in range(65,91): 
    characters.append(chr(i))
    
    
#randomFilename receives a list of characters as a parameter and returns
#a random string of length 30-60 using those characters
def randomFilename(characters):
        nameSize = randint(30,60)
        name = ""
        for i in range(nameSize):
                name = name + characters[randint(0, len(characters) - 1)]
        return name

request = ""
while not (request == "single" or request == "directory"):
    request = input("If you would like to randomize just one filename enter 'single' \nIf you would like randomize an entire directory enter 'directory' ")
        
 
if request == "single": #randomize a single file
    directory = input("Enter the full path to the directory with the file you would like to randomize: ")   #get the directory
    filename = input("Enter the name of the file you would like to randomize: ")    #get the filename
    
    confirm = "no"  
    while confirm != "yes": #get the user to confirm before we start renaming files
        confirm = input("Renaming the file " + filename + " in " + directory + "\nif this is correct type \"yes\" otherwise close the program: ")
        if filename.count(".") == 1:    #if there is exactly 1 '.' in the filename

                #split the filename to get the extension
                filename, extension = os.path.splitext(directory + "\\" + filename)

                isDuplicate = True
                while isDuplicate:      #check each file to make sure the new name is not a duplicate
                        newFilename = randomFilename(characters) + extension #get the new name
                        isDuplicate = False
                        for file in os.listdir(directory):
                                if file == newFilename:
                                        isDuplicate = True
                
                os.rename(filename + extension, directory + "\\" + newFilename) #rename the file
    
    input("Done ") #do this so the console window won't close immediately
    
    
elif request == "directory":    
        
    directory = input("Enter the full path of the directory you would like to randomize: ") #get the directory  

    confirm = "no"  
    while confirm != "yes": #get the user to confirm before we start renaming files
            confirm = input("Renaming all files in " + directory + 
                    "\nif this is correct type \"yes\" otherwise close the program: ")

    for filename in os.listdir(directory):
            if filename.count(".") == 1:    #if there is exactly 1 '.' in the filename

                    #split the filename to get the extension
                    filename, extension = os.path.splitext(directory + "\\" + filename)

                    isDuplicate = True
                    while isDuplicate:      #check each file to make sure the new name is not a duplicate
                            newFilename = randomFilename(characters) + extension #get the new name
                            isDuplicate = False
                            for file in os.listdir(directory):
                                    if file == newFilename:
                                            isDuplicate = True
                    
                            
                    os.rename(filename + extension, directory + "\\" + newFilename) #rename the file

    input("Done ") #do this so the console window won't close immediately

            
