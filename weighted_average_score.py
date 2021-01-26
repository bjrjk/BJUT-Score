credit = []
grade = []

while True:
    txt = input("Please input credit and grade, split by space(Press Enter to break):")
    if txt.strip() == '': break
    arr = txt.split()
    credit.append(float(arr[0]))
    grade.append(float(arr[1]))

grade_credit_sum = 0
credit_sum = 0

for i in range(len(credit)):
    grade_credit_sum += credit[i] * grade[i]
    credit_sum += credit[i]

print('Score：%f' % (grade_credit_sum/credit_sum))
