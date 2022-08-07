import mariadb
import sys
import time

def main():
    for i in range(5):
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user="root",
                password="root",
                host="database",
                port=3306,
                database="database"

            )
            print("database connected")

            break
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            if i == 4:
                return
            time.sleep(5)

        
    cur = conn.cursor()
    cur.execute("CREATE TABLE SampleTable (id INT, name VARCHAR(32), PRIMARY KEY (id))")
    cur.execute("INSERT INTO SampleTable (id,name) VALUES (?, ?)", (0 ,'Sample'))
    cur.execute("SELECT id, name FROM SampleTable")
    for id, name in cur:
        print(f"id:{id} name:{name}")

    conn.close()

main()