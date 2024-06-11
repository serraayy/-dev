import pandas as pd
import numpy as np

excel_file = r"C:\Users\burka\OneDrive\Masaüstü\soru1_2_data (8).xlsx"

df = pd.read_excel(excel_file)

data = df.values

min_pixel_value = np.min(data)
max_pixel_value = np.max(data)

L = 256

stretched_image = np.zeros_like(data, dtype=int)


for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        stretched_image[i, j] = ((data[i, j] - min_pixel_value) / (max_pixel_value - min_pixel_value)) * (L - 1)

stretched_image = stretched_image.astype(int)
  
print(stretched_image)