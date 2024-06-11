import pandas as pd
import numpy as np

dosya_yolu = r"C:\Users\burka\OneDrive\Masaüstü\soru1_2_data (8).xlsx"
veri = pd.read_excel(dosya_yolu, header=None)

piksel_verisi = veri.values.flatten()

histogram, bin_kenarlari = np.histogram(piksel_verisi, bins=256, range=(0, 256))
kdf = histogram.cumsum()

kdf_min = kdf.min()

kdf_normalize = ((kdf - kdf_min) * 255) / (kdf.max() - kdf_min)
kdf_normalize = np.round(kdf_normalize).astype('int')

esitlenmis_piksel = kdf_normalize[piksel_verisi]

esitlenmis_resim = esitlenmis_piksel.reshape(veri.shape)

esitlenmis_df = pd.DataFrame(esitlenmis_resim)

print(esitlenmis_df)