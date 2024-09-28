import streamlit as st
import google.generativeai as genai

st.title("SymptomScan: Predicting the disease based on symptoms")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
genai.configure(api_key="AIzaSyC5WKGH75glm-gkNHNjZEXgCfbpIWSEiFQ")
var = ""
var2=""


def create_gen_model():
    return genai.GenerativeModel('models/gemini-pro')


def main():
    query = st.text_input("Enter The Symptoms Here:")
    st.write(" ")
    st.write(" ")
    if st.button("Predict the Disease"):
        model = create_gen_model()
        var = f"I'm experiencing some symptoms like {query} While I can't expect a diagnosis from you, can you help me find disease name from some reliable resources online? If you found disease name only give that name. Not give resource name. Give answer in one line"
        response = model.generate_content(var)
        st.header("Disease Predicted:")
        st.header(response.text)

        var2=f"I am infected with disease known as {response.text}While I can't expect a diagnosis from you,can you help me to suugest propable medications related to this from some reliable sources online?"

        response2=model.generate_content(var2)
        st.header("Predicted Solution:")
        st.header(response2.text)


if __name__ == "__main__":
    main()