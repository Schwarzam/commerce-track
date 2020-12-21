from tkinter import *
import tkinter as tk
from functions_client import table_rows, db_get_client_records, insert_cliente_values, get_recs, get_next, delete_cliente_value
from functions_startpage import get_soma_cliente

class Client(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Nome da pessoa")
		label.grid(row=2, column=0)
		nome = Entry(master=self)
		nome.grid(row=2, column=2)

		label = tk.Label(self, text="Produto vendido")
		label.grid(row=3, column=0)
		produto = Entry(master=self)
		produto.grid(row=3, column=2)

		label = tk.Label(self, text="Quantidade vendida")
		label.grid(row=4, column=0)
		quantidade = Entry(master=self)
		quantidade.grid(row=4, column=2)

		label = tk.Label(self, text="Data da venda")
		label.grid(row=5, column=0)
		data = Entry(master=self)
		data.grid(row=5, column=2)

		label = tk.Label(self, text="Preco cobrado")
		label.grid(row=6, column=0)
		preco = Entry(master=self)
		preco.grid(row=6, column=2)

		button = tk.Button(self, text="Adicionar venda", command=lambda:insert_cliente_values(nome.get(), produto.get(), quantidade.get(), data.get(), preco.get()))
		button.grid(row=9, column=2, padx=20, pady=20)

		label = tk.Label(self, text="apagar venda ID")
		label.grid(row=5, column=4)
		ids = Entry(master=self)
		ids.grid(row=5, column=5)
		button = tk.Button(self, text="Excluir venda", command=lambda:delete_cliente_value(int(ids.get())))
		button.grid(row=6, column=5)

		button = tk.Button(self, text="Atualizar Pedidos", command=lambda:get_recs(self))
		button.grid(row=12, rowspan = 2, column=2, padx=10, pady=10)

		button = tk.Button(self, text="Proximos 15", command=lambda:get_next(self))
		button.grid(row=12, column=5, padx=10, pady=10)

		table_rows(self)

		button = tk.Button(self, text="Pagina Inicial", command=lambda:controller.show_frame(StartPage))
		button.grid(row=50, column=2, padx=10, pady=10)


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)


		label = tk.Label(self, text="InspiraFlor Board")
		label.config(font=("Courier", 36))
		label.pack(pady=10, padx=10)
		
		get_soma_cliente(self)

		button = tk.Button(self, text="Cliente", command=lambda:controller.show_frame(Client))
		button.pack(padx=10, pady=10)