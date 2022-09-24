def gpa1(gpa):
    if (gpa <=0.9):
        return "F"
    elif(gpa <=1.9):
        return "D"
    elif (gpa <=2.9):
        return "C"
    elif (gpa <= 3.9):
        return "B"
    elif (gpa <= 4.9):
        return "A"
    elif (gpa > 4.9):
        return "EROOR YOUR GPA IS TO HIGH."
    
    

print(gpa1(3.5))
