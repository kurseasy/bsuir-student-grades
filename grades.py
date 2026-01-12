import sqlite3

# подключение к базе
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    group_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

# функции
def add_student(name, group):
    cursor.execute("INSERT INTO students (name, group_name) VALUES (?, ?)", (name, group))
    conn.commit()

def add_grade(student_id, subject, grade):
    cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
    conn.commit()

def list_grades(student_id):
    cursor.execute("SELECT subject, grade FROM grades WHERE student_id=?", (student_id,))
    return cursor.fetchall()

def average_grade(student_id):
    cursor.execute("SELECT AVG(grade) FROM grades WHERE student_id=?", (student_id,))
    return cursor.fetchone()[0]

def list_students():
    cursor.execute("SELECT id, name, group_name FROM students")
    return cursor.fetchall()

# меню
def menu():
    while True:
        print("\nВыберите команду:")
        print("1. Добавить студента")
        print("2. Добавить оценку")
        print("3. Показать все оценки студента")
        print("4. Показать средний балл студента")
        print("5. Показать всех студентов")
        print("6. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            name = input("Имя студента: ")
            group = input("Группа: ")
            add_student(name, group)
            print("✅ Студент добавлен")

        elif choice == "2":
            student_id = int(input("ID студента: "))
            subject = input("Предмет: ")
            grade = int(input("Оценка: "))
            add_grade(student_id, subject, grade)
            print("✅ Оценка добавлена")

        elif choice == "3":
            student_id = int(input("ID студента: "))
            grades = list_grades(student_id)
            print("Оценки:", grades)

        elif choice == "4":
            student_id = int(input("ID студента: "))
            avg = average_grade(student_id)
            print("Средний балл:", avg)

        elif choice == "5":
            students = list_students()
            print("Список студентов:")
            for s in students:
                print(f"ID: {s[0]}, Имя: {s[1]}, Группа: {s[2]}")

        elif choice == "6":
            print("Выход из программы...")
            break

        else:
            print("❌ Неверный номер команды")

if __name__ == "__main__":
    menu()
