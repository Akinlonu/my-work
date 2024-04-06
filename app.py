import os
from pdfminer.high_level import extract_text
from docx import Document
import streamlit as st

import numpy as np
from gensim.models import KeyedVectors
import joblib


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
# model = KeyedVectors.load_word2vec_format('Google-News-Vectors/GoogleNews-vectors-negative300.bin', binary=True)


def main():
    st.write(
        """<h3 align="center">Effective Elicitation Of Functional Requirement Features For Quality 
        Software Development</h3>""", unsafe_allow_html=True
    )

    st.write(
        """<h4 align="center">Akinlonu Adebisi Opeyemi 232997</h4>""", unsafe_allow_html=True
    )

    st.write(
        """<p align="center">Supervised  by:   Dr. B.I. Ayinla</p>""", unsafe_allow_html=True
    )

    st.write("""
        #### About
        <p align="justify">The objective of this project is the development of an improved software functional 
            requirement elicitation model using Word2vec. For the completion of this study, Natural language processing will be used to assist in data gathering for client's software system, extract and interpret requirement by subjecting it to machine learning from natural language text and also creating summaries of text automatically using algorithms while preserving its most important information and also checking if the left over words after extraction are important to the software system.
        </p>""", unsafe_allow_html=True
    )

    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a elicited file (Accepted format: txt)")

    if uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[1]
        if file_extension == '.txt':
            file_contents = uploaded_file.read().decode('latin1')
        else:
            st.write("Unsupported file type. Please upload a .txt file.")
            return  

        st.write("Extracted Functional Requirements:")

        file_contents = file_contents.replace('', '').replace('', '').replace('â', '')

        st.write(HTML_WRAPPER.format(file_contents), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
