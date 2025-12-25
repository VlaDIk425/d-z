math_students = {"Анна", "Борис", "Виктор", "Дарья", "Елена"}
physics_students = {"Виктор", "Георгий", "Дарья", "Иван", "Ксения"}
cs_students = {"Анна", "Виктор", "Елена", "Иван", "Мария"}

all_three = math_students & physics_students & cs_students
print("1. Студенты, которые посещают  три курса:", all_three)

only_math = math_students - physics_students - cs_students
print("2. Студенты, которые посещают только математику:", only_math)

all_unique = math_students | physics_students | cs_students
print("3.Уникальные студенты:", all_unique)

math_physics = (math_students & physics_students) - cs_students

math_cs = (math_students & cs_students) - physics_students

physics_cs = (physics_students & cs_students) - math_students

exactly_two = math_physics | math_cs | physics_cs
print("4. Студенты, которые посещают два курса:", exactly_two)
