import streamlit as st
import dspy
from clinical_situation import utils

model = "gpt-oss-20b"

if "dspy_ready" not in st.session_state:
    dspy.configure(lm=utils.lm(model))
    st.session_state.dspy_ready = True

# frontend
st.set_page_config(page_title="Clinical Situation", page_icon="💭", layout="wide")

if "textarea_content" not in st.session_state:
    st.session_state.textarea_content = ""

if "analyze_trigger" not in st.session_state:
    st.session_state.analyze_trigger = False

st.markdown(
    """
    <style>
        .block-container{
                padding-top: 25px;
            }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("💭***Clinical Situation***")
st.write("*Powered by* `" + model + "`")

col_input, col_output = st.columns(2)

def trigger_analysis():
    st.session_state.analyze_trigger = True

with col_input:
    text = st.text_area(
        "text",
        st.session_state.textarea_content,
        height=700,
        label_visibility="collapsed",
        placeholder="... ou copier-coller votre texte ici",
        key="input_text",
        on_change=trigger_analysis  # déclenche l'analyse avec ctrl+enter
    )

with col_output:
    st.write("*Analyse du texte*:")
    placeholder = st.empty()

    if st.session_state.analyze_trigger and text.strip() != "":
        with st.spinner("En cours ...", show_time=True):
            annotated_words = utils.extract_list(text)
            annotated_text = utils.highlight_text(text, annotated_words)
            clinicalsituation = utils.assess_situation(text)

        placeholder.markdown(clinicalsituation, unsafe_allow_html=True)
        placeholder.markdown(annotated_text, unsafe_allow_html=True)

        # Réinitialise le trigger pour ne pas relancer automatiquement
        st.session_state.analyze_trigger = False
