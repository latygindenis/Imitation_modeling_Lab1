import random

taskInput = (1, 13)
taskProc = (1, 18)
a = random.randrange(taskInput[0], taskInput[1], 1)
Tprihod = 0
Tprostoy = 0
Tnachalooblsl = 0
Tojidaniye = 0
Tokonobls = 0

Tokonobls1 = 0
Tojidaniye1 = 0
Tprostoy1 = 0

Tbuf = 0
Tbuf1 = 0
Tbuf2 = 0
buffer = 0
TimeMax = 0
MissCheck = 0
AvarageProcessingComp1 = 0
AvarageProcessingComp2 = 0
N = int(input("Введите количество заявок: "))
for i in range(1, N+1):
    Tprihod = Tprihod + random.randrange(taskInput[0], taskInput[1], 1)
    if Tprihod < Tokonobls:
        if Tprihod < Tbuf:
            buffer += 1
            if buffer == 1:
                Tojidaniye = Tojidaniye + Tokonobls - Tprihod
                Tokonobls = Tokonobls + random.randrange(taskProc[0], taskProc[1], 1)
                Tbuf1 = Tokonobls

            if buffer == 2:
                Tbuf2 = Tbuf1
                Tojidaniye = Tojidaniye + Tokonobls - Tprihod
                Tokonobls = Tokonobls + random.randrange(taskProc[0], taskProc[1], 1)
                Tbuf1 = Tokonobls

            if buffer == 3:
                buffer -= 1
                MissCheck += 1
                continue
        else:
            Tojidaniye = Tojidaniye + Tokonobls - Tprihod
            Tokonobls = Tokonobls + random.randrange(taskProc[0], taskProc[1], 1)
            if buffer == 2:
                Tbuf = Tbuf2
                Tbuf2 = Tbuf1
                Tbuf1 = Tokonobls
            if buffer == 1:
                Tbuf = Tbuf1
                Tbuf1 = Tokonobls
    else:
        Tprostoy = Tprostoy + Tprihod - Tokonobls
        Tokonobls = Tprihod + random.randrange(taskProc[0], taskProc[1], 1)
        buffer = 0
        Tbuf = Tokonobls
    AvarageProcessingComp1 += Tokonobls - Tprihod

    if Tokonobls < Tokonobls1:
        Tojidaniye1 = Tojidaniye1 + Tokonobls1 - Tokonobls
        Tokonobls1 = Tokonobls1 + random.randrange(taskProc[0], taskProc[1], 1)

    else:
        Tprostoy1 = Tprostoy1 + Tokonobls - Tokonobls1
        Tokonobls1 = Tokonobls + random.randrange(taskProc[0], taskProc[1], 1)
    AvarageProcessingComp2 += Tokonobls1 - Tokonobls


    # print(i, Tprihod, Tokonobls, buffer, Tbuf,Tokonobls1, sep=' ')

amountOfSuccessRequest = N - MissCheck
print("Количество заявок:", N)
print( "Среднее время нахождения задания в системе:\n", "  Для обработки на первом компьтере:",'%.3f' % (AvarageProcessingComp1/amountOfSuccessRequest),
      "\n   Для обработки на втором компьтере:", '%.3f' % (AvarageProcessingComp2/amountOfSuccessRequest),
      "\n   В целом в системе:", '%.3f' % ( (AvarageProcessingComp1 + AvarageProcessingComp2)/amountOfSuccessRequest))

print("Среднее время нахождения задания в очереди:",
      "\n   Ожидание в очереди к первому компьютеру:", '%.3f' % (Tojidaniye/amountOfSuccessRequest),
      "\n   Ожидание в очереди ко второму компьютеру:", '%.3f' % (Tojidaniye1/amountOfSuccessRequest),
      "\n   Общее время в очередях:", '%.3f' % ((Tojidaniye + Tojidaniye1)/amountOfSuccessRequest))


print("Вероятность простоя:",
      "\n   Первый компьюnер: "'%.3f' %(Tprostoy/Tokonobls * 100), "% ",
      "\n   Второй компьютер: "'%.3f' %(Tprostoy1/Tokonobls1 * 100), "%")
print("Количество пропущенных заявок:", MissCheck, "\nВероятность упустить заявку:", '%.3f' % (MissCheck/N * 100), "%")