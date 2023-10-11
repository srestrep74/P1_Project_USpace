import MySQLdb
import os
import environ
import RPi.GPIO as IO

env = environ.Env()
environ.Env.read_env()

db = MySQLdb.connect(env('DB_HOST'), env('DB_USER'), env('DB_PASSWORD'), env('DB_NAME'))
SW1 = 19
SW2 = 21
cur = db.cursor()
insertions = {}
pines = {1: SW1, 5: SW2}

IO.setmode(IO.BOARD)
IO.setup(SW1, IO.IN)
IO.setup(SW2, IO.IN)

while True:
    cur.execute("SELECT * FROM Admins_space")
    for row in cur.fetchall():
        print(row[0], row[1], row[3])
        inserted_id = 0
        signal = 0
        id = row[0]
        print(signal)
        availability = row[3]
        if id in pines:
            signal = IO.input(pines[id])
            if availability == 0 and signal == 1:
                cur.execute(f"UPDATE Admins_space SET availability='1' WHERE id={id}")
                cur.execute(f"UPDATE Admins_space SET occupancy=max_occupancy WHERE id={id}")
                cur.execute(f"INSERT INTO Analytics_ocuppiedspace (occupied_at, unoccupied_at, space_id_id) VALUES (NOW(), NOW(), {id})")
                db.commit()
                inserted_id = cur.lastrowid
                print(f"Se insertó un nuevo registro con ID: {inserted_id}")
                insertions[id] = inserted_id
            elif availability == 1 and signal == 0:
                cur.execute(f"UPDATE Admins_space SET availability='0' WHERE id={id}")
                cur.execute(f"UPDATE Analytics_ocuppiedspace SET unoccupied_at=NOW() WHERE id={insertions[id]}")
                cur.execute(f"UPDATE Admins_space SET occupancy=0 WHERE id={id}")
                db.commit()

db.close()