import sqlite3

class ragistation:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS contact_list(
            id Integer Primary Key,
            name text,
            email text,
            gender text,
            contact text,
            dob text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()


    # Insert Function
    def insert(self, name, email, gender, contact, dob, address):
        self.cur.execute("insert into contact_list values (NULL,?,?,?,?,?,?)",
                         (name, email, gender, contact, dob, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from contact_list")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from contact_list where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, email, gender, contact, dob, address):
        self.cur.execute(
            "update contact_list set name=?, email=?, gender=?, contact=?, dob=?, address=? where id=?",
            (name, email, gender, contact, dob, address, id))
        self.con.commit()

    #search 
    #def searchdata (self,name):
     #   self.cur.execute("SELECT * from contact_list where name=?",\
      #      (name,))
       ##return rows      
class Database(ragistation):
    pass   