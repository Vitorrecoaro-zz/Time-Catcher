# Função do Código: Receber valores de hora, data e usuário de logon e logoff.
# Criador: Vitor de Almeida Recoaro.
# Versão: 1.7
# Data: 30/04/2020.
# Novas funcionalidade: Pega o hostname da máquina, cria um arquivo no formato csv, passado um argumento para o programa para fazer o logon ou logoff num mesmo arquivo.
# Mensagem de erro, caso não seja passado argumentos corretos, salva os Logs na memória principal na pasta TimeLogs, um argumento para onde será salvo a pasta TimeLogs
# O caminho do diretório e o argumento de parada será utilizado da seguinte forma "stop*C:\Exemple...\".

import datetime as dt
import os
import socket as sk 
import csv
import sys as sy
if len(sy.argv)!=2:
        input("Invalid Argument\nPress ENTER to exit.")
else:
        arg = str(sy.argv[1])
        firstStar = arg.index("*")
        operation = arg[0:firstStar]
        firstStar += 1
        mode = 1 
        time = dt.datetime.now()            # Recebe as horas atuais do CPU.
        dados = ""                          # Formata os dados de tempo recebido  na exibição brasileira
        dados += time.strftime("%d")        #
        dados += "/"                        #
        dados += time.strftime("%m")        #
        dados += "/"                        #
        dados += time.strftime("%Y")        #
        dados += " "                        #       
        dados += time.strftime("%H")        #
        dados += ":"                        #
        dados += time.strftime("%M")        #
        # dados += '"'                      #
        # dados += time.strftime("%S")      #
        usuario = str(os.getlogin())        # Recebe o usuário que fez login.
        host_name = str(sk.gethostname())   # Recebe o nome do computador que está sendo usado.
        row = [usuario,dados,host_name]
        path = arg[firstStar:]              # Pega o diretório que será guardado o .csv
        if(len(path)==0): 
                if(os.path.isdir("\\TimeLogs")==False): #Testa se a pasta TimeLogs, existe. Caso não, cria a pasta.
                        os.mkdir("\\TimeLogs")
                if(os.path.isfile("\\TimeLogs\\"+usuario+"_Log.csv")==False): #Testa se o arquivo "csv" existe, se não ele será criado com o cabeçalho.
                        mode = 0
                with open("\\TimeLogs\\"+usuario+"_Log.csv",'a', newline='') as file: #Abre o arquivo "csv", caso não exista ele cria e adiciona em linhas abaixo dele.
                        writer = csv.writer(file)
                        if(mode==0):
                                writer.writerow([("User"),("Time"),("Host"),("Event")])
                        if(operation=="start"):
                                row.append("Login")
                                writer.writerow(row)
                        elif(operation=="stop"):
                                row.append("Logout")
                                writer.writerow(row)
        else:
                firstBar = path.index("\\")             # Pega o diretório principal
                mainMemory = str(path[0:firstBar])      #
                if(os.path.isdir(mainMemory)==False):
                        input("Invalid destination of file\nPress ENTER to exit")
                else:
                        if(os.path.isdir(path)==False):
                                os.makedirs(path)         # Cria todas pastas que foram passadas como argumento
                        row = [usuario,dados,host_name] 
                        if(os.path.isdir(path+"\\TimeLogs")==False): #Testa se a pasta TimeLogs, existe. Caso não, cria a pasta.
                                os.mkdir(path+"\\TimeLogs")
                        if(os.path.isfile(path+"\\TimeLogs\\"+usuario+"_Log.csv")==False): #Testa se o arquivo "csv" existe, se não ele será criado com o cabeçalho.
                                mode = 0
                        with open(path+"\\TimeLogs\\"+usuario+"_Log.csv",'a', newline='') as file: #Abre o arquivo "csv", caso não exista ele cria e adiciona em linhas abaixo dele.
                                writer = csv.writer(file)
                                if(mode==0):
                                        writer.writerow([("User"),("Time"),("Host"),("Event")])
                                if(operation=="start"):
                                        row.append("Login")
                                        writer.writerow(row)
                                elif(operation=="stop"):
                                        row.append("Logout")
                                        writer.writerow(row)
