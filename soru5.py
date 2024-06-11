import numpy as np

yogunluk_degerleri = np.array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142])
piksel_sayilari = np.array([12, 18, 32, 48, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25])

toplam_piksel = np.sum(piksel_sayilari)
histogram = piksel_sayilari / toplam_piksel

kumulatif_toplam = np.cumsum(histogram)
kumulatif_ortalama = np.cumsum(histogram * yogunluk_degerleri)

global_ortalama = kumulatif_ortalama[-1]

siniflar_arasi_varyans = ((global_ortalama * kumulatif_toplam - kumulatif_ortalama) ** 2) / (kumulatif_toplam * (1 - kumulatif_toplam))

optimal_esik_indeksi = np.nanargmax(siniflar_arasi_varyans)
optimal_esik_degeri = yogunluk_degerleri[optimal_esik_indeksi]

print("Otsu'nun yöntemi ile optimum eşik değeri:", optimal_esik_degeri)
