import datetime
def historico(logMsg, resultado=None):
    data = datetime.datetime.now()
    dataFormt = data.strftime("%d/%m/%Y")
    horaFormt = data.strftime("%H:%M:%S")
    
    log = f"{dataFormt}, {horaFormt}, {logMsg}, {resultado}\n"
    
    with open('historico.txt', 'a') as arq:
        arq.write(log)