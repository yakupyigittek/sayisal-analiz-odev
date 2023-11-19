# Sayısal Analiz Ödev 3 Soru 2

e=2.718281828
baslangic=2
def f(x):
    return 4 * e ** (-0.5 * x) - x

def f_turev(x):
    return (-2) * (e ** (-0.5 * x)) - 1

for x in range(4):
    yeni_kok = baslangic - (f(baslangic) / f_turev(baslangic))
    baslangic = yeni_kok
    print(x+1,". iterasyon sonucu yeni kök: ",yeni_kok)
    print("Yeni kökün değeri: ",f(yeni_kok),"\n")