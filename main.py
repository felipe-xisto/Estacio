import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


janela = Tk()


class funcs():
    def limpar(self):
        self.ent_id.delete(0, END)
        self.ent_nome.delete(0, END)
        self.ent_serie.delete(0, END)
        self.ent_turma.delete(0, END)
        self.ent_mae.delete(0, END)
        self.ent_resp.delete(0, END)
        self.ent_valor.delete(0, END)
        self.ent_anoref.delete(0, END)
        self.ent_data.delete(0, END)
        self.cb_ensino.delete(0, END)
        self.cb_turno.delete(0, END)
        self.cb_formapg.delete(0, END)
        self.cb_dependente.delete(0, END)
        self.cb_bolsa.delete(0, END)

    def cadastro(self):
        try:
            Id = self.ent_id.get()
            Nome = self.ent_nome.get()
            Nome = Nome.upper()
            Mae = self.ent_mae.get()
            Mae = Mae.upper()
            Resp = self.ent_resp.get()
            Resp = Resp.upper()
            Serie = self.ent_serie.get()
            Serie = Serie.upper()
            Turma = self.ent_turma.get()
            Turma = Turma.upper()
            Turno = self.cb_turno.get()
            Ensino = self.cb_ensino.get()
            Valor = self.ent_valor.get()
            Valor = Valor.upper()
            Anoref = self.ent_anoref.get()
            Anoref = Anoref.upper()
            Formapg = self.cb_formapg.get()
            Data = self.ent_data.get()
            Data = Data.upper()
            Dependente = self.cb_dependente.get()
            Bolsa = self.cb_bolsa.get()
            conexao = sqlite3.connect("APMC.db")
            cursor = conexao.cursor()
            cursor.execute(
                '''INSERT INTO alunos (Id, Nome, Mae, Resp, Serie, Turma, Turno, Ensino, Valor, Anoref, Formapg, Data, 
                Dependente, Bolsa) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(Id, Nome, Mae, Resp, Serie,
                                                                                     Turma, Turno, Ensino, Valor,
                                                                                     Anoref, Formapg, Data,
                                                                                     Dependente, Bolsa))
            conexao.commit()
            self.listar()
            conexao.close()
        except sqlite3.IntegrityError:
            messagebox.showerror(title="Erro de Identificador", message="Ou Identificador já foi utilizado ou Não foi usado Números")
            conexao.close()

    def listar(self):
        self.pagina.delete(*self.pagina.get_children())
        conexao = sqlite3.connect("APMC.db")
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM alunos')
        lista = cursor.fetchall()
        for lista in lista:
            self.pagina.insert("", END, values=lista)
            conexao.close()

    def alterar(self):
        continuar = messagebox.askokcancel(title="Alterar Cadastro?", message="Você tem certeza que quer alterar esse cadastro?")
        if continuar == True:
            Id = self.ent_id.get()
            Nome = self.ent_nome.get()
            Nome = Nome.upper()
            Mae = self.ent_mae.get()
            Mae = Mae.upper()
            Resp = self.ent_resp.get()
            Resp = Resp.upper()
            Serie = self.ent_serie.get()
            Serie = Serie.upper()
            Turma = self.ent_turma.get()
            Turma = Turma.upper()
            Turno = self.cb_turno.get()
            Ensino = self.cb_ensino.get()
            Valor = self.ent_valor.get()
            Valor = Valor.upper()
            Anoref = self.ent_anoref.get()
            Anoref = Anoref.upper()
            Formapg = self.cb_formapg.get()
            Data = self.ent_data.get()
            Data = Data.upper()
            Dependente = self.cb_dependente.get()
            Bolsa = self.cb_bolsa.get()

            conexao = sqlite3.connect("APMC.db")
            cursor = conexao.cursor()
            cursor.execute(
                '''UPDATE alunos SET Nome=?, Mae=?, Resp=?, Serie=?, Turma=?, Turno=?, Ensino=?, Valor=?, Anoref=?, 
                Formapg=?, Data=?, Dependente=?, Bolsa=? WHERE Id=?''',
                (Nome, Mae, Resp, Serie, Turma, Turno, Ensino, Valor, Anoref, Formapg, Data, Dependente, Bolsa, Id))
            conexao.commit()
            self.listar()
            conexao.close()
        else:
            self.limpar
    def deletar(self):
        continuar = messagebox.askokcancel(title="Deletar Cadastro?", message="Você tem certeza que quer deletar esse cadastro?")

        if continuar == True:
            Id = self.ent_id.get()
            conexao = sqlite3.connect("APMC.db")
            cursor = conexao.cursor()
            cursor.execute('''DELETE FROM alunos WHERE Id=?''', (Id,))
            conexao.commit()
            self.listar()
            conexao.close()
        else:
            pass


    def buscar(self):
        self.pagina.delete(*self.pagina.get_children())
        self.ent_nome.insert(0, "%")
        self.ent_nome.insert(END, "%")
        Name = self.ent_nome.get()
        Name = Name.upper()
        self.limpar()
        conexao = sqlite3.connect("APMC.db")
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM alunos WHERE Nome LIKE ? ''', (Name,) )
        lista = cursor.fetchall()
        for lista in lista:
            self.pagina.insert("", END, values=lista)
            conexao.close()

    def duploclick(self, Event):
        self.limpar()
        self.pagina.selection()
        for n in self.pagina.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = self.pagina.item(n, "values")
            self.ent_id.insert(END, col1)
            self.ent_nome.insert(END, col2)
            self.ent_mae.insert(END, col3)
            self.ent_resp.insert(END, col4)
            self.ent_serie.insert(END, col5)
            self.ent_turma.insert(END, col6)
            self.cb_turno.insert(END, col7)
            self.cb_ensino.insert(END, col8)
            self.ent_valor.insert(END, col9)
            self.ent_anoref.insert(END, col10)
            self.cb_formapg.insert(END, col11)
            self.ent_data.insert(END, col12)
            self.cb_dependente.insert(END, col13)
            self.cb_bolsa.insert(END, col14)

class App(funcs):

    def criar_tabela(self):
        conexao = sqlite3.connect("APMC.db")
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                            Id INTEGER NOT NULL PRIMARY KEY,
                            Nome TEXT NOT NULL,
                            Mae TEXT NOT NULL,
                            Resp TEXT NOT NULL,
                            Serie TEXT NULL,
                            Turma TEXT NULL,
                            Turno TEXT NULL,
                            Ensino TEXT NULL,
                            Valor REAL NOT NULL,
                            Anoref INTEGER NOT NULL,
                            Formapg TEXT NOT NULL,
                            Data TEXT NOT NULL,
                            Dependente TEXT NOT NULL,
                            Bolsa TEXT NOT NULL
                            )''')
        conexao.commit()
        conexao.close()

    def tela(self):
        self.configwin()
        self.widgets()
        self.menus()
        janela.mainloop()

    def configwin(self):
        janela.title("Controle de Pagamentos")
        janela.geometry("720x600")
        janela.configure(background= "#1e3743")
        janela.resizable(True,True)
        janela.minsize(width=720, height=600)

    def widgets(self):

#Frames
        self.frame1=Frame(janela, bd=4, bg="light blue", highlightbackground="midnight blue", highlightthickness= 4)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
        self.frame2 = Frame(janela, bd=4, bg="light blue", highlightbackground="midnight blue", highlightthickness= 4)
        self.frame2.place(relx=0.01, rely=0.53, relwidth=0.98, relheight=0.46)

#Botões
        self.bt_cadastrar=Button(self.frame1,text="Cadastrar", command=self.cadastro)
        self.bt_cadastrar.place(relx=0.15, rely=0.9, relwidth=0.1)

        self.bt_atualizar=Button(self.frame1,text="Alterar", command=self.alterar)
        self.bt_atualizar.place(relx=0.251, rely=0.9, relwidth=0.1)

        self.bt_deletar=Button(self.frame1,text="Deletar", command=self.deletar)
        self.bt_deletar.place(relx=0.351, rely=0.9, relwidth=0.1)

        self.bt_listar=Button(self.frame1,text="Listar Tudo", command=self.listar)
        self.bt_listar.place(relx=0.50, rely=0.9, relwidth=0.1)

        self.bt_buscar=Button(self.frame1, text="Busca P/ Nome", command=self.buscar)
        self.bt_buscar.place(relx=0.60, rely=0.9, relwidth=0.1)

        self.bt_limpar=Button(self.frame1, text="Limpar", command=self.limpar)
        self.bt_limpar.place(relx=0.80, rely=0.1, relwidth=0.1)

#Labels
        self.lb_id=Label(self.frame1, text="Identificador", bg="light blue")
        self.lb_id.place(relx=0.01, rely=0.01)

        self.lb_nome=Label(self.frame1, text="Nome do Aluno", bg="light blue")
        self.lb_nome.place(relx=0.2, rely=0.01)

        self.lb_mae=Label(self.frame1, text="Mãe do Aluno", bg="light blue")
        self.lb_mae.place(relx=0.2, rely=0.15)

        self.lb_resp=Label(self.frame1, text="Responsável pelo Pagamento", bg="light blue")
        self.lb_resp.place(relx=0.2, rely=0.30)

        self.lb_serie=Label(self.frame1, text="Série", bg="light blue")
        self.lb_serie.place(relx=0.01, rely=0.18)

        self.lb_turma=Label(self.frame1, text="Turma", bg="light blue")
        self.lb_turma.place(relx=0.08, rely=0.18)

        self.lb_ensino=Label(self.frame1, text="Ensino", bg="light blue")
        self.lb_ensino.place(relx=0.01, rely=0.32)

        self.lb_turno=Label(self.frame1, text="Turno", bg="light blue")
        self.lb_turno.place(relx=0.01, rely=0.45)

        self.lb_valor=Label(self.frame1, text="Valor R$", bg="light blue")
        self.lb_valor.place(relx=0.2, rely=0.45)

        self.lb_anoref=Label(self.frame1, text="Ano de Referência", bg="light blue")
        self.lb_anoref.place(relx=0.30, rely=0.45)

        self.lb_formapg=Label(self.frame1, text="Forma de Pagamento", bg="light blue")
        self.lb_formapg.place(relx=0.45, rely=0.45)

        self.lb_data=Label(self.frame1, text="Data", bg="light blue")
        self.lb_data.place(relx=0.63, rely=0.45)

        self.lb_dependente=Label(self.frame1, text="Dependente", bg="light blue")
        self.lb_dependente.place(relx=0.01, rely=0.58)

        self.lb_bolsa=Label(self.frame1, text="Benefícios", bg="light blue")
        self.lb_bolsa.place(relx=0.01, rely=0.72)

#Caixas de Texto
        self.ent_id=Entry(self.frame1)
        self.ent_id.place(relx=0.01, rely=0.08, width=60)

        self.ent_nome=Entry(self.frame1)
        self.ent_nome.place(relx=0.2, rely=0.08, relwidth=0.5)

        self.ent_serie=Entry(self.frame1)
        self.ent_serie.place(relx=0.01, rely=0.25, width=20)

        self.ent_turma=Entry(self.frame1)
        self.ent_turma.place(relx=0.08, rely=0.25, width=20)

        self.ent_mae=Entry(self.frame1)
        self.ent_mae.place(relx=0.2, rely=0.23, relwidth=0.5)

        self.ent_resp=Entry(self.frame1)
        self.ent_resp.place(relx=0.2, rely=0.38, relwidth=0.5)

        self.ent_valor=Entry(self.frame1)
        self.ent_valor.place(relx=0.2, rely=0.52, width=60)

        self.ent_anoref=Entry(self.frame1)
        self.ent_anoref.place(relx=0.30, rely=0.52, width=60)

        self.ent_data=Entry(self.frame1)
        self.ent_data.place(relx=0.63, rely=0.52, width=60)

#Comboboxes
        self.cb_ensino=ttk.Combobox(self.frame1, values=("FUNDAMENTAL", "MÉDIO",))
        self.cb_ensino.place(relx=0.01, rely=0.38, relwidth=0.1)

        self.cb_turno=ttk.Combobox(self.frame1, values=("MATUTINO","VESPERTINO"))
        self.cb_turno.place(relx=0.01, rely=0.51, relwidth=0.1)

        self.cb_formapg=ttk.Combobox(self.frame1, values=("DINHEIRO","DÉBITO", "CRÉDITO","PIX"))
        self.cb_formapg.place(relx=0.45, rely=0.52, relwidth=0.1)

        self.cb_dependente=ttk.Combobox(self.frame1, values=("CIVIL","MILITAR"))
        self.cb_dependente.place(relx=0.01, rely=0.64, relwidth=0.1)

        self.cb_bolsa=ttk.Combobox(self.frame1, values=("BENEFICIÁRIO","NÃO POSSUI"))
        self.cb_bolsa.place(relx=0.01, rely=0.78, relwidth=0.1)

#Listagem
        self.pagina=ttk.Treeview (self.frame2, column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13","col14"),selectmode="browse")
        self.pagina.place(relx=0.001, rely=0.01, relwidth=0.95, relheight=0.95)
        self.pagina.heading("#0")
        self.pagina.heading("#1", text="ID")
        self.pagina.heading("#2", text="NOME")
        self.pagina.heading("#3", text="MÃE DO ALUNO")
        self.pagina.heading("#4", text="RESPONSÁVEL")
        self.pagina.heading("#5", text="SÉRIE")
        self.pagina.heading("#6", text="TURMA")
        self.pagina.heading("#7", text="TURNO")
        self.pagina.heading("#8", text="ENSINO")
        self.pagina.heading("#9", text="VALOR")
        self.pagina.heading("#10", text="ANO REFERÊNCIA")
        self.pagina.heading("#11", text="FORMA DE PAGAMENTO")
        self.pagina.heading("#12", text="DATA")
        self.pagina.heading("#13", text="DEPENDENTE")
        self.pagina.heading("#14", text="BENEFÍCIOS")

        self.pagina.column("#0", width=1)
        self.pagina.column("#1", width=10)
        self.pagina.column("#2", width=100)
        self.pagina.column("#3", width=100)
        self.pagina.column("#4", width=100)
        self.pagina.column("#5", width=1)
        self.pagina.column("#6", width=1)
        self.pagina.column("#7", width=1)
        self.pagina.column("#8", width=1)
        self.pagina.column("#9", width=1)
        self.pagina.column("#10", width=1)
        self.pagina.column("#11", width=1)
        self.pagina.column("#12", width=1)
        self.pagina.column("#13", width=1)
        self.pagina.column("#14", width=1)

#Barra de Rolagem
        self.barra=ttk.Scrollbar(self.frame2, orient="vertical", command=self.pagina.yview)
        self.pagina.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.96, rely=0.01, relheight=0.95)
#DuploClick
        self.pagina.bind("<Double-1>", self.duploclick)



    def menus(self):
        def quit(): janela.destroy()
        menubar = Menu(janela)
        janela.config(menu=menubar)
        filemenu = Menu(menubar)

        menubar.add_cascade(label="Opções", menu=filemenu)

        filemenu.add_command(label="Sair", command=quit)



a=App()
a.criar_tabela()
a.tela()