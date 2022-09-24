def gpa(gpa):
    if (gpa>= 4.0):
        return "A"
    elif (gpa >=3.0):
        return "B"
    elif (gpa >= 2.0):
        return "C"
    elif (gpa >=1.0):
        return "D"
    else:
        return "Fail"
    if (gpa > 4.9):
        return "Erooooooooor Your GPA is to high"

print( gpa(5))
