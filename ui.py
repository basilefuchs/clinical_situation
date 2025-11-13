import streamlit as st
import dspy
from clinical_situation import modules, utils

model = "qwen3:latest"

if "dspy_ready" not in st.session_state:
    dspy.configure(lm=utils.lm(model))
    st.session_state.dspy_ready = True

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
    unsafe_allow_html=True,
)

st.header("**Clinical Situation**")
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
        on_change=trigger_analysis,
    )

with col_output:
    st.write("*Analyse du texte*:")
    placeholder = st.empty()

    if st.session_state.analyze_trigger and text.strip() != "":
        with st.spinner("En cours ...", show_time=True):
            classifier = modules.ClinicalSituation()
            extractor = modules.Extract("severity")

            clinicalsituation = classifier(text)
            annotated_words = extractor(text)

            classification, confidence = clinicalsituation

            markdown_output = f"**Situation clinique :** <span style='background-color: #ff433d; color:white; display: inline-block; padding: 2px 6px; border-radius:4px; line-height:1.2;'><b>{classification} ({confidence:.2f})</b></span><br><br>"
            annotated_text = utils.highlight_text_by_severity(text, annotated_words)

        placeholder.markdown(
            markdown_output + "\n" + annotated_text, unsafe_allow_html=True
        )

        st.session_state.analyze_trigger = False
