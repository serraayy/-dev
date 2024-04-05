import random
import math
import matplotlib.pyplot as plt

def atış_hesaplaması():
    
    hedef_konumu = 20000 + 200 * random.randint(-10, 10)
    genislik_baslangic = hedef_konumu
    genislik_bitis = hedef_konumu + 1000 + 100 * random.randint(-2, 2)
    hedefi_vurdu = False
    hedefin_onune_dustu = None
    
    top_konumu = [0, 19]

    alt_sinir = 330
    ust_sinir = 1800
    hiz = (alt_sinir + ust_sinir) / 2

    atis_sayisi = 0
    atis_sonuclari = []

    while not hedefi_vurdu:
        
        atis_sayisi += 1

        vx = hiz * math.cos(math.radians(30))
        vy = hiz * math.sin(math.radians(30))

       
        t_çıkış = vy / 9.8
        t_iniş = math.sqrt(vy**2 + 2 * 9.8 * 19) / 9.8
        t_air = t_çıkış+ t_iniş
        y_distance = vy * t_iniş

        
        if y_distance < hedef_konumu:
            hedefin_onune_dustu = True
            alt_sinir = hiz
        elif y_distance > hedef_konumu:
            hedefin_onune_dustu = False
            ust_sinir = hiz

        hiz = (alt_sinir + ust_sinir) / 2

        atis_sonuclari.append((atis_sayisi, y_distance))

      
        if abs(y_distance - hedef_konumu) <= 1:
            hedefi_vurdu = True

        print(f"Atış {atis_sayisi}: Top {'önüne' if hedefin_onune_dustu else 'arkasına'} düştü")

    atis_no, y_duzlemi = zip(*atis_sonuclari)
    plt.plot(atis_no, y_duzlemi, marker='o', linestyle='-')
    plt.axhline(y=hedef_konumu, color='r', linestyle='--', label='Hedef Konumu')
    plt.xlabel('Atış Sayısı')
    plt.ylabel('Y Düşey Mesafe (m)')
    plt.title('Atışların Y Düşey Mesafesi')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"Hedef {atis_sayisi}. atışta vuruldu")
    print(f"Son hız: {hiz} m/s")

atış_hesaplaması()