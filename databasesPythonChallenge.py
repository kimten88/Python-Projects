
import sqlite3



def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = sqlite3.connect(':memory:')
    

    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_roster( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_Name TEXT, \
                    col_Species TEXT, \
                    col_IQ TEXT \
                    );")
    conn.commit()
    conn.close()


def data_entry():
    conn = sqlite3.connect(':memory:')
    data = ('Jean-Baptiste Zorg','Human','122'), ('Korben Dallas','Meat Popsicle','100'),('Ak\'not','Mangalore','-5')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_roster (col_Name,col_Species,col_IQ) VALUES (?,?,?)""")
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_roster""")
    count = cur.fetchone()[0]
    return cur,count




  












if __name__ == '__main__':
    create_connection()
    data_entry()
    count_records()
    print(tbl_roster)
