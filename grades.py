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
    cursor.execute("SELECT id, subject, grade FROM grades WHERE student_id=?", (student_id,))
    return cursor.fetchall()

def average_grade(student_id):
    cursor.execute("SELECT AVG(grade) FROM grades WHERE student_id=?", (student_id,))
    return cursor.fetchone()[0]

def list_students():
    cursor.execute("SELECT id, name, group_name FROM students")
    return cursor.fetchall()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    cursor.execute("DELETE FROM grades WHERE student_id=?", (student_id,))
    conn.commit()

def delete_grade(grade_id):
    cursor.execute("DELETE FROM grades WHERE id=?", (grade_id,))
    conn.commit()

# меню
def menu():
    while True:
        print("\nВыберите команду:")
        print("1. Добавить студента")
        print("2. Добавить оценку")
        print("3. Показать все оценки студента")
        print("4. Показать средний балл студента")
        print("5. Показать всех студентов")
        print("6. Удалить студента")
        print("7. Удалить оценку")
        print("8. Выход")

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
            print("Оценки:")
            for g in grades:
                print(f"ID оценки: {g[0]}, Предмет: {g[1]}, Оценка: {g[2]}")

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
            student_id = int(input("ID студента для удаления: "))
            delete_student(student_id)
            print("🗑️ Студент и его оценки удалены")

        elif choice == "7":
            grade_id = int(input("ID оценки для удаления: "))
            delete_grade(grade_id)
            print("🗑️ Оценка удалена")

        elif choice == "8":
            print("Выход из программы...")
            break

        else:
            print("❌ Неверный номер команды")

if __name__ == "__main__":
    menu()
