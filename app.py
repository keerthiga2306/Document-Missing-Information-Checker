import streamlit as st
from pypdf import PdfReader
from docx import Document
from checker import check_missing_information
st.set_page_config(
    page_title="Document Missing-Information Checker",
    page_icon="📄",
    layout="centered"
)
st.title("📄 Document Missing-Information Checker")
st.write(
    "Upload a PDF, DOCX, or TXT document "
    "to check whether important information is missing."
)
uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx", "txt"]
)
def extract_text(file):
    file_name = file.name.lower()
    if file_name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    elif file_name.endswith(".docx"):
        document = Document(file)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
        return text
    elif file_name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""
if uploaded_file is not None:
    st.success(
        f"Uploaded: {uploaded_file.name}"
    )
    try:
        document_text = extract_text(uploaded_file)
        if not document_text.strip():
            st.error(
                "❌ No readable text found in this document."
            )
        else:
            found_fields, missing_fields = (
                check_missing_information(document_text)
            )
            st.subheader("✅ Information Found")
            if found_fields:
                for field in found_fields:
                    st.success(field)
            else:
                st.info(
                    "No required information was found."
                )
            st.subheader("⚠️ Missing Information")
            if missing_fields:
                for field in missing_fields:
                    st.warning(
                        f"Missing: {field}"
                    )
            else:
                st.success(
                    "🎉 No required information is missing!"
                )
            with st.expander("📖 View Extracted Text"):
                st.text(document_text)
    except Exception as error:

        st.error(
            f"❌ Error while processing document: {error}"
        )