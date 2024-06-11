import numpy as np

histogram_verisi = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42,
    108: 32, 109: 16, 110: 10, 140: 5, 141: 4, 142: 25
}

yoğunluk_degerleri = np.array(list(histogram_verisi.keys()))
piksel_sayilari = np.array(list(histogram_verisi.values()))

T0 = 100
esik = 1

while True:
    G1 = yoğunluk_degerleri[yoğunluk_degerleri > T0]
    G2 = yoğunluk_degerleri[yoğunluk_degerleri <= T0]
    m1 = np.sum(G1 * piksel_sayilari[yoğunluk_degerleri > T0]) / np.sum(piksel_sayilari[yoğunluk_degerleri > T0])
    m2 = np.sum(G2 * piksel_sayilari[yoğunluk_degerleri <= T0]) / np.sum(piksel_sayilari[yoğunluk_degerleri <= T0])

    T1 = (m1 + m2) / 2
    
    if abs(T1 - T0) < esik:
        break
    
    T0 = T1
print(f'Optimal eşik değeri: {T1:.2f}')
  
