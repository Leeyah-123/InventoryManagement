import sqlite3


def create_db():
    con = sqlite3.connect(database=r'IMS.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee ("
                "'eid' INTEGER NOT NULL,"
                "'name' text NOT NULL,"
                "'email' text  NOT NULL UNIQUE,"
                "'gender' text  NOT NULL,"
                "'contact' text  NOT NULL,"
                "'dob' text,"
                "'doj' text,"
                "'pass' text,"
                "'utype' text,"
                "'address' text,"
                "'salary' text,"
                "PRIMARY KEY('eid' AUTOINCREMENT)"
                ")")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier ("
                "'invoice' INTEGER NOT NULL,"
                "'name' text NOT NULL,"
                "'contact' text  NOT NULL UNIQUE,"
                "'desc' text,"
                "PRIMARY KEY('invoice' AUTOINCREMENT)"
                ")")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category ("
                "'cat_id' INTEGER NOT NULL,"
                "'name' text NOT NULL,"
                "PRIMARY KEY('cat_id' AUTOINCREMENT)"
                ")")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product ("
                "'pid' INTEGER NOT NULL,"
                "'category' text,"
                "'supplier' text,"
                "'name' text,"
                "'price' text,"
                "'qty' text,"
                "'status' text,"
                "PRIMARY KEY('pid' AUTOINCREMENT)"
                ")")
    con.commit()
    con.close()


create_db()
