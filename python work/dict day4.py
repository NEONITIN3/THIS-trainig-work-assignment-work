emp={"Ram" : "devops","age":23,"skill":["java","python","testing"]}
print(type(emp))

print(len(emp))
print(emp.keys())
print(emp.values())
print(emp.items())
print(emp.get("email","not found"))
#inserting new key and values
emp["email"]="ram@gmail.com"
print(emp.items())
#i =key
#j=values
for i,j in emp.items():
    print(i,j)


#second way to creating dict.
emp_list=["raam","harry","john","NEO"]
role_list=["Dev","devops","IThead","Admin"]
project=dict.fromkeys(emp_list,role_list)
print(project)
project=dict.fromkeys(role_list,emp_list)
print(project)

#dict structure
j=0
for i in project.keys():
        project[i]=emp_list[j]
        j+=1
print(project)

#another way to make dict
'''zip function'''
dev=['sam','rak','sdk']
tech=['python','java','databases']
team=dict(zip(dev,tech))
print(team)
#update
d={"manager":"ohm"}
project.update(d)
print(project)

#dict compreh.
'''{1:odd,2:even.....}'''
d={i:"EVEN" if i%2==0 else "odd" for i in range(1,20)}
print(d)

project_lead={i:j for i,j in project.items() if i=="manager" or i=="Admin"}
print(project_lead)

