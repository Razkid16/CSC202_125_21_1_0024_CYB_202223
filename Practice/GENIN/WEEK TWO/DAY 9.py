# just f-ing around
student_scores = {
    "Peace": 81,
    "Douggy": 95,
    "Faceless": 91,
    "Idan": 74,
    "Ralph": 88,
    "Sule": 73
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)
print(student_scores)






#dictionary inside dictionary
#nexted dictionary

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris","Lille","Dijon"], 
        "Total_visited": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "Total_visited": 10
    },
]

print(travel_log)