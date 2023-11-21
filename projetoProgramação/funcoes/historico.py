from path import RECORD_PATH as RECORD
import datetime

def historico(log_msg, resultado=None):
    data = datetime.datetime.now()
    data_fmt = data.strftime("%d/%m/%Y")
    hora_fmt = data.strftime("%H:%M:%S")
    
    log = f"{data_fmt}, {hora_fmt}, {log_msg}, {resultado}\n"
    
    with open(RECORD, 'a') as arq:
        arq.write(log)