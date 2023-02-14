groupmates = [
    {
        "name": "Александр",
        "surname": "Лозицкий",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Арсений",
        "surname": "Смирнов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Мария",
        "surname": "Шубина",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Иванов",
        "exams": ["Философия", "ЭЭиС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Василий",
        "surname": "Карзанов",
        "exams": ["Философия", "ЭЭиС", "КТП"],
        "marks": [4, 4, 4]
    }
]

avg_mark = None
while not avg_mark:
    try:
        avg_mark = float(input())
    except ValueError:
        print("Некорректные входные параметры")


def filter_students_with_avg_mark(students, avg_mark):
    for student in groupmates:
        if sum(student["marks"]) / len(student["marks"]) > avg_mark:
            print(student["name"], student["surname"])
            subjs_and_marks = zip(student["exams"], student["marks"])
            for sbj, mark in subjs_and_marks:
                print(f"{sbj} - {mark}", end=" ")
            print("\n")
    

filter_students_with_avg_mark(groupmates, avg_mark)
