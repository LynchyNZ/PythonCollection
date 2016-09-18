import glob
import os
'''Renames all .jpg files in current folder to numbers starting from 1, using zfill to pad zeros
   Takes three parameters e.g. print(FileRenamer(1, 4, ".jpg")) which starts at 1, padded to 4 digits for all .jpg files
   Start - Number to start images from
   Padding - Length of filname, padded with zeros (e.g. 47 with a padding of 4 -> 0047.jpg). Use 0 for no padding
   Extension - File extension of files to rename
   
   FileRenamer written by Daniel Lynch
   Last updated: 14/05/2016
   www.lynchy.co.nz'''
def FileRenamer(start, padding, extension):
    files = glob.glob("*" + extension) 
    files.sort()
    count = start
    if len(files) == 0:
        message = ("No files found with the extension: " + extension)
    else:
        for f in files:
            n = str(count).zfill(padding) + extension
            print("Before: " + f + "   After: " + n) 
            try:
                os.rename(f, n)
            except:
                print("An error occured while attempting to rename a file!")
            count += 1
        message = "Images renamed by Lynchy's File Renamer script :)"
    return message
            
print(FileRenamer(1, 4, ".jpg"))
