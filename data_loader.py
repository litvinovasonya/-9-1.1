#файл с загрузкой данных и анализом зависимостей

import pandas as pd #импортируем библиотеку для работы с таблицами

#загружаем данные и создаем список с нужными показателями
def load_student_data(): #функция для загрузки данных из файла
    file_name = "StudentPerformanceFactors.csv" #датасет уже в этой же папки, поэтому путь к нему - его имя
    df = pd.read_csv(file_name) #загружаем данные
    students = [] #создаем список, чтобы сохранять данные о студентах

    num_rows = len(df) #находим количество строк в таблице
    for i in range(num_rows):
        row = df.iloc[i] #проходимся по каждой строке, присваивая ей номер i

        student = {
            "ID": i + 1, #айди
            "Hours_Studied": row["Hours_Studied"], #часы, потраченные на учебу
            "Sleep_Hours": row["Sleep_Hours"], #часы, потраченные на сон
            "Attendance": row["Attendance"], #процент посещаемости
            "Exam_Score": row["Exam_Score"] #итоговый балл на экзамене
        }
        #создаем список студентов: айди создаем сами, используя номер ряда + 1 (первый айди = 1)
        #остальные данные берем из таблицы
        students.append(student) #добавляем студента в список
    return students

#анализируем зависимости итоговой оценки и других показателей
def analyze_dependencies(students):
    df = pd.DataFrame(students) #превращаем список в датафрейм (таблицу)
    corr_study = df["Hours_Studied"].corr(df["Exam_Score"]) #рассчитываем корреляцию между часами учебы и баллом
    corr_sleep = df["Sleep_Hours"].corr(df["Exam_Score"]) #рассчитываем корреляцию между часами сна и баллом
    corr_attendance = df["Attendance"].corr(df["Exam_Score"]) #рассчитываем корреляцию между посещаемостью и баллом

#корреляция - это число от -1 до 1, показывающее степень взаимосвязанности показателей, будем использовать этот показатель для составления отчета о зависимостях
#1 - идеальная прямая зависимость (чем больше X, тем больше Y)
#0 - нет зависимости
#-1 - идеальная обратная зависимость (чем больше X, тем меньше Y)

#в реальных данных редко встречаются "идеальные" показатели, поэтому присвоим следующие значения:
    def analysis(corr_value):
        if corr_value > 0.5:
            return "сильная прямая зависимость"
        elif corr_value > 0.2:
            return "умеренная прямая зависимость"
        elif corr_value < -0.5:
            return "сильная обратная зависимость"
        elif corr_value < -0.2:
            return "умеренная обратная зависимость"
        else:
            return "слабая зависимость"

#создаем отчет с полученными зависимостями
#каждую корреляцию округляем до тысячных для более структурированного анализа
#на основе полученного числа выдаем показатель, выраженный словами
    dependencies_report = {
        "study_effect": {
            "correlation": round(corr_study, 3),
            "interpretation": analysis(corr_study)
        },
        "sleep_effect": {
            "correlation": round(corr_sleep, 3),
            "interpretation": analysis(corr_sleep)
        },
        "attendance_effect": {
            "correlation": round(corr_attendance, 3),
            "interpretation": analysis(corr_attendance)
        }
    }

    return dependencies_report

#возвращаем результаты всей работы в одном словаре для следующего участника
def participant1_complete_work():
    students = load_student_data()
    dependencies = analyze_dependencies(students)

    return {
        'students_data': students,
        'dependencies_analysis': dependencies
    }

#выводим результаты этой части работы
#корреляцию выражаем в числовом и текстовом виде
if __name__ == "__main__":
    a = participant1_complete_work() #запускаем программу работы участника 1

    print(f"Студентов: {len(a['students_data'])}") #выводим общее количество студентов
    print(f"\nУчеба: {a['dependencies_analysis']['study_effect']['correlation']} ({a['dependencies_analysis']['study_effect']['interpretation']})") #зависимость между часами учебы и итоговым баллом
    print(f"Сон: {a['dependencies_analysis']['sleep_effect']['correlation']} ({a['dependencies_analysis']['sleep_effect']['interpretation']})") #зависимость между часами сна и итоговым баллом
    print(f"Посещаемость: {a['dependencies_analysis']['attendance_effect']['correlation']} ({a['dependencies_analysis']['attendance_effect']['interpretation']})") #зависимость между посещаемостью и итоговым баллом