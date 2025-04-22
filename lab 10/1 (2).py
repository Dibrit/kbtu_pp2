import psycopg2

conn = psycopg2.connect("dbname=test1 user=artem password=1234")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS pb (
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

ch = input()

if ch == "1":
    n = input("имя")
    p = input("телефона")
    cur.execute("""INSERT INTO pb (n, p) VALUES (%s, %s) ON CONFLICT (p) DO NOTHING; """, (n, p))
    conn.commit()

elif ch == "2":
    p = input("телефон ")
    n = input("новое имя: ")
    p_new = input("новый телефона: ")
    cur.execute("""
        UPDATE pb SET n = %s, p = %s WHERE p = %s;
    """, (n, p_new, p))
    conn.commit()

elif ch == "3":
    fch = input("1 - запрос по имени, 2 - запрос по номеру")
    
    if fch == "1":
        n = input()
        cur.execute("SELECT * FROM pb WHERE n = %s;", (n,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    
    elif fch == "2":
        p = input()
        cur.execute("SELECT * FROM pb WHERE p = %s;", (p,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

elif ch == "4":
    p = input()
    cur.execute("DELETE FROM pb WHERE p = %s;", (p,))
    conn.commit()

cur.close()
conn.close()
