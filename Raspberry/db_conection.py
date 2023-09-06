import MySQLdb

db = MySQLdb.connect('birzyay0v1nhjnvywaun-mysql.services.clever-cloud.com', 'ud03785zpvgrc7vl', '', 'birzyay0v1nhjnvywaun')

cur = db.cursor()
insertions = {}

while True:
    cur.execute("SELECT * FROM Admins_space")

    for row in cur.fetchall():
        print(row[0], row[1], row[3])
        signal = int(input('signal: '))
        inserted_id = 0
        id = row[0]
        availability = row[3]
        if availability == 0 and signal == 1:
            cur.execute(f"UPDATE Admins_space SET availability='1' WHERE id={id}")
            cur.execute(f"INSERT INTO Analytics_ocuppiedspace (occupied_at, unoccupied_at, space_id_id) VALUES (NOW(), NOW(), {id})")
            db.commit()
            inserted_id = cur.lastrowid
            print(f"Se insertó un nuevo registro con ID: {inserted_id}")
            insertions[id] = inserted_id
        elif availability == 1 and signal == 0:
            cur.execute(f"UPDATE Admins_space SET availability='0' WHERE id={id}")
            cur.execute(f"UPDATE Analytics_ocuppiedspace SET unoccupied_at=NOW() WHERE id={insertions[id]}")
            db.commit()
    
# Cerrar la conexión a la base de datos al salir del bucle
db.close()