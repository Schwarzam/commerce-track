import sqlite3
from tkinter import *
import tkinter as tk
from Database import db_execute, db_get_query


def get_soma_cliente(self):
	query = f"""SELECT quantidade, preco FROM clientes"""
	res = db_get_query(query)

	quantidade = 0
	preco = 0

	for r in res:
		quantidade = quantidade + int(r[0])
		preco = preco + float(r[1])

	label = tk.Label(self, text=f"Quantidade vendida: {quantidade}")
	label.config(font=("Courier", 30))
	label.pack(pady=10, padx=10)

	label = tk.Label(self, text=f"Lucro bruto: R$ {preco}")
	label.config(font=("Courier", 30))
	label.pack(pady=10, padx=10)

	print(quantidade, preco)