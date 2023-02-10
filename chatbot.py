import openai
import streamlit as st
openai.api_key = "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"
@st.cache(allow_output_mutation=True)
# openai.api_key = "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"

def generate_response(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    message = completion.choices[0].text
    return message

def chat_history():
    if 'generated' not in st.session_state:
        st.session_state.generated = []
    if 'past' not in st.session_state:
        st.session_state.past = []

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.write("AI:", st.session_state['generated'][i], key=str(i))
            st.write("You:", st.session_state['past'][i], key=str(i) + '_user')

def get_input():
    user_input = st.text_input("You:")
    return user_input

def main():
    st.header("This chatBot is created by Syed Hurairah And Sahil")
    st.title("ChatBot : Streamlit + OpenAI")
    user_input = get_input()
    if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
    chat_history()

if __name__ == '__main__':
    main()
st.title("Simple to use")