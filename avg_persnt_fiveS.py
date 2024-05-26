marks=[]
total_mark=0
for i in range(5):
    subject_marks=float(input(f"Enter marks,sub{i+1}:"))
    marks.append(subject_marks)
    total_mark +=subject_marks
print("Avarage number is:",(total_mark/5))
print("Pesentage number:",(total_mark/500)*100)