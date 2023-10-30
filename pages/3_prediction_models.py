import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import random

st.title("TSS prediction models")
st.header('TSSFinder',divider="rainbow")
sequence_input = st.text_area("Please input your sequence", ">genome_fasta\nCTGATTTTCGTTGGCCCTAGATTTCATCAATCTCTAATTTCATTTTGTATTTTTATCGTTTTGAAATTTAAATGTCAAGTCCCAACGGTCCTCTGATCTCGGCAGTTTTTGTGTTATGTAAATGACTA")

uploaded_files = st.file_uploader("Choose a FASTA file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
species = st.selectbox("Please select your species", ["Arabidopsis thaliana", "Oryza sativa", "Drosophila melanogaster", "Homo sapiens", "Saccharomyces cerevisiae","Gallus gallus"])
if st.button("run tssfinder"):
    completed_process = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    st.write("OUTPUT：")
    st.code(completed_process.stdout)

st.header('TSSPlant',divider="rainbow")

