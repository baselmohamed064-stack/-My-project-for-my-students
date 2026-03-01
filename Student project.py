clas=[
  ["basel","18","(d:60%)"],
  ["anas","15","(d:80)"],
  ["mohamed","16","(d:90)"]
]
print("welcome to student management system")
print("1.add student")
print("2.delete student")
print("3.viwe student and his grade")
print("4.scerch for student")
print("5.viwe grate student")
i=input("enter your choice: ")
if  i=="1":
  name=input("enter your name: ")
  age=input("enter your age: ")
  grade=input("enter your grde:")
  clas.append([name,age,grade])
  print(clas)
elif i=="2":
  name2=input("enter studint name to remove: ")
  for u  in clas:
    if u[0]==name2:
      clas.remove(u)
      print(clas)
      break
    else:
       print("not found")
elif i=="3":
  
  for p in clas:
    print(p[0]+p[2])  
elif i=="4":
  b=input("enter student name: ")
  for r in clas:
     if r[0]==b:
       print(r)
elif i=="5" :
  for y in clas:
     if y[2]>"(d:80)":
        print("the gratest student is: "+y[0]+"his grade is: "+y[2])




     
       
        
  

  
  
