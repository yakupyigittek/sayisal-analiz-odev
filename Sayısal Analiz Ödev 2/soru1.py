# Sayısal Analiz Ödev 2 Soru 1

x_alt=2
x_ust=4
def f(x):
    return x ** 3 - 2 * (x ** 2) - 5

for x in range(4):
    yeni_kok = (x_alt + x_ust) / 2
    if f(yeni_kok) * f(x_ust) < 0:
        x_alt = yeni_kok
    else:
        x_ust = yeni_kok
    print(x+1,". iterasyon sonucu yeni kök: ",yeni_kok)