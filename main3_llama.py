# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은 ")
# print(result)

# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# result = chat_model.predict("hi!")
# print(result)

# from dotenv import load_dotenv
# load_dotenv()
# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# content = "코딩"
# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)

# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers

llm = CTransformers(
    model = "llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type = "llama"
)

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = llm.predict("write a poem about" + content + ": ")
        st.write(result)







