"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""

def get_person_short_name(fio: str) -> str:
    family, name, fathername = fio.split()
    return f'{family} {name[0]}. {fathername[0]}.'
print(get_person_short_name("Лермонтов Михаил Юрьевич"))

