import numpy as np

# data 10 hari
suhu_c = np.array([31, 32, 29, 30, 29, 31, 29, 33, 34, 28])

# konversi celsius ke fahrenheit
suhu_f = suhu_c * 9/5 + 32

print("Celsius    :", suhu_c)
print("Fahrenheit :", suhu_f)