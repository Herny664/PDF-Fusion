import streamlit as st

#Frontend
st.image("img/fusion-pdf.png")
st.header("Combine PDFs Simply and efectively")
st.subheader("Attach PDFs to combine")
pdfs_attached = st.file_uploader(label="", accept_multiple_files=True)
fusion = st.button(label="Combine PDFs")