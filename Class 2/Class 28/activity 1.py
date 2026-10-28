student_scores={
    "s1":{"name":"Emily","score":60},
    "s2":{"name":"Bella","score":40},
    "s3":{"name":"John","score":60},
    "s4":{"name":"Anya","score":80},
    "s5":{"name":"Bob","score":50}
}
scores=0
for i in student_scores:
    print("next")
name=input("Please enter the student name:")

finding=student_scores.get(name)
print(finding)