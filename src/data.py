import cx_Oracle
import src.bin.db_con as db


def execProcess(query="select * from atomiccodes.prestador", method="SELECT"):
    if method == "SELECT":
        try:
            lista = list()
            dsn_tns = cx_Oracle.makedsn(db.db_host, db.db_port, service_name=db.db_schema)
            conn = cx_Oracle.connect(user=db.db_user, password=db.db_pass, dsn=dsn_tns)

            c = conn.cursor()
            c.execute(query)
            for row in c:
                lista.append(row)
                #print(row, '-')

            c.close()
            conn.close()
            return lista
        except Exception as n:
            print(n)
            return False
    elif method == "INSERT":
        try:
            dsn_tns = cx_Oracle.makedsn(db.db_host, db.db_port, service_name=db.db_schema)
            conn = cx_Oracle.connect(user=db.db_user, password=db.db_pass, dsn=dsn_tns)
            conn.autocommit = True

            c = conn.cursor()
            c.execute(query)

            c.close()
            conn.close()
            return True
        except Exception as n:
            print(n)
            return False


def main():
    print("EXECUTA QUERY EM BANCO")


if __name__ == "__main__":
    main()
    execProcess()
