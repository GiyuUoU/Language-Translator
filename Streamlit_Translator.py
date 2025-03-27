
#For running this code -->(Run this command in cmd) cd C:\Projects\Python projects\Using streamlit
#Then run this --> python3 -m streamlit run Streamlit_Translator.py


import streamlit as st
from googletrans import Translator, LANGUAGES
from PIL import Image

# Load language names
languages = {code: name.title() for code, name in LANGUAGES.items()}
language_names = list(languages.values())  # List of language names for searching

# Load and display the logo (if available)
st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translator")

try:
    logo = Image.open("logo.png")  # Ensure "logo.png" is in the same directory
    st.image(logo, width=100)
except:
    pass  # Skip logo if not found

# User input text
text = st.text_area("Enter text to translate:")

# Searchable language selection
target_lang = st.selectbox("Select Target Language:", options=language_names, index=language_names.index("Hindi"))

# Translation function
def translate_text(text, target_lang):
    if not text.strip():
        return "Please enter text to translate."
    
    target_code = next((code for code, name in languages.items() if name == target_lang), None)

    if target_code:
        translator = Translator()
        translation = translator.translate(text, dest=target_code)
        return translation.text
    else:
        return "Invalid language selection."

# Translate button
if st.button("Translate"):
    translated_text = translate_text(text, target_lang)
    st.subheader("Translated Text:")
    st.write(translated_text)
