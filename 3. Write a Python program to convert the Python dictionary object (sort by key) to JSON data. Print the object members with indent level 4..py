import json

dict={'a':1,'d':2,'e':3,'d':4,'b':5,'f':6,'c':7}

keys=sorted(dict)
sorted_dict={i: dict[i] for i in keys}
print(json.dumps(sorted_dict,indent=4))