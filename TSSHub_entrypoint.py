import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import random

st.set_page_config(
    page_title="TSSHub",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
        )

st.title('TSSHub')

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp()
def home():
    st.header('Welcome to TSSHub!', divider='rainbow')
    st.subheader('Data collection')
    st.text('The species we collected shows below:')
    species_names = ["Arabidopsis thaliana", "Oryza sativa", "Drosophila melanogaster",
                 "Homo sapiens", "Saccharomyces cerevisiae", "Gallus gallus"]
    data_counts = [random.randint(100, 300) for _ in species_names]
    df = pd.DataFrame({
    'Species': species_names,
    'Data Count': data_counts
    })
    st.bar_chart(df.set_index('Species'))



@app.addapp()
def Jbrwose():
 hy.info('Hello from Jbrwose')


@app.addapp()
def prediction_models():
    st.title('TSSFinder')
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

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()

