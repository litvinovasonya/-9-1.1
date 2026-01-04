# recommendations.py - Анализ топ-20 студентов и рекомендации
import pandas as pd
from habits_analysis import participant3_complete_work  # берем данные предыдущих участников

# анализ привычек топ-20 студентов
def analyze_top_20_habits(students):
    df = pd.DataFrame(students) # преобразуем список студентов в таблицу

    # сортируем по убыванию балла
    df_sorted = df.sort_values(by="Exam_Score", ascending=False)
    top_20 = df_sorted.head(20) # берем первыъ 20 студентов (топ-20)

    # рассчитываем статистики для топ-20
    stats = {
        "count": len(top_20), # количество студентов
        "min_score": round(top_20["Exam_Score"].min(), 1), # минимальный балл
        "max_score": round(top_20["Exam_Score"].max(), 1), # максимальный балл
        "avg_score": round(top_20["Exam_Score"].mean(), 1), # средний балл

        # статистики по учебе
        "study_stats": {
            "min": round(top_20["Hours_Studied"].min(), 1), # минимум часов учебы
            "max": round(top_20["Hours_Studied"].max(), 1), # максимум часов учебы
            "mean": round(top_20["Hours_Studied"].mean(), 1), # среднее значение
            "median": round(top_20["Hours_Studied"].median(), 1), # медиана
            "std": round(top_20["Hours_Studied"].std(), 1), # стандартное отклонение
            "optimal_range": {
                "lower": round(top_20["Hours_Studied"].quantile(0.25), 1), # 25-й процентиль
                "upper": round(top_20["Hours_Studied"].quantile(0.75), 1) # 75-й процентиль
            }
        },

        # Статистики по сну
        "sleep_stats": {
            "min": round(top_20["Sleep_Hours"].min(), 1), # минимум часов сна
            "max": round(top_20["Sleep_Hours"].max(), 1), # максимум часов сна
            "mean": round(top_20["Sleep_Hours"].mean(), 1),# среднее значение часов сна
            "median": round(top_20["Sleep_Hours"].median(), 1), # медиана
            "std": round(top_20["Sleep_Hours"].std(), 1), # стандартное отклонение
            "optimal_range": {
                "lower": round(top_20["Sleep_Hours"].quantile(0.25), 1), # 25-й процентиль
                "upper": round(top_20["Sleep_Hours"].quantile(0.75), 1) # 75-й процентиль
            }
        },

        # Статистики по посещаемости
        "attendance_stats": {
            "min": round(top_20["Attendance"].min(), 1), # минимальная посещаемость
            "max": round(top_20["Attendance"].max(), 1), # максимальная посещаемость
            "mean": round(top_20["Attendance"].mean(), 1), # среднее значение
            "median": round(top_20["Attendance"].median(), 1), # медиана
            "std": round(top_20["Attendance"].std(), 1), # стандартное отклонение
            "optimal_range": {
                "lower": round(top_20["Attendance"].quantile(0.25), 1), # 25-й процентиль
                "upper": round(top_20["Attendance"].quantile(0.75), 1) # 75-й процентиль
            }
        }
    }

    return stats

# генерация рекомендаций для попадания в топ-20
def generate_top_20_recommendations(top_20_stats):
    # извлекаем статистики для удобства работы
    study = top_20_stats["study_stats"]  # статистика по учебе
    sleep = top_20_stats["sleep_stats"] # статистика по сну
    attendance = top_20_stats["attendance_stats"] # статистика по посещаемости

    recommendations = {
        # общие рекомендации по баллам
        "general_recommendations": [
            f"Для попадания в топ-20 необходимо набрать минимум {top_20_stats['min_score']} баллов",
            f"Средний балл топ-20 студентов: {top_20_stats['avg_score']}"
        ],

        "study_recommendations": [ # Конкретные рекомендации по учебе
            f"Уделяйте учебе от {study['optimal_range']['lower']} до {study['optimal_range']['upper']} часов",
            f"Медианное значение времени учебы у успешных студентов: {study['median']} часов",
            f"Избегайте крайностей: не менее {study['min']}ч и не более {study['max']}ч"
        ],

        "sleep_recommendations": [ # Конкретные рекомендации по сну
            f"Оптимальная продолжительность сна: {sleep['optimal_range']['lower']}-{sleep['optimal_range']['upper']} часов",
            f"Медианное значение сна у успешных студентов: {sleep['median']} часов",
            f"Регулярный сон важен: отклонение не должно превышать {sleep['std']} часов"
        ],

        "attendance_recommendations": [ # Конкретные рекомендации по посещаемости
            f"Посещайте не менее {attendance['optimal_range']['lower']}% занятий",
            f"Медианное значение посещаемости: {attendance['median']}%",
            f"Для уверенного попадания в топ-20 стремитесь к {attendance['optimal_range']['upper']}% посещаемости"
        ],

        "additional_insights": [ # Дополнительные выводы и советы

            "Сбалансированный подход (учеба + сон + посещаемость) эффективнее, чем максимизация одного показателя",
            "Регулярность важнее периодических рывков",
            "Качество времени учебы важнее его количества"
        ]
    }

    return recommendations
# Создаем детализированный отчет по топ-20
def create_detailed_top_20_report(top_20_stats, recommendations):
    # Создаем таблицы для наглядного представления оптимальных диапазонов
    optimal_ranges = pd.DataFrame({
        "Показатель": ["Часы учебы", "Часы сна", "Посещаемость"],
        "Мин. в топ-20": [
            top_20_stats["study_stats"]["min"], # минимальное значение учебы в топ-20
            top_20_stats["sleep_stats"]["min"], # минимальное значение сна в топ-20
            top_20_stats["attendance_stats"]["min"] # минимальная посещаемость в топ-20
        ],
        "Оптимальный минимум": [
            top_20_stats["study_stats"]["optimal_range"]["lower"],# 25-й процентиль учебы
            top_20_stats["sleep_stats"]["optimal_range"]["lower"], # 25-й процентиль сна
            top_20_stats["attendance_stats"]["optimal_range"]["lower"] # 25-й процентиль посещаемости
        ],
        "Медиана": [
            top_20_stats["study_stats"]["median"], # медиана часов учебы
            top_20_stats["sleep_stats"]["median"], # медиана часов сна
            top_20_stats["attendance_stats"]["median"]  # медиана посещаемости
        ],
        "Оптимальный максимум": [
            top_20_stats["study_stats"]["optimal_range"]["upper"], # 75-й процентиль учебы
            top_20_stats["sleep_stats"]["optimal_range"]["upper"], # 75-й процентиль сна
            top_20_stats["attendance_stats"]["optimal_range"]["upper"] # 75-й процентиль посещаемости
        ],
        "Макс. в топ-20": [
            top_20_stats["study_stats"]["max"], # максимальное значение учебы в топ-20
            top_20_stats["sleep_stats"]["max"], # максимальное значение сна в топ-20
            top_20_stats["attendance_stats"]["max"] # максимальная посещаемость в топ-20
        ]
    })

    detailed_report = {
        "summary": { # краткая сводка
            "top_20_min_score": top_20_stats["min_score"],
            "top_20_avg_score": top_20_stats["avg_score"],
            "students_analyzed": top_20_stats["count"]
        },
        "optimal_ranges_table": optimal_ranges,
        "statistical_summary": top_20_stats,
        "recommendations": recommendations
    }

    return detailed_report

# основная функция модуля
def participant4_complete_work():
    # получаем данные от предыдущего участника
    data = participant3_complete_work()

    # анализируем привычки топ-20 студентов
    top_20_stats = analyze_top_20_habits(data["students_data"])

    # генерируем рекомендации
    recommendations = generate_top_20_recommendations(top_20_stats)

    # создаем детализированный отчет
    top_20_report = create_detailed_top_20_report(top_20_stats, recommendations)

    # возвращаем все данные, включая новый анализ
    return {
        "students_data": data["students_data"],
        "dependencies_analysis": data["dependencies_analysis"],
        "top_students": data["top_students"],
        "bottom_students": data["bottom_students"],
        "habits_analysis": data["habits_analysis"],
        "top_20_analysis": top_20_report
    }
# функция для вывода результатов
if __name__ == "__main__":
    print("Анализ топ-20 студентов и рекомендации")
    data = participant4_complete_work() # запускаем основную функцию
    top_20_report = data["top_20_analysis"] # извлекаем отчет по топ-20
    # выводим его
    print("Общая информация о топ-20")
    print(f" минимальный балл в топ-20: {top_20_report['summary']['top_20_min_score']}")
    print(f" средний балл в топ-20: {top_20_report['summary']['top_20_avg_score']}")
    print("Оптимальные диапозоны для попадания в топ-20:")
    print(top_20_report['optimal_ranges_table'].to_string(index=False))
    print("Общие рекомендации:")
    for rec in top_20_report['recommendations']['general_recommendations']:
        print(f"   • {rec}")
    print(" По учебе:")
    for rec in top_20_report['recommendations']['study_recommendations']:
        print(f"   • {rec}")
    print(" По сну:")
    for rec in top_20_report['recommendations']['sleep_recommendations']:
        print(f"   • {rec}")
    print(f"По посещаемости:")
    for rec in top_20_report['recommendations']['attendance_recommendations']:
        print(f"   • {rec}")
    print(f"  Дополнительные советы")
    for insight in top_20_report['recommendations']['additional_insights']:
        print(f"   • {insight}")
    print("Итоговые рекомендации для попадания в топ-20:")
    study_stats = top_20_report['statistical_summary']['study_stats']
    sleep_stats = top_20_report['statistical_summary']['sleep_stats']
    attendance_stats = top_20_report['statistical_summary']['attendance_stats']
    print(f"1. Учеба: {study_stats['optimal_range']['lower']}-{study_stats['optimal_range']['upper']} часов")
    print(f" (идеально: {study_stats['median']} часов)")
    print(f"2. Сон: {sleep_stats['optimal_range']['lower']}-{sleep_stats['optimal_range']['upper']} часов")
    print(f" (идеально: {sleep_stats['median']} часов)")
    print(
        f"3. Посещаемость: {attendance_stats['optimal_range']['lower']}%-{attendance_stats['optimal_range']['upper']}%")
    print(f"(идеально: {attendance_stats['median']}%)")

    print(f"4. Целевой балл: минимум {top_20_report['summary']['top_20_min_score']} баллов")
