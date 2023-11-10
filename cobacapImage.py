import cv2
import os

# Membuat objek VideoCapture
cap = cv2.VideoCapture(0)

# Membaca frame dari kamera
ret, frame = cap.read()

# Menampilkan frame
cv2.imshow('Gambar', frame)

# Menunggu hingga tombol 's' ditekan untuk menyimpan gambar
if cv2.waitKey(1) & 0xFF == ord('s'):
    # Tentukan direktori tempat Anda ingin menyimpan gambar
    directory = "..EmotionGame/gambar/"
    
    # Pastikan direktori tersebut ada. Jika tidak, buat direktori tersebut.
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Simpan gambar di direktori yang ditentukan
    cv2.imwrite(os.path.join(directory, 'gambar.png'), frame)

# Menutup jendela dan melepaskan objek VideoCapture
cap.release()
cv2.destroyAllWindows()
