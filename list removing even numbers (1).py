list = [1,2,3,4,5,46,67,8,9,56,90]
print("List=",list)
for x in list:
    if(x%2)==0:
        list.remove(x)

print("After removing even numbers:", list)