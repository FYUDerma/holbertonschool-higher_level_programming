import MySQLdb

def list_states(mysql_username="", mysql_password="", database_name=""):
    """List all states from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")


