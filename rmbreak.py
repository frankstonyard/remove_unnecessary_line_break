import pyperclip
import os

filename = 'note.txt'
filenameW = 'noteW.txt'
content = ''

fo = open(filenameW, 'w', encoding='utf-8')
f = open(filename, 'r', encoding='utf-8')

lines = f.readlines()
for eachline in lines:
    content += eachline.strip() + ' '

os.system('cls')
print(content)
pyperclip.copy(content)
fo.writelines(content) 

f.close()
fo.close()
