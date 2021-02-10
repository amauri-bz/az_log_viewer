import sqlite3

class Database:

    _instance = None

    def __init__(self):
        #self.conn = sqlite3.connect(':memory:')
        self.conn = sqlite3.connect('project.db')
        self.actual_pos = '0.0'
        self.actual_find = ''
        self.actual_pattern = "None"
        self.create_table()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS project (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            proj TEXT NOT NULL, 
            patern TEXT NOT NULL, 
            color TEXT
        );
        """)

    def insert_data(self, proj, patern, color):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO project (proj, patern, color)
        VALUES (?,?,?)
        """, (proj, patern, color))
        self.conn.commit()

    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project;
        """)
        for linha in cursor.fetchall():
            print(linha)

    def read_all_paterns(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project WHERE proj = ?
        """, (self.instance().actual_pattern,))
        ret = []
        for tupla in cursor.fetchall():
            ret.append(tupla[2])
        return ret

    def read_all_projects(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project;
        """)
        ret = set()
        for tupla in cursor.fetchall():
            ret.add(tupla[1])
        return ret

    def read_data(self, proj, patern):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project WHERE proj = ? AND patern = ?
        """, (proj, patern))
        ret = None
        for tupla in cursor.fetchall():
            ret = tupla[3]
        return ret

    def update_data(self, proj, patern, color):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE project
        SET color = ?
        WHERE proj = ? AND patern = ?
        """, (color, proj, patern))
        self.conn.commit()

    def delete_data(self, proj, patern):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM project
        WHERE proj = ? AND patern = ?
        """, (proj, patern))
        self.conn.commit()

    def add_item(self, proj, patern, color):
        self.insert_data(proj, patern, color)
        if self.instance().actual_pattern == "None":
            self.instance().actual_pattern = proj

    def get_value(self, patern):
        return self.read_data(self.instance().actual_pattern, patern)

    def get_keys(self):
        return self.read_all_paterns()

    def get_projects(self):
        return self.read_all_projects()
