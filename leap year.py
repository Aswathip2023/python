year1 = int(input("Enter current year"))
year2 = int(input("Enter final year"))
print("Leap years are")
for year in (range(year1 , year2)):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)