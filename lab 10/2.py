import psycopg2

conn = psycopg2.connect("dbname=test7 user=artem password=1234")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id SERIAL PRIMARY KEY,
        n VARCHAR(100),
        s INTEGER,
        l INTEGER
    );
""")
conn.commit()

cur.execute("DELETE FROM user;")
cur.execute("INSERT INTO user (n, s, l) VALUES (%s, %s, %s);", ('0', 0, 0))
conn.commit()

print("Здравствуйте, почему то при попытке запустить pygame и SQL в одном коде у меня всё ломалось")
print("так что я решил исправить эту проблему сделав больше backend програмы ")
print("самой игры нет но все функции работают ")
print("если в запросе введёте 1 вместо имени то запуститься сохраниение(пауза) ")
print("если в запросе введёте 2 вместо имени то запуститься смерть змейки(сохраниение результатов) ")

while True:
    n = input("Введите имя: ")

    if n == "1":
        cur.execute("SELECT n, s, l FROM user;")
        u = cur.fetchone()
        cur.execute("INSERT INTO user_score (name, score, level, status) VALUES (%s, %s, %s, %s);", (u[0], u[1], u[2], 0))
        conn.commit()
        break

    elif n == "2":
        cur.execute("SELECT n, s, l FROM user;")
        u = cur.fetchone()
        cur.execute("INSERT INTO user_score (name, score, level, status) VALUES (%s, %s, %s, %s);", (u[0], u[1], u[2], 1))
        conn.commit()
        break

    else:
        cur.execute("SELECT score, level, status FROM user_score WHERE name = %s;", (n,))
        u = cur.fetchone()
        if u:
            if u[2] == 1:
                print(" Пользователь найден, Очки:", u[0], "Уровень:", u[1])
                break
            else:
                print("Пользователь найден, игра продолжается")
                break
        else:
            cur.execute("UPDATE user SET n = %s;", (n,))
            conn.commit()
            break

cur.close()
conn.close()
