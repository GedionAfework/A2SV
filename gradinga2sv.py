grades = 0
def gradingStudents(grades):
    trial = 1
    lists = []
    while trial <= n:
        trial += 1
        grades = int(input(""))
        lists.append(grades)
    for grade in lists:
        if grade < 38:
            print(grade)
        else:
            divide = grade % 5
            if divide >= 3:
                new = 5 - divide
                numb = grade + new
                print(numb)
            else:
                print(grade)
n = int(input(""))
gradingStudents(grades)

