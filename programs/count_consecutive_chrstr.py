string = "aaabbbcceddbbaa"
count = 1
result = " "
if len(string)>1:
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count+=1
        else:
            result+=string[i-1]+str(count)
            count = 1
    result+=string[i-1]+str(count)
print(result)
myfile = open("babu.py","w")
myfile.write(result)
