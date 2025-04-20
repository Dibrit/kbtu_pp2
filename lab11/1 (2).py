import psycopg2

conn = psycopg2.connect("dbname=test8 user=artem password=1234")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE pb (
        id SERIAL PRIMARY KEY,
        n VARCHAR(200),
        p VARCHAR(15) UNIQUE
    );
""")
conn.commit()

print("1. Ввести данные вручную")
print("2. Обновить данные")
print("3. Запросить данные")
print("4. Удалить данные")
print("5. Запросить всех пользователей")
print("6. Добавить несколько пользователей")

ch = input()

if ch == "1":
    n = input("Имя: ")
    p = input("Телефон: ")
    cur.execute("""INSERT INTO pb (n, p) VALUES (%s, %s);""", (n, p))
    conn.commit()

elif ch == "2":
    p = input("Старый телефон: ")
    n = input("Новое имя: ")
    p_new = input("Новый телефон: ")
    cur.execute("""UPDATE pb SET n = %s, p = %s WHERE p = %s;""", (n, p_new, p))
    conn.commit()

elif ch == "3":
    fch = input("1 - запрос по имени, 2 - запрос по номеру: ")
    
    if fch == "1":
        n = input("Имя: ")
        cur.execute("SELECT * FROM pb WHERE n = %s;", (n,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    
    elif fch == "2":
        p = input("Телефон: ")
        cur.execute("SELECT * FROM pb WHERE p = %s;", (p,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

elif ch == "4":
    fch = input("1 - удаление по имени, 2 - удаление по номеру: ")
    if fch == "1":
        n = input("Имя: ")
        cur.execute("DELETE FROM pb WHERE n = %s;", (n,))
        conn.commit()
    elif fch == "2":
        p = input("Телефон: ")
        cur.execute("DELETE FROM pb WHERE p = %s;", (p,))
        conn.commit()

elif ch == "5":
    cur.execute("SELECT * FROM pb;")
    b = cur.fetchall()
    for i in b:
        print("Имя:", i[1], ", Телефон:", i[2])

elif ch == "6":
    h = int(input("Сколько пользователей вы хотите добавить? "))
    for j in range(h):
        n = input("Имя: ")
        p = input("Телефон: ")
        cur.execute("""INSERT INTO pb (n, p) VALUES (%s, %s);""", (n, p))
        conn.commit()

cur.close()
conn.close()
