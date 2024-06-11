import pandas as pd
import numpy as np

dosya_yolu = r"C:\Users\burka\OneDrive\Masaüstü\soru3_data (1).xlsx"
veri = pd.read_excel(dosya_yolu, header=None)

gauss_filtresi = np.array([[1, 2, 1],
                           [2, 4, 2],
                           [1, 2, 1]]) / 16

satir_sayisi, sutun_sayisi = veri.shape

cikti = np.zeros((satir_sayisi - 2, sutun_sayisi - 2))

# Gauss filtresini uygula
for i in range(1, satir_sayisi - 1):
    for j in range(1, sutun_sayisi - 1):
        cikti[i - 1, j - 1] = np.sum(veri.iloc[i - 1:i + 2, j - 1:j + 2].values * gauss_filtresi)

cikti_df = pd.DataFrame(cikti)

print(cikti_df)


