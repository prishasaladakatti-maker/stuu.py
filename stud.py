name = input("enter the name")

subject1 = float(input("enter marks  for subject 1:"))
subject2 = float(input("enter marks  for subject 1:"))
subject3 = float(input("enter marks  for subject 1:"))
total_marks = subject1 + subject2 + subject3 
print("student result")
print("studentname:",name)
print("total marks",total_marks)

avg = total_marks/3
print("average",avg)
if(total_marks>35):
    print("pass")
else:
    print("fail")