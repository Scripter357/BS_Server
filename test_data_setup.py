import sys
import os
import psycopg2

print("Inputting test data...")
print("Connecting to database...")
conn = psycopg2.connect(database="server_db", user="postgres", password="postgres", host="localhost", port="5432")
cursor = conn.cursor()
conn.autocommit = True

cursor.execute("""
INSERT INTO areas VALUES
  (1, 'северный'),
  (2, 'южный'),
  (3, 'западный'),
  (4, 'восточный')
""")

cursor.execute("""
INSERT INTO salons VALUES
  (1, 1, 'Красопета'),
  (2, 1, 'Худые ножки'),
  (3, 1, 'Большая ляшка'),
  (4, 2, 'Круглый персик'),
  (5, 5, 'Ешкин кот')
""")

cursor.execute("""
INSERT INTO services VALUES
  (1, 'Мелирование', 1500),
  (2, 'Наращивание волос', 6500),
  (3, 'Маникюр', 1800),
  (4, 'Педикюр', 2100),
  (5, 'Эпиляция', 3400),
  (6, 'Массаж', 3600),
  (7, 'Ламинирование бровей', 900),
  (8, 'Татуировка', 7000)
""")

cursor.execute("""
INSERT INTO positions VALUES
  (1, 'Стилист', 35000),
  (2, 'Мастер маникюра', 25000),
  (3, 'Мастер эпиляции', 26000),
  (4, 'Массажист', 37000),
  (5, 'Бровист', 15000),
  (6, 'Татуировщик', 44000)
""")

cursor.execute("""
INSERT INTO employees VALUES
  (1, 'Боброва', 'Эдилия', 'Леонидовна'),
  (2, 'Овчинникова', 'Мэри', 'Всеволодовна'),
  (3, 'Филатова', 'Анастасия', 'Созонова'),
  (4, 'Харитонова', 'Милолика', 'Макаровна'),
  (5, 'Блохин', 'Панкратий', 'Платонович')
""")

cursor.execute("""
INSERT INTO clients VALUES
  (1, 'Агафонова', 'Фая', 'Вениаминовна'),
  (2, 'Борисова', 'Инара', 'Николаевна'),
  (3, 'Ковалева', 'Агнесса', 'Иринеевна')
""")

cursor.execute("""
INSERT INTO salon_service VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (1, 4),
  (1, 7),
  (2, 3),
  (2, 4),
  (2, 5),
  (2, 6),
  (3, 1),
  (3, 2),
  (3, 5),
  (4, 6),
  (4, 7),
  (4, 8),
  (5, 5),
  (5, 6)
""")

cursor.execute("""
INSERT INTO employee_position VALUES
  (1, 1),
  (1, 2),
  (1, 5),
  (2, 3),
  (2, 4),
  (3, 6),
  (4, 1),
  (5, 4),
  (5, 6)
""")

cursor.execute("""
INSERT INTO orders VALUES
  (1, 1, 1, 9800),
  (2, 1, 2, 4800)
""")

cursor.execute("""
INSERT INTO order_details VALUES
  (1, 1, 1, 1, 1500),
  (1, 2, 1, 1, 6500),
  (1, 3, 1, 1, 1800),
  (2, 3, 4, 1, 1800),
  (2, 4, 4, 1, 2100),
  (2, 7, 1, 1, 900)
""")

print("")

print("Closing connection...")
conn.close()
