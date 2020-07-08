import mariadb
import dbAccount as db


class InsertDB:
    def __init__(self):
        pass

    def InsertDB(self, DATA, TEMPERATURA, UMIDADE, CO2, TVOC):
        conn = mariadb.connect(
            user=db.user,
            password=db.password,
            host=db.host,
            database=db.database
        )
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO tb_airquality ( DATA_HORA, TEMPERATURA, UMIDADE, CO2, TVOC) VALUES (? , ? , ? , ? , ?)", (DATA, TEMPERATURA, UMIDADE, CO2, TVOC))
        except mariadb.Error as e:
            print(f'Error: {e}')
        conn.commit()
        conn.close()
