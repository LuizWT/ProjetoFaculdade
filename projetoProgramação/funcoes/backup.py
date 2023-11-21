from path import LOG_PATH as LOG
from path import RECORD_PATH as RECORD
import shutil
import datetime
import os

def historico(log_msg, resultado=None):
    data = datetime.datetime.now()
    data_format = data.strftime("%d/%m/%Y")
    hora_format = data.strftime("%H:%M:%S")
    
    log = f"{data_format}, {hora_format}, {log_msg}, {resultado}\n"
    
    with open(RECORD, 'a') as arq:
        arq.write(log)

def fazer_backup():
    data = datetime.datetime.now().strftime("%d_%m_%Y")
    pasta = "pasta_backup"

    backup_log = f"{data}_log.txt"
    backup_historico = f"{data}_historico.txt"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    try:
        shutil.copyfile(LOG, os.path.join(pasta, backup_log))
        shutil.copyfile(RECORD, os.path.join(pasta, backup_historico))
    except:
        print('Ocorreu um Erro ao manusear os arquivos!')
    
    print(f"Backup realizado com sucesso!")
    print(f"\n'{backup_log}' e '{backup_historico}' foram salvos em '{pasta}'.")