# ask how many semesters have you completed at northeastern 
# for each semester, ask how many courses taken 
# for each course in each semester, ask how many credit hours and what grade you got 
# hold seperate variable for quality points so that adding a new semester is not difficult 
# calculate gpa for completed semesters
# ask if they want to compute their predict gpa 
# ask how many classes they will be taking in the next _ semesters 
# ask how many credit hours, and what grade they want to test 
# add the quality points to the pts stored earlier 
# compute the predicted gpa 
# ask if they want to recompute 
# if not, end loop 
# else, erase stored variables and run the loop again 

GRADE_TO_PTS = {
    "A": 4.000,
    "A-": 3.667,
    "B+": 3.333,
    "B": 3.000,
    "B-": 2.667,
    "C+": 2.333,
    "C": 2.000,
    "C-": 1.667,
    "D+": 1.333,
    "D": 1.000,
    "D-": 0.667,
    "F": 0.000
}

REJECTED_GRADES = set(["S", "U", "X", "I", "L", "W"])

def main():
    quality_pts = 0
    hours = 0 

    completed_sems = int(input("How many semesters have you completed at Northeastern? "))

    for i in range(completed_sems):
        courses = int(input(f"How many classes did you take in semester {i+1}: "))
        print("Enter your courses in order along with the grade you recieved and the course credit hours")

        for _ in range(courses):
            data = input("(Grade c_hours):\n ").split()
      
            grade, c_hours = data[0], data[1]
            c_hours = int(c_hours)
            
            if grade not in REJECTED_GRADES:
                quality_pts += GRADE_TO_PTS[grade] * c_hours 
                hours += c_hours

    gpa = round((quality_pts / hours), 3)
    
    future_quality_pts = 0
    future_quality_pts += quality_pts

    future_hours = 0 
    future_hours += hours 

    calculate_future = input("Do you want to calculate your possible future GPA? (y / n) ").lower()

    if calculate_future == 'y':
        end = False 
        while not end:
            current_sem = int(input("How many classes are you currently taking/ will take in the next semester? "))
            for _ in range(current_sem):
                try:
                    grade, c_hours = input("What grade do you want to calculate for and the class credit hours: \n").split()
                except ValueError:
                    grade, c_hours = input("What grade do you want to calculate for and the class credit hours: \n").split()

                c_hours = int(c_hours)

                if grade not in REJECTED_GRADES:
                    future_quality_pts += GRADE_TO_PTS[grade] * c_hours
                    future_hours += c_hours
            
            f_gpa = round(((quality_pts + future_quality_pts) / (hours + future_hours)))
            print(f"This brings your future GPA to {f_gpa}")
            again = input("Do you wish to recalculate? (y / n) ").lower()
            if again == 'n':
                end = True 
    
    gpa = round((quality_pts / hours), 3)

    return f"Your current GPA is {gpa}. If you achieve the aforementioned grades in your current/next semester, \n your GPA will be {f_gpa}"

if __name__ == '__main__':
    print(main())


