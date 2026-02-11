#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt",)
print(nb_characters_added)

cat file_append.txt
cat: file_append.txt: No such file or directory
./2-main.py
24
cat file_append.txt
This School is so cool!
./2-main.py
24
cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu: ~/$
