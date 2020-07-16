import mariadb
import dbAccount as db


class InsertDB:
    def __init__(self):
        pass

    def InsertDB(self, HOSTNAME, DATA, TEMPERATURA, UMIDADE):
        conn = mariadb.connect(
            user=db.user,
            password=db.password,
            host=db.host,
            database=db.database
        )
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO tb_airquality ( HOSTNAME_PCD, DATA_HORA, TEMPERATURA, UMIDADE) VALUES (? , ? , ?, ?)", (HOSTNAME, DATA, TEMPERATURA, UMIDADE))
        except mariadb.Error as e:
            print(f'Error: {e}')
        conn.commit()
        conn.close()
