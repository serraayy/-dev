x_verileri = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]

c1 = 16
c2 = 22

def manhattan_uzaklik(x, y):
    return abs(x - y)

for i in range(4):
    küme1_toplam = 0
    küme1_adet = 0
    küme2_toplam = 0
    küme2_adet = 0

    for yaş in x_verileri:
        uzaklik1 = manhattan_uzaklik(yaş, c1)
        uzaklik2 = manhattan_uzaklik(yaş, c2)

        if uzaklik1 < uzaklik2:
            küme1_toplam += yaş
            küme1_adet += 1
        else:
            küme2_toplam += yaş
            küme2_adet += 1

    yeni_c1 = küme1_toplam / küme1_adet if küme1_adet != 0 else c1
    yeni_c2 = küme2_toplam / küme2_adet if küme2_adet != 0 else c2

    print(f"Döngü {i+1}:")
    print("  x  |  c1   |  c2  | Uzaklık 1 | Uzaklık 2 | En Yakın Küme | Yeni Merkez")
    for yaş in x_verileri:
        uzaklik1 = manhattan_uzaklik(yaş, c1)
        uzaklik2 = manhattan_uzaklik(yaş, c2)
        en_yakin_küme = 'Küme 1' if uzaklik1 < uzaklik2 else 'Küme 2'
        yeni_merkez = yeni_c1 if en_yakin_küme == 'Küme 1' else yeni_c2
        print(f"{yaş:^5} | {c1:^8.2f} | {c2:^8.2f} | {uzaklik1:^9.2f} | {uzaklik2:^9.2f} | {en_yakin_küme:^13} | {yeni_merkez:^11.2f}")

    c1, c2 = yeni_c1, yeni_c2
    print('=' * 94)