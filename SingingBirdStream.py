import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("QR Code Creator")
st.write("Where links become squares.")

default_url = "https://www.youtube.com/watch?v=P5kYgjV2DXM&list=PLi--g4OaB3-YyMq-JXE61sWDGYe5tiDBs&index=10"

user_input = st.text_input("Insert magic words or sneaky link", default_url)

if user_input:
    qr = qrcode.make(user_input)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    st.subheader("Generated QR Code")
    st.image(image_bytes, caption="Scan to open link")

    st.download_button(
        label="Download QR Code",
        data=image_bytes,
        file_name="qrcode.png",
        mime="image/png"
    )
