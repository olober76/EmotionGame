
# Copy Emotion GAME

This is a Python program code where the user must match his facial expression to the emotional display that will be displayed randomly by the program.
In this program, users are required to complete the game by imitating the emojis displayed. For each similar expression, 10 points will be added and 
when our points reach 200, a picture will be taken from the camera and saved in the **./image** directory as a form of achievement for completing the game.

This program uses a machine learning model to predict the form of emotion that is input in the form of a camera. For face detection, this program uses 
OpenCV with Haar Cascade Face Detector as a face detector.

The following are various types of images that represent human emotions as a reference for users to imitate their expressions.

| Picture                                                                                                                        | Type of emotion |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| <img src=https://github.com/olober76/EmotionGame/assets/90765208/6ad20a89-9a5f-42c6-8a1e-8951c5214e4d width=250 height=250>    | **Biasa**       |
| <img src=https://github.com/olober76/EmotionGame/assets/90765208/73bea68c-3d46-4ead-bfd2-2519c573871a width=250 height=250>    | **Marah**       |
| <img src=https://github.com/olober76/EmotionGame/assets/90765208/40d80bbf-8cef-4fc7-a13b-43d7b5f986b1 width=250 height=250>    | **Sedih**       |
| <img src=https://github.com/olober76/EmotionGame/assets/90765208/c1af52ab-ad85-4ffd-ab5e-4f0d61aab6bc width=250 height=250>    | **Senang**      |
| <img src=https://github.com/olober76/EmotionGame/assets/90765208/5776673d-e873-4eab-a3d4-7a13b11aa723 width=250 height=250>    | **Terkejut**    | 


## Installation and How to Use

First, need to build an environment to run this code (Using Python 3.8). If you are using anaconda, here is command line

`conda create -n emojiGame python=3.8`

Then you can  install the requirements package, and use the pip to install all the packages that are needed

`cd EmotionGame`
`pip install -r requirements.txt`


## Preview

Here is the preview of how to code should work
| **Preview Video**                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------- |
| <video  width=900 height=450 src=https://github.com/olober76/EmotionGame/assets/90765208/6f013892-bc80-4599-af5e-7e325fbeb7bb > |




