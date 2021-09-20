# Santosh Khadka
# What if we have to open every file in a directory?
# What if we want to actually move files around on our computer?

import os       # Allows for command line style commands
import shutil   # Move files around
import send2trash   # Delete files to resycle bin. pip install send2trash
f = open("practice.txt", 'w+')
f.write("Santosh Khadka")
f.close()

print(os.getcwd())    # Works because of os
# print(str(os.getcwd()).replace("\\", "\\\\"))   # Replace \ with \\
# print(os.listdir())     # same as ls command
# print(os.listdir('C:\\Users\\PC-SK\\Desktop\\GIT_STUFF\\MINE\\learning_algos\\Learning-python'))        # print all files in 'directory'
# print(os.listdir('C:\\Users\\PC-SK\\Desktop\\GIT_STUFF\MINE\\learning_algos\\Learning-python'))         # Need to use \\ instead of \
    
# shutil.move('practice.txt', 'C:\\Users\\PC-SK\\Desktop\\GIT_STUFF\\MINE\\learning_algos\\Learning-python\\Section 14 - Advanced Python Modules\\end')     # Error if specified file not found

'''
Deleting Files

NOTE: The os module provides 3 methods for deleting files:

    os.unlink(path) which deletes a file at the path your provide
    os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
    shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. 
    
    All of these methods can not be reversed! Won't be able to recover the file. 
    Instead use send2trash module: Safer alternative that sends deleted files to trash bin instead of permanent delete.
    
    send2trash: pip install send2trash     
'''
# print('Before delete:   ', os.listdir())
# send2trash.send2trash('practice.txt')
# print('After delete:    ', os.listdir())