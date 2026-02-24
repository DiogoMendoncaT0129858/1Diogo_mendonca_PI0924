import requests as r

nameFirst = input("Insira o primero nome:\n")
nameLast = input("Insira o ultimo nome:\n")
role = input("O individuo que quer encontrar é Formando ou Formador?:\n")
maxNum = int(input("Insira o numero de ID maximo:\n"))
minNum = int(input("Insira o numero de ID minimo:\n"))
attemps = 0

if (maxNum < minNum):
    print("Numero Maximo nao pode ser menor que o minimo!\n")
    maxNum = int(input("Insira o numero de ID maximo:\n"))
    minNum = int(input("Insira o numero de ID minimo:\n"))

for id in range(minNum, maxNum):
    attemps += 1
    url = r.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771937399276")
    

    if f"Sessão como {role}" in url.text:
        if nameFirst in url.text:
            if nameLast in url.text:
                print(id, "request: ", url.text, "\n")
                print(id, "|-- ENCONTRADO --|\n")
                print("Tentativas: ", attemps)
                break
    else:
        print("Não Encontrado...")
