import os

data_base = []
hora_base = []
descricao_base = []


def inicializar():
    try:
        f = open("dados.txt")
        f.close()
    except:
        with open('dados.txt', 'w') as arquivo:
            arquivo.close()
   
        

def cadastrar():
    data = input("Data: ")
    hora = input("Hora: ")
    descricao = input("Descrição: ")
  
    validacao(data,hora,descricao)

    data_base.append(str(data))
    hora_base.append(str(hora))
    descricao_base.append(str(descricao))


def validacao(data,hora,descricao):
    erros = 0
    if descricao_base == " " or data_base == " " or hora_base == " ":
        print("Campo em branco")
        return menu()
    
    

def listar(lista):
    os.system("clear")
    print("-----Compromissos------")
    for i in range(len(lista)):
        print(i+1,"-",descricao_base[i], data_base[i], hora_base[i])
    print("-----------------------")



def excluir(dat,hor,des):
    listar(dat)
    a = int(input("Qual dado deseja excluir: "))
    a = a-1
    data_base.pop(a)
    hora_base.pop(a)
    descricao_base.pop(a)
    os.system("clear")
    return print("Excluido com sucesso")


def salvar():
    try:
        f = open("data.txt")
        f.close()
    except:
        with open('data.txt', 'w') as arquivo:
            arquivo.close()
        with open('hora.txt', 'w') as arquivo:
            arquivo.close()
        with open('descricao.txt', 'w') as arquivo:
            arquivo.close()
        with open('data.txt', 'w') as arquivo:
            arquivo.close()
            
    data = open('data.txt', 'r')
    linhas = data.readlines()
    data.close()

    data = open('data.txt', 'a')
    hora = open('hora.txt', 'a')
    descricao = open('descricao.txt', 'a')
    print(linhas)
    for i in range(len(data_base)):
        data.write(data_base[i])
        data.write("\n")
        hora.write(hora_base[i])
        hora.write("\n")
        descricao.write(descricao_base[i])
        descricao.write("\n")
    data.close()
    hora.close()
    descricao.close()
    

        
def ler():
    with open("dados.txt",'r') as arquivo:
        for l in arquivo:
            print(l)  

def seletor(selet):
    if selet == 1:
        print("ok")
        cadastrar()
        return menu()
    elif selet == 2:
        listar(data_base)
        return menu()
    elif selet == 3:
        excluir(data_base,hora_base,descricao_base)
        return menu()
    elif selet == 4:
        salvar()
        return menu()
    elif selet == 6:
        ler()
        return menu()
    


def menu():
    inicializar()
    print(f"""
    1 - Cadastar Evento
    2 - Listar Eventos
    3 - Excluir Evento
    4 - Salvar Dados
    5 - Sair
    """)
    selet = int(input("> "))
    os.system("clear")
    seletor(selet)
