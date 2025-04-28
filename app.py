import streamlit as st
from PIL import Image
import pytesseract
import base64

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change path if needed

st.set_page_config(
    page_title="VisionText OCR",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .big-font {
            font-size: 36px !important;
            font-weight: 700;
            color: #4a4a4a;
        }
        .sub-font {
            font-size: 18px !important;
            color: #6e6e6e;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stDownloadButton>button {
            background-color: #0e76a8;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/535/535137.png", width=100)
    st.header("📤 Upload Your Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    st.markdown("---")
    st.caption("Made with ❤️ using Tesseract OCR")

st.markdown('<p class="big-font">VisionText OCR App</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Extract text from any image instantly with beautiful results!</p>', unsafe_allow_html=True)
st.markdown("---")

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="📸 Uploaded Image Preview", use_column_width=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        if st.button("🚀 Extract Text", use_container_width=True):
            with st.spinner("Processing your image... ⏳"):
                try:
                    # OCR process
                    text = pytesseract.image_to_string(image)

                    st.success("✅ Text extraction successful!")
                    st.markdown("### 📝 Extracted Text")
                    st.text_area("", text, height=300)

                    st.download_button(
                        label="📥 Download Text",
                        data=text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"❌ Error during OCR: {str(e)}")

    with col2:
        st.info("👈 Click the button to extract text from the image!")

else:
    st.warning("⚠️ Please upload an image to start OCR extraction.")

# Footer
st.markdown("---")
st.markdown(
    "<center>© 2025 VisionText OCR | Built with ❤️ using Streamlit & Tesseract</center>",
    unsafe_allow_html=True
)
