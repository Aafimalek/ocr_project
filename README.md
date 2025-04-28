# VisionText OCR

🔎 A lightweight, fast, and beautiful web app for Optical Character Recognition (OCR) built using **Streamlit** and **Tesseract OCR**.  
Extract text from images instantly, right from your browser!

---

## 🚀 Features

- 📤 Upload images (`.jpg`, `.jpeg`, `.png`)
- 📝 Extract text from any image using Tesseract OCR
- 📥 Download extracted text as a `.txt` file
- ✨ Modern and clean UI
- ⚡ Works even on low-resource machines (no GPU needed)
- ❤️ Fully open-source and customizable

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aafimalek/ocr-project
   cd visiontext-ocr
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR Engine**

   - **Windows**:  
     Download and install from [Tesseract OCR Wiki](https://github.com/tesseract-ocr/tesseract/wiki)

   - **Ubuntu/Linux**:
     ```bash
     sudo apt install tesseract-ocr
     ```

   - **MacOS**:
     ```bash
     brew install tesseract
     ```

4. **(Windows only)**  
   Set the Tesseract executable path in `app.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

---
## 🏃‍♂️ Run the App

```bash
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

---

## 📦 Project Structure

```bash
visiontext-ocr/
│
├── app.py            # Main Streamlit app
├── assets/           # Images/icons for UI
├── requirements.txt  # Python libraries list
└── README.md         # Project documentation
```

---

## ✨ Future Enhancements

- Support multiple languages (`lang='eng+hin'`)
- Draw bounding boxes on extracted text
- Add dark mode toggle 🌙
- Deploy app on Streamlit Cloud / Huggingface Spaces

---


## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Pillow (PIL)](https://python-pillow.org/)

---

## 🌟 Show your support!

If you like this project, give it a ⭐️ on GitHub!  
Pull requests are welcome!

