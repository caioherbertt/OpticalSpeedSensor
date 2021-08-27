import Adafruit_ADS1x15
import time
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
# db.child("Sensor2").child("Medida").push(a)
# a = ['0','0','0','0','0']
a = list(range(0, 10))
COND = 1000


def mm(valor):
    N = 10
    final = 0
    j = 0
   # print("a")
    while N >= 0:
        a.insert(N, valor)
        a.pop(10)
        N = N-1
    # print(a)
    if N == 0:
        N = 10
    while j < 10:
        final += float(a[j])/10
        j += 1
    return final
#    print("Valor medida: ", final)
    if j == 10:
        j = 0
        final = 0
#    time.sleep(1)


ref = list(range(0, 40))


def atualizaRef(valor):
    reffinal = 0
    y = 40
    i = 0
    while y >= 0:
        ref.insert(y, valor)
        ref.pop(40)
        y -= 1
    if y == 0:
        y = 40
    while i < 40:
        reffinal += float(ref[i])/40
        i += 1
#    print("Referencia: ",reffinal)
    return reffinal
    if i == 40:
        i = 0
        reffinal = 0
#    time.sleep(1)


while True:
        relogio = time.clock()
        print(relogio)
#      time.sleep(0.1)
