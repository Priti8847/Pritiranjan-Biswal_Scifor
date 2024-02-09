import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the pre-trained ANN model
model = load_model('mnist_classification.h5')

# Define a function to preprocess the uploaded image
def preprocess_image(img):
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values
    return img

# Define the Streamlit app
st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon=":pencil2:",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title('Handwritten Digit Recognition')
st.write("Upload an image of a handwritten digit and let the model predict it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    try:
        img = image.load_img(uploaded_file, target_size=(28, 28), color_mode='grayscale')
        img = preprocess_image(img)
        prediction = model.predict(img).argmax()
        st.success(f'Predicted Digit: {prediction}')
    except Exception as e:
        st.error(f'Error: {e}')
