import sqlite3

def db_execute(query):
	conn = sqlite3.connect('Database.db')
	cursor = conn.cursor()
	cursor.execute(query)

	try:
		conn.commit()
	except:
		pass

	conn.close()

def db_get_query(query):
	conn = sqlite3.connect('Database.db')
	cursor = conn.cursor()
	cursor.execute(query)

	res = cursor.fetchall()
	conn.close()

	return res




# def connect_or_create():
# 	conn = sqlite3.connect('Database.db')
# 	cursor = conn.cursor()

# 	conn.close()

# def db_execute(query):
# 	conn = sqlite3.connect('Database.db')
# 	cursor = conn.cursor()
# 	cursor.execute(query)

# 	conn.close()


# conn = sqlite3.connect('Database.db')
# cursor = conn.cursor()
# cursor.execute(""" SELECT * FROM clientes """)

# print(cursor.fetchall())

# conn.close()


# db_execute("""CREATE TABLE produtos (
# 		        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 		        nome TEXT NOT NULL,
# 		        estoque INTEGER NOT NULL,
# 		        data REAL NOT NULL,
# 		        custo_producao REAL NOT NULL,
#  		        preco REAL NOT NULL );""")

# db_execute("""DROP TABLE clientes""")

# db_execute("""CREATE TABLE clientes (
# 		        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 		        nome TEXT NOT NULL,
# 		        produto TEXT,
# 		        quantidade INTEGER NOT NULL,
# 		        data VARCHAR NOT NULL,
# 		        preco REAL NOT NULL );""")

