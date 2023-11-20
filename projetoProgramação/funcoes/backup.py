import shutil
import datetime
import os
def historico(logMsg, resultado=None):
    data = datetime.datetime.now()
    dataFormt = data.strftime("%d/%m/%Y")
    horaFormt = data.strftime("%H:%M:%S")
    
    log = f"{dataFormt}, {horaFormt}, {logMsg}, {resultado}\n"
    
    with open('historico.txt', 'a') as arq:
        arq.write(log)

def fazerBackup():
    data = datetime.datetime.now().strftime("%d_%m_%Y")
    pasta = "pastaBackup"

    shutil.copyfile('log.txt', os.path.join(pasta, f"{data}_log.txt"))
    shutil.copyfile('historico.txt', os.path.join(pasta, f"{data}_historico.txt"))
    
    print(f"Backup realizado com sucesso: {data}_log.txt e {data}_historico.txt foram salvos em '{pasta}'")