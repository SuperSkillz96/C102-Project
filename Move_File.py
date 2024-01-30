import os
import shutil

from_dir = 'C:/Users/Ravit/Downloads'
to_dir = 'C:/Users/Ravit/OneDrive/Documents/Home/Ravit/BYJU Coding/Class Projects/Module 3'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        #File you want to move
        path1 = from_dir + '/' + file_name 

        #Create folder in variable called 'Image Files'    
        path2 = to_dir + '/' + "Document_Files"  

        #Copying file to here          
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print('Moving' + file_name)
            shutil.move(path1, path3)
            print('File has been moved successfully!')
        else:
            os.makedirs(path2)
            print('Moving' + file_name)
            shutil.move(path1, path3)
            print('File has been moved successfully!')