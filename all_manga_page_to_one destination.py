import os, sys
import shutil
''' 
All manga page to one destination
    the path like :
        C:/directory (even on unix)
    the structure of the files must be like this :
            directory/folder/file.endwith
    ex:
        Kakegurui/chap1 / page1.jpg
                          page2.jpg
                          .
                          .
                 /chap2
                 .
                 .
                 .
'''
endwith='jpg'                       
path = "C:/directory"
directory = os.listdir( path )
destination='C:/destination'
photo_number = 0
for folder in directory:
    print (folder)
    for file in os.listdir(f'{path}/{folder}'):
        print(f'{photo_number} _____  {file}')
        shutil.copy2(f'{path}/{folder}/{file}', f'{destination}/{str(photo_number)}.{endwith}')
        print(f'page number : {photo_number} Done .')
        photo_number = photo_number +1





