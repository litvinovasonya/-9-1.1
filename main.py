# main.py - Главный модуль для генерации полного отчета

print("Генератор отчета о подготовке студентов")
print("1. Загрузка данных и анализ зависимостей")

import data_loader # Импортируем первый модуль
# Проверяем, был ли модуль запущен как самостоятельная программа
if hasattr(data_loader, '__name__') and data_loader.__name__ == '__main__':
    pass  # Модуль уже запущен
else:
    # Если модуль был импортирован, вызываем его основную функцию
    from data_loader import participant1_complete_work
    result1 = participant1_complete_work() # вызываем функцию которая возвращает результаты
    print(f"Студентов: {len(result1['students_data'])}")
    print(f"\nУчеба: {result1['dependencies_analysis']['study_effect']['correlation']} ({result1['dependencies_analysis']['study_effect']['interpretation']})")
    print(f"Сон: {result1['dependencies_analysis']['sleep_effect']['correlation']} ({result1['dependencies_analysis']['sleep_effect']['interpretation']})")
    print(f"Посещаемость: {result1['dependencies_analysis']['attendance_effect']['correlation']} ({result1['dependencies_analysis']['attendance_effect']['interpretation']})")


print("2. Поиск лучших и худших студентов")

import top_students #  Импортируем второй модуль
# Проверяем, был ли модуль запущен как самостоятельная программа
if hasattr(top_students, '__name__') and top_students.__name__ == '__main__':
    pass
else:
    # Импортируем и запускаем его основную функцию
    from top_students import participant2_complete_work

    result2 = participant2_complete_work() # вызываем функцию которая возвращает результаты
    # Извлекаем данные о лучших и худших студентах из результата
    top_students_data = result2["top_students"]
    bottom_students_data = result2["bottom_students"]

    print(f"Худших студентов: {len(bottom_students_data)}")

    print(f"Лучшие студенты по баллу:")
    # Выводим список лучших студентов (ID и балл)
    for student in top_students_data:
        print(f"ID {student['ID']} балл {student['Exam_Score']}")

    print(f"\nХудшие студенты по баллу:")
    # Выводим список худших студентов (ID и балл)
    for student in bottom_students_data:
        print(f"ID {student['ID']} балл {student['Exam_Score']}")

print("3. Анализ привычек студентов")
# Импортируем третий модуль
import habits_analysis

# Проверяем, был ли модуль запущен как самостоятельная программа
if hasattr(habits_analysis, '__name__') and habits_analysis.__name__ == '__main__':
    pass  # Модуль уже запущен
else:
    # Импортируем и запускаем его основную функцию
    from habits_analysis import participant3_complete_work
    result3 = participant3_complete_work()
    if 'habits_analysis' in result3:
        # Извлекаем данные анализа привычек
        habits_data = result3['habits_analysis']
        # Создаем DataFrame
        import pandas as pd
        habits_df = pd.DataFrame(habits_data)

        print("Сравнение привычек лучших и худших студентов:")
        # Выводим таблицу сравнения привычек
        print(habits_df.to_string())

print("4. Анализ топ-20 и рекомендации")
# Импортируем четвертый модуль
import recommendations

# Проверяем, был ли модуль запущен как самостоятельная программа
if hasattr(recommendations, '__name__') and recommendations.__name__ == '__main__':
    pass  # Модуль уже запущен
else:
    # Импортируем и запускаем его основную функцию
    from recommendations import participant4_complete_work

    result4 = participant4_complete_work()
    # Получаем отчет по топ-20 из результата
    top_20_report = result4["top_20_analysis"]

    # Выводим результаты
    print("Анализ топ-20 студентов и рекомендации")
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
    print("По посещаемости:")
    for rec in top_20_report['recommendations']['attendance_recommendations']:
        print(f"   • {rec}")
    print("  Дополнительные советы")
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
