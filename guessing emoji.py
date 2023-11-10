import cv2
import numpy as np
import tensorflow as tf
import random

img_senang = cv2.imread("../EmotionGame/list_ekspresiPNG/Senang.png")
img_sedih = cv2.imread("../EmotionGame/list_ekspresiPNG/Sedih.png")
img_terkejut = cv2.imread("../EmotionGame/list_ekspresiPNG/Terkejut.png")
img_biasa = cv2.imread("../EmotionGame/list_ekspresiPNG/Biasa.png")
img_marah = cv2.imread("../EmotionGame/list_ekspresiPNG/Marah.png")
arr_img = [img_terkejut, img_biasa, img_marah, img_senang, img_sedih]
skrinsut = False

face_detection = cv2.CascadeClassifier('haar_cascade_face_detection.xml')

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
settings = {
    'scaleFactor': 1.3, 
    'minNeighbors': 5, 
    'minSize': (50, 50)
}

labels = ['Terkejut', 'Biasa', 'Marah', 'Senang', 'Sedih']

model = tf.keras.models.load_model('../EmotionGame/network-5Labels.h5')

emoji_index = 0
score = 0
def emoji(label):
    if label == labels[0]:
        img = arr_img[0]
    elif label == labels[1]:
        img = arr_img[1]
    elif label == labels[2]:
        img = arr_img[2]
    elif label == labels[3]:
        img = arr_img[3]
    elif label == labels[4]:
        img = arr_img[4]
    return img

emoji_tebak = False

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected = face_detection.detectMultiScale(gray, **settings)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for x, y, w, h in detected:
        cv2.rectangle(img, (x, y), (x+w, y+h), (245, 135, 66), 2)
        cv2.rectangle(img, (x, y), (x+w//3, y+20), (245, 135, 66), -1)
        face = gray[y+5:y+h-5, x+20:x+w-20]
        face = cv2.resize(face, (48, 48))
        face = face/255.0
        
        predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax()
        state = labels[predictions]
        cv2.putText(img, state, (x+10, y+15), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
      # checking label = emoji gui
        if state == labels[emoji_index]:
            score+=10
            emoji_index = random.randint(0, len(arr_img) - 1)  # update emoji
            
        break  # add this line to break the loop after the first face is detecte
    cv2.putText(img, "Tebak Tebakan Emoji", (50, 50),font,1, (0,0,255),2,cv2.LINE_AA )

    if emoji_index >= 0 and emoji_index < len(arr_img):
        emoji_image = arr_img[emoji_index].copy()  # Salin gambar agar tidak mempengaruhi gambar asli
        cv2.putText(emoji_image, f"score: {score}", (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA )
        cv2.imshow('Emoji', emoji_image)

        
    
    cv2.imshow('Facial Expression', img)
    cv2.putText(img, "Tebak Tebakan Emoji", (50, 50),font,1, (0,0,255),2,cv2.LINE_AA )
    if score == 200:
        # index=0
        if skrinsut == False :
            cv2.putText(img, f"Selamat kamu menang tebak emoji!", (200, 500), font, 1, (0, 255, 0), 2, cv2.LINE_AA )
            cv2.imwrite(f"../EmotionGame/gambar/image.png", img)  # change the path to where you want to save the image
            score_image = cv2.imread(f"../EmotionGame/gambar/image.png", )  # read the saved image
            # cv2.resize(score_image, (1080, 720))
            cv2.imshow("Oleh Oleh kalian", score_image,)# display the saved image
            skrinsut = True
            cv2.namedWindow("Oleh Oleh kalian",cv2.WINDOW_FULLSCREEN)
    if cv2.waitKey(1) == ord("r"):
        cv2.destroyWindow("Oleh Oleh kalian")
        score = 0
        skrinsut = False
    # if cv2.waitKey(5) != ord("x"):
    #     break
camera.release()
cv2.destroyAllWindows()
