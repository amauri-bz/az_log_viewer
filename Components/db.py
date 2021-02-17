import sqlite3

class Database:

    _instance = None

    def __init__(self):
        #self.conn = sqlite3.connect(':memory:')
        self.conn = sqlite3.connect('project.db')
        self.actual_pos = '0.0'
        self.actual_find = ''
        self.actual_proj = None
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
            pattern TEXT NOT NULL,
            color TEXT
        );
        """)

    def insert_data(self, proj, pattern, color):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO project (proj, pattern, color)
        VALUES (?,?,?)
        """, (proj, pattern, color))
        self.conn.commit()

    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project;
        """)
        for linha in cursor.fetchall():
            print(linha)

    def read_all_patterns(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project WHERE proj = ?
        """, (self.instance().actual_proj,))
        ret = []
        for tupla in cursor.fetchall():
            if tupla[2] != "None":
                ret.append(tupla[2])
        return ret

    def read_all_projects(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project;
        """)
        ret = set()
        ret.add("None")
        for tupla in cursor.fetchall():
            ret.add(tupla[1])
        return ret

    def read_data(self, proj, pattern):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM project WHERE proj = ? AND pattern = ?
        """, (proj, pattern))
        ret = None
        for tupla in cursor.fetchall():
            ret = tupla[3]
        return ret

    def update_data(self, proj, pattern, color):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE project
        SET color = ?
        WHERE proj = ? AND pattern = ?
        """, (color, proj, pattern))
        self.conn.commit()

    def delete_data(self, proj, pattern):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM project
        WHERE proj = ? AND pattern = ?
        """, (proj, pattern))
        self.conn.commit()

    def delete_proj(self, proj):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM project
        WHERE proj = ?
        """, (proj,))
        self.conn.commit()

    def add_item(self, proj, pattern, color):
        self.insert_data(proj, pattern, color)
        if self.instance().actual_proj == "None":
            self.instance().actual_proj = proj

    def get_value(self, pattern):
        return self.read_data(self.instance().actual_proj, pattern)

    def get_keys(self):
        return self.read_all_patterns()

    def get_projects(self):
        return self.read_all_projects()
