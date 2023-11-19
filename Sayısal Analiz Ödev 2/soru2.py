# Sayısal Analiz Ödev 2 Soru 2

x_alt=1
x_ust=2
def f(x):
    return x ** 3 + 4 * (x ** 2) - 10

for x in range(4):
    yeni_kok = (x_alt + x_ust) / 2
    if f(yeni_kok) * f(x_ust) < 0:
        x_alt = yeni_kok
    else:
        x_ust = yeni_kok
    print(x+1,". iterasyon sonucu yeni kök: ",yeni_kok)