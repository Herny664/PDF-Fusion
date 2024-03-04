import streamlit as st
import PyPDF

#Vars
output_pdf = "documents/pdf_combined.pdf"

#functions
def combine_pdfs(output_path, documents):
    pdf_combined = PyPDF.PdfMerger()

    for document in documents:
        pdf_combined.append(document) #Add each PDF to the final fusion
    pdf_combined.write(output_path) #Save Combined PDF in output path

#Frontend
st.image("img/fusion-pdf.png")
st.header("Combine PDFs Simply and efectively")
st.subheader("Attach PDFs to combine")
pdfs_attached = st.file_uploader(label="", accept_multiple_files=True)
fusion = st.button(label="Combine PDFs")

if fusion:
    if len(pdfs_attached) <= 1:
        st.Warning("Please, make sure to attach more than one PDF")
    else:
        combine_pdfs(output_pdf, pdfs_attached)
        st.success("Here it is. You can download the PDF combined.")
        with open(output_pdf, "rb") as file:
            pdf_data = file.read()
        st.download_button(label="Download PDF Combined", data=pdf_data, file_name="PDF_Combined.pdf")