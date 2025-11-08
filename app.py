import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Free Translator using Deep Translator")
st.divider()

input_text = st.text_area("Enter text to translate:")

source_language = st.selectbox("Source language", ["auto", "english", "spanish", "french", "german", "hindi", "marathi"])
target_language = st.selectbox("Target language", ["english", "spanish", "french", "german", "hindi", "marathi"])

if st.button("Translate"):
    if input_text.strip():
        translation = GoogleTranslator(source=source_language, target=target_language).translate(input_text)
        st.subheader("📝 Translation:")
        st.write(translation)

        st.download_button(
            label="Download Translation as .txt file",
            data=translation,
            file_name="translation.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ Please enter some text to translate.")
