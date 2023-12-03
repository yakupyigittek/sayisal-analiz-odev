#Sayısal Analiz Taylor Serisi Ödevi
#Yakup Yiğit Tek - 02220224011
#05.11.2023

pi=3.141592653             #Pi sayısını atama
gercekDeger=0.809016994    #Cos(π/5)'in gerçek değerini atama

print("Gerçek cos(π/5) değeri:", gercekDeger)

x=pi/5

tekTerimliTaylor=((-1)**0)*(x**(2*0))/1 #Burada "/1" ifadesi "0!"i temsil etmektedir.
ikiTerimliTaylor=tekTerimliTaylor+((-1)**1)*(x**(2*1))/2

print("Tek terimli Taylor değeri:",tekTerimliTaylor)
print("İki terimli Taylor değeri:",ikiTerimliTaylor)

tekTerimliKesmeHatasi=gercekDeger-tekTerimliTaylor
ikiTerimliKesmeHatasi=gercekDeger-ikiTerimliTaylor

print("Tek terimli kesme hatası:",tekTerimliKesmeHatasi)
print("İki terimli kesme hatası:",ikiTerimliKesmeHatasi)