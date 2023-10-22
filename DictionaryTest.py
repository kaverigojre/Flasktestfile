thisdict =	 [ {
  "name": "Ford",
  "age": "21",
  
},
{
  "name": "Ria",
  "age": "31",
 
},

{
  "name": "Dev",
  "age": "41",
 
}

]

age1=None

User_input= input("enter user name =" )

for i in thisdict:
    if i['name']==User_input:
        age1=i
        break

print(age1)
