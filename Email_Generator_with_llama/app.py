import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getLLMResponse(form_input,email_sender,email_recipient,email_style):
   

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    #Template for building the PROMPT
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

  
    #Generating the response using LLM
    response=llm.invoke(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response


st.set_page_config(page_title="Gerar Emails",
                    page_icon='📧',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Gerador de Emails 📧")

form_input = st.text_area('Insira o tópico do e-mail', height=275)

col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Nome do remetente')
with col2:
    email_recipient = st.text_input('Nome do destinatário')
with col3:
    email_style = st.selectbox('Estilo de escrita',
                                    ('Formal', 'Agradecendo', 'Não satisfeito', 'Neutro'),
                                       index=0)


submit = st.button("Gerar")

if submit:
    st.write(getLLMResponse(form_input,email_sender,email_recipient,email_style))
