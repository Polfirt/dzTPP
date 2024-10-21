import sqlite3

# Создание/подключение к базе данных
connection = sqlite3.connect('university_database.db')
db_cursor = connection.cursor()

# Создание таблиц
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        faculty TEXT,
        birth_date TEXT
    )
''')

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Instructors (
        instructor_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        department TEXT
    )
''')

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        course_description TEXT,
        instructor_id INTEGER,
        FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
    )
''')

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Exams (
        exam_id INTEGER PRIMARY KEY,
        exam_date TEXT,
        course_id INTEGER,
        max_score INTEGER,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
''')

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        exam_id INTEGER,
        score INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
    )
''')

connection.commit()

# Функции для добавления данных
def add_new_student(first_name, last_name, faculty, birth_date):
    try:
        db_cursor.execute('''
            INSERT INTO Students (first_name, last_name, faculty, birth_date)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, faculty, birth_date))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при добавлении студента: {e}")

def add_new_instructor(first_name, last_name, department):
    try:
        db_cursor.execute('''
            INSERT INTO Instructors (first_name, last_name, department)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, department))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при добавлении препода: {e}")

def add_new_course(course_name, course_description, instructor_id):
    try:
        db_cursor.execute('''
            INSERT INTO Courses (course_name, course_description, instructor_id)
            VALUES (?, ?, ?)
        ''', (course_name, course_description, instructor_id))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при добавлении курса: {e}")

def add_new_exam(exam_date, course_id, max_score):
    try:
        db_cursor.execute('''
            INSERT INTO Exams (exam_date, course_id, max_score)
            VALUES (?, ?, ?)
        ''', (exam_date, course_id, max_score))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при добавлении экзамена: {e}")


def add_new_grade(student_id, exam_id, score):
    try:
        db_cursor.execute('''
            INSERT INTO Grades (student_id, exam_id, score)
            VALUES (?, ?, ?)
        ''', (student_id, exam_id, score))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при добавлении оценки: {e}")

# Функции для обновления данных
def update_student_data(student_id, first_name=None, last_name=None, faculty=None, birth_date=None):
    try:
        update_query = 'UPDATE Students SET'
        params = []
    
        if first_name:
            update_query += ' first_name=?,'
            params.append(first_name)
    
        if last_name:
            update_query += ' last_name=?,'
            params.append(last_name)
    
        if faculty:
            update_query += ' faculty=?,'
            params.append(faculty)
    
        if birth_date:
            update_query += ' birth_date=?,'
            params.append(birth_date)
    
        update_query = update_query.rstrip(',') + ' WHERE student_id=?'
        params.append(student_id)
    
        db_cursor.execute(update_query, tuple(params))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при обновлении данных студента: {e}")

def update_instructor_data(instructor_id, first_name=None, last_name=None, department=None):
    try:
        update_query = 'UPDATE Instructors SET'
        params = []
    
        if first_name:
            update_query += ' first_name=?,'
            params.append(first_name)
    
        if last_name:
            update_query += ' last_name=?,'
            params.append(last_name)
    
        if department:
            update_query += ' department=?,'
            params.append(department)
    
        update_query = update_query.rstrip(',') + ' WHERE instructor_id=?'
        params.append(instructor_id)
    
        db_cursor.execute(update_query, tuple(params))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при обновлении данных препода: {e}")

def update_course_data(course_id, course_name=None, course_description=None, instructor_id=None):
    try:
        update_query = 'UPDATE Courses SET'
        params = []
    
        if course_name:
            update_query += ' course_name=?,'
            params.append(course_name)
    
        if course_description:
            update_query += ' course_description=?,'
            params.append(course_description)
    
        if instructor_id:
            update_query += ' instructor_id=?,'
            params.append(instructor_id)
    
        update_query = update_query.rstrip(',') + ' WHERE course_id=?'
        params.append(course_id)
    
        db_cursor.execute(update_query, tuple(params))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при обновлении данных курса: {e}")

# Функции для удаления данных
def delete_student_data(student_id):
    try:
        db_cursor.execute('DELETE FROM Students WHERE student_id=?', (student_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при удалении студента: {e}")
        

def delete_instructor_data(instructor_id):
    try:
        db_cursor.execute('DELETE FROM Instructors WHERE instructor_id=?', (instructor_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при удалении препода: {e}")

def delete_course_data(course_id):
    try:
        db_cursor.execute('DELETE FROM Courses WHERE course_id=?', (course_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при удалении курса: {e}")

def delete_exam_data(exam_id):
    try:
        db_cursor.execute('DELETE FROM Exams WHERE exam_id=?', (exam_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при удалении экзамена: {e}")

# Функции для выполнения запросов
def fetch_students_by_faculty(faculty):
    try:
        db_cursor.execute('SELECT * FROM Students WHERE faculty=?', (faculty,))
        return db_cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при получении списка: {e}")

def fetch_courses_by_instructor(instructor_id):
    try:
        db_cursor.execute('SELECT * FROM Courses WHERE instructor_id=?', (instructor_id,))
        return db_cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при получении списка: {e}")

def fetch_students_by_course(course_id):
    try:
        db_cursor.execute('''
            SELECT Students.* FROM Students
            JOIN Grades ON Students.student_id = Grades.student_id
            JOIN Exams ON Grades.exam_id = Exams.exam_id
            WHERE Exams.course_id=?
        ''', (course_id,))
        return db_cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при получении списка: {e}")

def fetch_grades_by_course(course_id):
    try:
        db_cursor.execute('''
            SELECT Grades.* FROM Grades
            JOIN Exams ON Grades.exam_id = Exams.exam_id
            WHERE Exams.course_id=?
        ''', (course_id,))
        return db_cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при получении списка: {e}")

def fetch_avg_score_by_course(student_id, course_id):
    try:
        db_cursor.execute('''SELECT AVG(Grades.Score) FROM Grades
                          JOIN Exams ON Grades.ExamID = Exams.ID
                          WHERE Grades.StudentID = ? AND Exams.CourseID = ?''', (student_id, course_id))
        return db_cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при выводе среднего значения по курсу: {e}")

def fetch_avg_score_by_student(student_id):
    try:
        db_cursor.execute('''
            SELECT AVG(score) FROM Grades
            WHERE student_id=?
        ''', (student_id,))
        return db_cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при выводе среднего значения по студенту: {e}")

def fetch_avg_score_by_faculty(faculty):
    try:
        db_cursor.execute('''
            SELECT AVG(Grades.score) FROM Grades
            JOIN Students ON Grades.student_id = Students.student_id
            WHERE Students.faculty=?
        ''', (faculty,))
        return db_cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Произошла ошибка при выводе среднего значения по факультету: {e}")

# Основная функция
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить нового студента")
        print("2. Добавить нового преподавателя")
        print("3. Добавить новый курс")
        print("4. Добавить новый экзамен")
        print("5. Добавить новую оценку")
        print("6. Обновить данные студента")
        print("7. Обновить данные преподавателя")
        print("8. Обновить данные курса")  
        print("9. Удалить студента")
        print("10. Удалить преподавателя")
        print("11. Удалить курс")
        print("12. Удалить экзамен")
        print("13. Получить список студентов по факультету")
        print("14. Получить список курсов по преподавателю")
        print("15. Получить список студентов по курсу")
        print("16. Получить оценки студентов по курсу")
        
        print("17. Получить средний балл студента по курсу")
        print("18. Получить средний балл студента в целом")
        print("19. Получить средний балл по факультету")
        print("0. Выйти")
        
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            faculty = input("Введите факультет: ")
            birth_date = input("Введите дату рождения (гггг-мм-дд): ")
            add_new_student(first_name, last_name, faculty, birth_date)
        
        elif choice == '2':
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            department = input("Введите кафедру: ")
            add_new_instructor(first_name, last_name, department)
        
        elif choice == '3':
            course_name = input("Введите название курса: ")
            course_description = input("Введите описание курса: ")
            instructor_id = int(input("Введите ID преподавателя: "))
            add_new_course(course_name, course_description, instructor_id)
        
        elif choice == '4':
            exam_date = input("Введите дату экзамена (гггг-мм-дд): ")
            course_id = int(input("Введите ID курса: "))
            max_score = int(input("Введите максимальный балл: "))
            add_new_exam(exam_date, course_id, max_score)
        
        elif choice == '5':
            student_id = int(input("Введите ID студента: "))
            exam_id = int(input("Введите ID экзамена: "))
            score = int(input("Введите оценку: "))
            add_new_grade(student_id, exam_id, score)
        
        elif choice == '6':
            student_id = int(input("Введите ID студента: "))
            first_name = input("Введите имя (оставьте пустым для сохранения текущего значения): ")
            last_name = input("Введите фамилию (оставьте пустым для сохранения текущего значения): ")
            faculty = input("Введите факультет (оставьте пустым для сохранения текущего значения): ")
            birth_date = input("Введите дату рождения (оставьте пустым для сохранения текущего значения): ")
            update_student_data(student_id, first_name or None, last_name or None, faculty or None, birth_date or None)

        elif choice == '7':
            instructor_id = int(input("Введите ID преподавателя: "))
            first_name = input("Введите имя (оставьте пустым для сохранения текущего значения): ")
            last_name = input("Введите фамилию (оставьте пустым для сохранения текущего значения): ")
            department = input("Введите кафедру (оставьте пустым для сохранения текущего значения): ")
            update_instructor_data(instructor_id, first_name or None, last_name or None, department or None)

        elif choice == '8':
            course_id = int(input("Введите ID курса: "))
            course_name = input("Введите имя курса (оставьте пустым для сохранения текущего значения): ")
            course_description = input("Введите описание курса (оставьте пустым для сохранения текущего значения): ")
            instructor_id = input("Введите ID препода (оставьте пустым для сохранения текущего значения): ")
            update_course_data(course_id, course_name or None, course_description or None, instructor_id or None)
        
        elif choice == '9':
            student_id = int(input("Введите ID студента: "))
            delete_student_data(student_id)
            
        elif choice == '10':
            instructor_id = input("Введите ID препода: ")
            delete_instructor_data(instructor_id)
            
        elif choice == '11':
            course_id = input("Введите ID курса: ")
            delete_course_data(course_id)
            
        elif choice == '12':
            exam_id = input("Введите ID экзамена: ")
            delete_exam_data(exam_id)
            
        elif choice == '13':
            faculty = input("Введите факультет: ")
            students = fetch_students_by_faculty(faculty)
            for student in students:
                print(student)
        
        elif choice == '14':
            instructor_id = int(input("Введите ID препода: "))
            courses = fetch_courses_by_instructor(instructor_id)
            for course in courses:
                print(course)
        
        elif choice == '15':
            course_id = int(input("Введите ID курса: "))
            students = fetch_students_by_course(course_id)
            for student in students:
                print(student)
        
        elif choice == '16':
            course_id = int(input("Введите ID курса: "))
            grades = fetch_grades_by_course(course_id)
            for grade in grades:
                print(grade)
        
        elif choice == '17':
            course_id = int(input("Введите ID курса: "))
            student_id = int(input("Введите ID студента: "))
            avg_score_bc = fetch_avg_score_by_course(student_id, course_id)
            print(avg_score_bc)

        elif choice == '18':
            student_id = input("Введите ID студента: ")
            avg_grade_bs = fetch_avg_score_by_student(student_id)
            print(avg_grade_bs)

        elif choice == '19':
            faculty = input("Введите факультет: ")
            avg_grade_bf = fetch_avg_score_by_faculty(faculty)
            print(avg_grade_bf)

        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Неккоректынй выбор. Может мискликнул? Если так прям критично, то просто 0 нажми.")

    db_cursor.close()


    if name == "__main__":
        main()

#конец кода)
