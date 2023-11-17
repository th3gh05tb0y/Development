#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan - Version 1.0 (alfa)
# Develompent: gh05tb0y
# contact: th3_gh05tb0y@proton.me

import socket
import sys
import subprocess
from datetime import datetime

# Caminho do pathfile
pathfile = './utils'
if pathfile not in sys.path:
    sys.path.append(pathfile)

from banner import *

# Limpar a tela ao executar a aplicação
subprocess.call('clear', shell=True)

# Caso o usuário não informe nenhum parâmetro
if len(sys.argv) != 4:
    print('\n [!] ERROR: Missing input arguments.')
    print('\n [!] Usage: ./pytcpscan.py <target> <initial port> <final port>')
    sys.exit(1)

# Caso o usuário informe os dados corretamente
# Cria o socket de conexão para testar as portas
def connect(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    try:
        s.connect((target, port))
        return(1)
    except:
        return(2)

# Variáveis que serão tratadas no processo de 
# análise das portas abertas.
target = str(sys.argv[1])
init_port = int(sys.argv[2])
end_port = int(sys.argv[3])
host = socket.gethostbyname(target) # Responsável por converter host em ip

# Inicia a varredura levando em consideração o 
# range de portas informadas nos parâmetros

print(' [*] Connecting to target: %s\n' + 
      ' [*] Scanning ports between %s and %s\n' +  
      ' [*] Please wait...' % (target, init_port, end_port))
print('-' * 50)
print(' [!] Scanning remote host', host)
print(' [!] This may take a while, be patient.')
print('-' * 50)

# Registrando o momento que a varredura iniciou
t1 = datetime.now()

# Laço que testa as portas dentro do range
try:
    for port in range(init_port, end_port + 1):
        e = connect(target, port)
        if e == 1:
            print(' [+] POSITIVE to port {}: \t Status: OPEN'.format(port))
        
# Se control+c for pressionado, encerra a aplicação.
except KeyboardInterrupt:
    print('\n\n [?] You pressed Control+C' +
          '\n [!] The application has been stopped prematurely.')
    sys.exit()

# Se o host alvo não pôde ser resolvido
except socket.gaierror:
    print(' [!] Hostname could not be resolved. Exiting!')
    sys.exit()

# Se for impossível conectar ao alvo.
except socket.error:
    print('Implssible to connect to target!')
    sys.exit()

# Se tudo correr bem, registrar o termino da varredura
t2 = datetime.now()
totalTime = t2 - t1

print('-' * 50)
print ('\n [!] Scanning Completed in: ', totalTime)
print('-' * 50)
print('\n --- FINISHED --- \n')
