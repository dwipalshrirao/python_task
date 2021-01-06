import re

with open("5.read_file_of_5.txt",'r') as f:
    data=f.read()
    print(len(re.split(' |,|\.|\n',data)))
