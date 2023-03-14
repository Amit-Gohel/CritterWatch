import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
import os


def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((512, 512))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# Define a function to get the model's prediction for an image
def get_prediction(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    return prediction


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Define a list of class names
class_names = ['Background', 'Hart']

# Load the saved model from disk
model = tf.keras.models.load_model('model.h5')

# Open the first video capture device (typically the default webcam)
cap = cv2.VideoCapture(0)

# Loop over frames from the video capture device
while True:
    # Capture a frame from the video capture device
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("input.jpg", frame)
        prediction = get_prediction("input.jpg")
        print(prediction)
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
