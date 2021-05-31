str="RESTART"

print("R",end="")
for i in range(1,len(str)):
    if(str[i]=="R"):
        print("$",end="")
    else:
        print(str[i],end="")