import sqlite3

#entering in list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#connecting to the sqlite3 database
conn = sqlite3.connect('test.db')


#creating new table as long as it does not already exists, if it does exist, this instruction will be ignored
#it will create the primary key automatically 
#a new column will be created which will hold text data types
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close

conn = sqlite3.connect('test.db')


with conn:
    cur = conn.cursor()
    for filename in fileList:
        if filename.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", \
                   (filename,) )
        conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname FROM tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item)
        print(msg)
