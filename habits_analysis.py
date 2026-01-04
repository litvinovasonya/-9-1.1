#файл с анализом привычек лучших и худших студентов

import pandas as pd #импортируем библиотеку для работы с таблицами
from top_students import participant2_complete_work #берем данные и списки лучших и худших студентов

#сравниваем показатели лучших и худших студентов
def analyze_habits(top_students, bottom_students):
    top_df = pd.DataFrame(top_students) #превращаем список лучших в таблицу
    bottom_df = pd.DataFrame(bottom_students) #превращаем список худших в таблицу

    cols = ["Hours_Studied", "Sleep_Hours", "Attendance", "Exam_Score"] #выбираем показатели для сравнения

    top_means = top_df[cols].mean(numeric_only=True) #считаем средние значения для лучших
    bottom_means = bottom_df[cols].mean(numeric_only=True) #считаем средние значения для худших

    result_df = pd.DataFrame({
        "top_mean": top_means,
        "bottom_mean": bottom_means,
        "difference": top_means - bottom_means
    })

    return result_df

#возвращаем результаты этой части работы в одном словаре для следующего участника
def participant3_complete_work():
    a = participant2_complete_work() #получаем результаты участника два

    top_students = a["top_students"] #берем список лучших
    bottom_students = a["bottom_students"] #берем список худших

    habits_report = analyze_habits(top_students, bottom_students) #сравниваем привычки

    return {
        "students_data": a["students_data"],
        "dependencies_analysis": a["dependencies_analysis"],
        "top_students": top_students,
        "bottom_students": bottom_students,
        "habits_analysis": habits_report.to_dict()
    }

#выводим результаты этой части работы
if __name__ == "__main__":
    a = participant3_complete_work() #запускаем программу работы участника три

    print(f"Студентов: {len(a['students_data'])}") #выводим общее количество студентов
    print(f"Топ студентов: {len(a['top_students'])}") #выводим размер топа
    print(f"Худших студентов: {len(a['bottom_students'])}") #выводим размер худших

    df = pd.DataFrame(a["habits_analysis"]) #превращаем отчет в таблицу
    print("\nСравнение средних значений у лучших и худших студентов:") #выводим заголовок
    print(df.to_string()) #выводим таблицу
