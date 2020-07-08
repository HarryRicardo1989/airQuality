import mariadb
import dbAccount as db


class InsertDB:
    def __init__(self):
        pass

    def InsertDB(self, DATA, TEMPERATURA, UMIDADE):
        conn = mariadb.connect(
            user=db.user,
            password=db.password,
            host=db.host,
            database=db.database
        )
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO tb_airquality ( DATA_HORA, TEMPERATURA, UMIDADE) VALUES (? , ? , ?)", (DATA, TEMPERATURA, UMIDADE))
        except mariadb.Error as e:
            print(f'Error: {e}')
        conn.commit()
        conn.close()
