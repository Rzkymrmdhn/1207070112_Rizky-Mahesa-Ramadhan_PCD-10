# tampilkan kedua gambar
from matplotlib import pyplot as plt
import cv2
# panggil dan konversi warna agar sesuai dengan Matplotlib
einstein = cv2.imread('sendiri.jpg')
einstein = cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB) # simpan dengan nama yang sama = ditumpuk
# panggil dan konversi warna agar sesuai dengan Matplotlib
solvay = cv2.imread('berempat.jpg')
solvay = cv2.cvtColor(solvay, cv2.COLOR_BGR2RGB) 
plt.subplot(121),plt.imshow(einstein), plt.title('wajah')
plt.subplot(122),plt.imshow(solvay), plt.title('berempat')
plt.show()