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

# пример использования
if __name__ == "__main__":
    add_student("Milana", "FKP-ESIT")
    add_grade(1, "Math", 9)
    add_grade(1, "Physics", 8)
    print("Grades:", list_grades(1))
    print("Average:", average_grade(1))
