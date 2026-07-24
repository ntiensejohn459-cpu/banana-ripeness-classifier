import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(page_title="Banana Ripeness Classifier", page_icon="🍌", layout="centered")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("banana_model.keras")
    return model

def predict(model, pil_image):
    img = pil_image.convert("RGB").resize((128, 128))
    arr = np.expand_dims(np.array(img, dtype=np.float32), axis=0)
    prob_yellow = float(model.predict(arr, verbose=0)[0][0])
    prob_green = 1.0 - prob_yellow
    label = "Yellow (Ripe)" if prob_yellow >= 0.5 else "Green (Unripe)"
    return label, prob_green * 100, prob_yellow * 100

st.title("🍌 Banana Ripeness Classifier")
st.write("Upload a banana image to check if it's green (unripe) or yellow (ripe).")

model = load_model()
uploaded_file = st.file_uploader("Upload a banana image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, width=300)
    label, green_pct, yellow_pct = predict(model, img)
    st.write(f"**Prediction:** {label}")
    st.progress(int(green_pct), text=f"Green: {green_pct:.1f}%")
    st.progress(int(yellow_pct), text=f"Yellow: {yellow_pct:.1f}%")
