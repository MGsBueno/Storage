# import all modules
# coding: utf8
# import tkinter as tk
import sqlite3
from tkinter import *

conn = sqlite3.connect("/home/coluni/Documents/Almoxarifado/DB/Database.db")
c = conn.cursor()


class dataBase:
    def search(self, *args, **kwargs):
        # search in the DataBase
        sql = "Item"
        result = c.execute(sql, (self.self.form_e.get()), )
        for i in result:
            self.n1 = i[0]  # Name
            self.n1 = i[1]  # Place
            self.n1 = i[2]  # Amount
            self.n1 = i[3]  # Brand
            self.n1 = i[4]  # About
            self.n1 = i[5]  # Register Code
        conn.commit()

        # insert into the entries to show

    def __init__(self, master, *args, **kwargs):
        ##------------------ Search Bar ------------------##
        self.master = master
        self.heading_l = Label(master, text="Busca", fg='white', bg='black')
        self.heading_l.grid(sticky=E + W)
        self.form_e = Entry(master, width=42)
        self.form_e.grid(row=0, column=1, columnspan=3, sticky=N + S)
        self.result_l = Label(root, text="Resultados", bg="black", fg='white')
        self.result_l.grid()
        self.bt = Button(master, text="Pesquisar", command=self.search)
        self.bt.grid(row=0, column=4, sticky=W)
        ##------------------ Search Bar end ------------------##

        ##------------------ Results ------------------##
        self.name_l = Label(master, text="Nome", bg="Gray", fg='white', )
        self.name_l.grid(row=2, column=0, sticky=E + W)
        self.place_l = Label(master, text="Local", bg="Gray", fg='white')
        self.place_l.grid(row=2, column=1, sticky=E + W)
        self.amount_l = Label(master, text="Quantidade", bg="Gray", fg='white')
        self.amount_l.grid(row=2, column=2, sticky=E + W)
        self.brand_l = Label(master, text="Marca", bg="Gray", fg='white')
        self.brand_l.grid(row=2, column=3, sticky=E + W)
        self.about_l = Label(master, text="Descrição", bg="Gray", fg='white')
        self.about_l.grid(row=2, column=4, sticky=E + W, columnspan=2)
        self.code_l = Label(master, text="   Código  ", bg="Gray", fg='white')
        self.code_l.grid(row=2, column=6, sticky=E + W)

        # Dinamic Entry (Do a "For" For catch all entries)
        self.text_name_e = Text(master, height=1, width=15)
        self.text_name_e.grid(row=3, column=0)
        self.text_place_e = Text(master, height=1, width=15)
        self.text_place_e.grid(row=3, column=1)
        self.text_amount_e = Text(master, height=1, width=11)
        self.text_amount_e.grid(row=3, column=2)
        self.text_brand_e = Text(master, height=1, width=15)
        self.text_brand_e.grid(row=3, column=3)
        self.text_about_e = Text(master, height=1, width=29)
        self.text_about_e.grid(row=3, column=4, columnspan=2)
        self.text_code_e = Text(master, height=1, width=8)
        self.text_code_e.grid(row=3, column=6, columnspan=2)
        ##------------------ Results end------------------##


root = Tk()
root["bg"] = "Black"
b = dataBase(root)
root.geometry("1366x768+0+0")
root.title("Controle de Estoque")
root.mainloop()

"""
janela = Tk()
janela.title("Controle de Estoque")
janela["bg"] = "Black" #Altera a cor interior da Janela
#janela["background"] = "Black" #altera a cor externa da Janel EX: barra de  titulo
janela.geometry("800x300+200+200") #"LarguraxAltura+E+T


#janela.Label(janela, text = "Controle de estoque").pack()
janela.mainloop()

"""
