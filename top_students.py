#файл с поиском лучших и худших студентов

import pandas as pd #импортируем библиотеку для работы с таблицами
from data_loader import participant1_complete_work #берем загрузку данных и анализ зависимостей из первого файла

#находим лучших и худших студентов по итоговому баллу
def get_top_and_bottom_students(students, n=10):
    df = pd.DataFrame(students) #превращаем список в датафрейм
    df_sorted = df.sort_values(by="Exam_Score", ascending=False) #сортируем по баллу по убыванию

    top_students = df_sorted.head(n) #берем первых n студентов
    bottom_students = df_sorted.tail(n).sort_values(by="Exam_Score", ascending=True) #берем последних n студентов и сортируем по возрастанию

    return {
        "top_students": top_students.to_dict("records"), #возвращаем список словарей для удобного использования дальше
        "bottom_students": bottom_students.to_dict("records")
    }

#возвращаем результаты этой части работы в одном словаре для следующего участника
def participant2_complete_work():
    a = participant1_complete_work() #получаем результаты участника один
    students = a["students_data"] #берем список студентов

    top_bottom = get_top_and_bottom_students(students, 10) #находим топ и худших

    return {
        "students_data": students,
        "dependencies_analysis": a["dependencies_analysis"],
        "top_students": top_bottom["top_students"],
        "bottom_students": top_bottom["bottom_students"]
    }

#выводим результаты этой части работы
if __name__ == "__main__":
    a = participant2_complete_work() #запускаем программу работы участника два

    top_students = a["top_students"]
    bottom_students = a["bottom_students"]

    print(f"Худших студентов: {len(bottom_students)}") #выводим размер списка худших

    print(f"\nЛучшие студенты по баллу:") #выводим лучших
    for s in top_students:
        print(f"ID {s['ID']} балл {s['Exam_Score']}") #выводим айди и балл

    print(f"\nХудшие студенты по баллу:") #выводим худших
    for s in bottom_students:
        print(f"ID {s['ID']} балл {s['Exam_Score']}") #выводим айди и балл

