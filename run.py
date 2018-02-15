import random

N = 1000

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
                print("miss")
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

    if TimeMax < Tokonobls - Tprihod:
        TimeMax = Tokonobls - Tprihod

    print(i, Tprihod, Tokonobls, buffer, Tbuf,Tokonobls1, sep=' ')


print("Average time of processing - first computer:",AvarageProcessingComp1/N,  "second computer:", AvarageProcessingComp2/N)
print("Average time of waiting:")
print("Chance of standing:")
print("Amount of miss:", MissCheck, "Variaty of miss:", MissCheck/N * 100, "%")