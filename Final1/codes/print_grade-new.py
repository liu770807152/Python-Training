def print_grade(mark):
    if mark >= 80:
        print("HD")
    if (mark >= 70) and (mark < 80):
        print("D")
    if 60 <= mark < 70:
        print("Cr")
    if 50 <= mark < 60:
        print("P")
    if mark < 50:
        print("Fail")
