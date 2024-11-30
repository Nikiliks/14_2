import sqlite3

# Открываем соединение с базой данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users, если такая таблица еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Сохранение изменений
connection.commit()

# Вставка данных в таблицу
# for i in range(10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'{i}example1@gmail.com', f'{10 * i}', '1000'))
#
# for i in range(0, 10, 2):
#     cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id = ?', (i + 1,))
# # Сохранение изменений
# connection.commit()
# # Удаляем каждую 3-ю запись (индексы: 0, 1, 2) начиная с 1-й
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
#
# # Сохраняем изменения
# connection.commit()
#
# # Выборка всех записей, где возраст не равен 60
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
# rows = cursor.fetchall()
#
# # Обработка и вывод результата
# for row in rows:
#     username, email, age, balance = row
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute(" DELETE FROM Users WHERE id = ?", (6,)) # Удаление записи с id = 6
cursor.execute( "SELECT COUNT(*) FROM Users")  # общее количество записей
count_user = cursor.fetchone()[0]
# print(count_user)
cursor.execute("SELECT SUM(balance) FROM Users") # сумма всех балансов
sum_balance = cursor.fetchone()[0]
# print(sum_balance)
cursor.execute( "SELECT AVG(balance) FROM Users") # средний баланс всех пользователей
avg_balance = cursor.fetchone()[0]
print(avg_balance)
# Сохраняемся
connection.commit()
# Закрываем соединение с базой данных
connection.close()


