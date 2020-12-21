import sqlite3
from tkinter import *
import tkinter as tk
from Database import db_execute, db_get_query

def db_get_client_counts():
	res = db_get_query(f"""SELECT COUNT(*) FROM clientes""")

	return int(res[0][0])

def db_get_client_records(num=0):
	res = db_get_query(f"""SELECT * FROM clientes ORDER BY id DESC LIMIT 15 OFFSET {num}""")

	resdict = {}
	resdict["id"] = []
	resdict["name"] = []
	resdict["produto"] = []
	resdict["quantidade"] = []
	resdict["data"] = []
	resdict["preco"] = []

	for r in res:
		resdict["id"].append(r[0])
		resdict["name"].append(r[1])
		resdict["produto"].append(r[2])
		resdict["quantidade"].append(r[3])
		resdict["data"].append(r[4])
		resdict["preco"].append(r[5])

	return resdict

count = 0

def get_next(self):	
	num_recs = db_get_client_counts()

	for label in self.grid_slaves():
		if int(label.grid_info()["row"]) > 16 and int(label.grid_info()["row"]) < 34:
			label.grid_forget()

	global count
	if (count + 15) <= num_recs:
		count = (count + 15)
	else:
		count = count

	get_recs(self, counts=count)

def get_recs(self, counts=None):
	if counts == None:
		count = 0
		recs = db_get_client_records(count)

	else:
		count = counts
		recs = db_get_client_records(count)

	row = 17
	if len(recs) > 0:
		for rec in range(len(recs['name'])):
			label = tk.Label(self, text=f"{recs['id'][rec]}")
			label.grid(row=row, column=0)

			label = tk.Label(self, text=f"{recs['name'][rec]}")
			label.grid(row=row, column=1)

			label = tk.Label(self, text=f"{recs['produto'][rec]}")
			label.grid(row=row, column=2)

			label = tk.Label(self, text=f"{recs['quantidade'][rec]}")
			label.grid(row=row, column=3)

			label = tk.Label(self, text=f"{recs['data'][rec]}")
			label.grid(row=row, column=4)

			label = tk.Label(self, text=f"R$ {recs['preco'][rec]}")
			label.grid(row=row, column=5)

			row = row + 1

def table_rows(self):
	row = 15
	label = tk.Label(self, text=f"ID")
	label.grid(row=row, column=0)

	label = tk.Label(self, text=f"Nome")
	label.grid(row=row, column=1)

	label = tk.Label(self, text=f"Produto")
	label.grid(row=row, column=2)

	label = tk.Label(self, text=f"Quantidade")
	label.grid(row=row, column=3)

	label = tk.Label(self, text=f"Data")
	label.grid(row=row, column=4)

	label = tk.Label(self, text=f"Preco")
	label.grid(row=row, column=5)


def insert_cliente_values(name, produto, quantidade, data, preco):
	query = f"""INSERT INTO clientes (nome, produto, quantidade, data, preco) VALUES ('{name}', '{produto}', {quantidade}, '{data}', {preco});"""
	
	db_execute(query)

def delete_cliente_value(ids):
	print(ids)
	query = f"""DELETE FROM clientes WHERE id = {ids};"""
	
	db_execute(query)

