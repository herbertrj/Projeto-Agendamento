# CORPO DO APLICATO DO FRONT END
from tkinter import *
from tkinter import font, messagebox, ttk

from tkcalendar import Calendar, DateEntry

#importando views
from view import *

######## Cores #########
valor_color0 = "#f0f3f5" # Preta
valor_color1 = "#feffff" # branca
valor_color2 = "#4fa882" # verde
valor_color3 = "#38576b" # valor
valor_color4 = "#403d3d" # letra
valor_color5 = "#606636" # - profit
valor_color6 = "#038cfc" # azul
valor_color7 = "#ef5350" # vermelha
valor_color8 = "#f0f3f5" # + verde
valor_color9 = "#f0f3f5" # sky blue

################# cores ###############

# Janelas 
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=valor_color9)
janela.resizable(width=False, height=False) # bloqueia o tamanho da janeela

frame_cima = Frame(janela, width=310, height=50, bg=valor_color2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=valor_color1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=valor_color1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# LABEL CIMA #####################
app_nome = Label(frame_cima, text="Formulário de Consultoria", anchor=NW, font=('Ivy 13 bold'), bg=valor_color2, fg= valor_color1, relief='flat')
app_nome.place(x=50, y=15)

#funcao inserir
def inserir():
    nome= entrada_nome.get()
    email= entrada_email.get()
    tel = entrada_telefone.get()
    dia = entrada_calendario.get()
    estado = entrada_estado.get()
    assunto = entrada_assunto.get()

    lista = [nome, email, tel, dia, estado,assunto]

    if nome=='':
        messagebox.showerror('Erro','Nome nao pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Dados inseridos com sucesso!')

        entrada_nome.delete(0,'end')
        entrada_email.delete(0,'end')
        entrada_telefone.delete(0,'end')
        entrada_calendario.delete(0,'end')
        entrada_estado.delete(0,'end')
        entrada_assunto.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()
    
    mostrar()


#variavel global tree 
global tree

#funcao atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]
        
        entrada_nome.delete(0,'end')
        entrada_email.delete(0,'end')
        entrada_telefone.delete(0,'end')
        entrada_calendario.delete(0,'end')
        entrada_estado.delete(0,'end')
        entrada_assunto.delete(0,'end')
       
        entrada_nome.insert(0,tree_lista[1])
        entrada_email.insert(0,tree_lista[2])
        entrada_telefone.insert(0,tree_lista[3])
        entrada_calendario.insert(0,tree_lista[4])
        entrada_estado.insert(0,tree_lista[5])
        entrada_assunto.insert(0,tree_lista[6])

        def update():
            nome= entrada_nome.get()
            email= entrada_email.get()
            tel = entrada_telefone.get()
            dia = entrada_calendario.get()
            estado = entrada_estado.get()
            assunto = entrada_assunto.get()

            lista = [nome, email, tel, dia, estado, assunto, valor_id]

            if nome=='':
                messagebox.showerror('Erro','Nome nao pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Dados foram atualizados com sucesso!')

                entrada_nome.delete(0,'end')
                entrada_email.delete(0,'end')
                entrada_telefone.delete(0,'end')
                entrada_calendario.delete(0,'end')
                entrada_estado.delete(0,'end')
                entrada_assunto.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()
            
            mostrar()

        #botão Confirmar
        button_confirmar = Button(frame_baixo, command=update, text="Confirmar", width=10, font=('Ivy 7 bold'), bg=valor_color2, fg= valor_color1, relief='raised' , overrelief='ridge')
        button_confirmar.place(x=110, y=370)

        # update()

    except IndexError:
        messagebox.showerror('Erro', 'selecione um dos dados na tabela')            
        

#funcao deletar 
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso! O dados foram deletas da tabela com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'selecione um dos dados na tabela')     




################## FRAME BAIXO ###############
#NOME
l_nome = Label(frame_baixo, text="Nome *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_nome.place(x=15, y=10)
entrada_nome = Entry(frame_baixo, width=45, justify="left" ,relief='solid')
entrada_nome.place(x=15, y=40)

# EMAIL
l_email = Label(frame_baixo, text="Email *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_email.place(x=15, y=70)
entrada_email = Entry(frame_baixo, width=45, justify="left" ,relief='solid')
entrada_email.place(x=15, y=100)

# Telefone
l_telefone = Label(frame_baixo, text="Telefone *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_telefone.place(x=15, y=130)
entrada_telefone = Entry(frame_baixo, width=45, justify="left" ,relief='solid')
entrada_telefone.place(x=15, y=160)

# Data consulta
l_calendario = Label(frame_baixo, text="Data da Consulta *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_calendario.place(x=15, y=190)
entrada_calendario = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
entrada_calendario.place(x=15, y=220)

# Estado
l_estado = Label(frame_baixo, text="Estado da Consulta *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_estado.place(x=160, y=190)
entrada_estado = Entry(frame_baixo, width=20, justify="left" ,relief='solid')
entrada_estado.place(x=160, y=220)

# Sobre
l_entrada_assunto = Label(frame_baixo, text="Informaçãos extras *", anchor=NW, font=('Ivy 10 bold'), bg=valor_color1, fg= valor_color4, relief='flat')
l_entrada_assunto.place(x=15, y=260)
entrada_assunto = Entry(frame_baixo, width=45, justify="left" ,relief='solid')
entrada_assunto.place(x=15, y=290)


############# BOTAO INSERIR ############
button_inserir = Button(frame_baixo, command=inserir,  text="Inserir", width=10, font=('Ivy 9 bold'), bg=valor_color6, fg= valor_color1, relief='raised' , overrelief='ridge')
button_inserir.place(x=15, y=340)


############# BOTAO ATUALIZAR ############
button_atualizar = Button(frame_baixo,command=atualizar, text="Atualizar", width=10, font=('Ivy 9 bold'), bg=valor_color2, fg= valor_color1, relief='raised' , overrelief='ridge')
button_atualizar.place(x=110, y=340)


############# BOTAO APAGAR ############
button_deletar = Button(frame_baixo,command=deletar, text="Deletar", width=10, font=('Ivy 9 bold'), bg=valor_color7, fg= valor_color1, relief='raised' , overrelief='ridge')
button_deletar.place(x=205, y=340)


####### FRAME DA DIREITA ##############


# lista = [[1,'Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [2,'Fortnato Mpngo', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [3,'Usando Python',  'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [4,'Clinton Berclidio', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [5,'A traicao da Julieta','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']
#            ]

def mostrar():
    global tree

    lista=mostrar_info()

    # lista para cabeçalho
    tabela_head = ['ID', 'Nome', 'email', 'telefone', 'Data', 'Estado', 'Sobre']


    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show='headings')

    # vertical scroll
    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    # vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scroll
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)
    # hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h=[30, 170, 140, 100, 120, 50, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1 

    for item in lista:
        tree.insert('', 'end', values=item)

# chamando funcao mostrar
mostrar()

janela.mainloop()