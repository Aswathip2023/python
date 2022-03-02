name=input("Enter the name ")
name2=name[-3:]
def func(name2):
   if name2=='ing':
       print(name+"ly")
   else: print(name+"ing")
func(name2)