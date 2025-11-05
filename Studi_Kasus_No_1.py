import numpy as np

# data dummy 10 hari
suhu_c = np.array([31, 32, 31, 30, 29, 31, 29, 33, 34, 28])

# convert ke fahrenheit
suhu_f = suhu_c * 9/5 + 32

print("Celsius    :", suhu_c)
print("Fahrenheit :", suhu_f)