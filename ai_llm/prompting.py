# python get-pip.py
# get-pip.py
import google.generativeai as genai
import streamlit as st
from api import call_weather
import requests

def get_api_key(file_name):
    with open(file_name,"r") as file:
        return file.read().strip()

genai.configure(api_key=get_api_key("p.txt"))
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash',
                              system_instruction=[
                                  '''As a travel planner ur role is to assist users in planning their ideal trip.Here are some examples
                                  <EXAMPLE>
                                  INPUT: 
                                  I'm planning a solo trip to tokyo for a week
                                  OUTPUT:
                                  -Destination:Tokyo
                                  -Duration: 1 week
                                  <EXAMPLE>
                                  INPUT: 
                                  I'm planning a solo trip to dubai for 5 days
                                  OUTPUT:
                                  -Destination:dubai
                                  -Duration: 5 days
                                  <EXAMPLE>
                                  INPUT: 
                                  I'm planning a solo trip to india for a month
                                  OUTPUT:
                                  -Destination:india
                                  -Duration: 1 month'''
                              ],
                              generation_config={
                                  "temperature":2,
                                  "top_p":0.95,
                                  "top_k":30,
                                  "stop_sequences":[
                                  ],
                                 "max_output_tokens":100,
                              },
                              safety_settings={
                                  genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH:
                                      genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
                              }
                              )

model2 = genai.GenerativeModel('gemini-1.5-flash',
                               system_instruction=['''
                               You extract the destinations from the prompts. Here are a few examples
                               <EXAMPLE>
                               INPUT: I want to go to Tokyo for a 5 day trip.I'm planning a solo trip.
                               OUTPUT: Tokyo
                               </EXAMPLE>
                               <EXAMPLE>
                               INPUT: I want to go to London for a week trip.I'm planning a family trip.
                               OUTPUT: London
                               </EXAMPLE>
                               <EXAMPLE>
                               INPUT: Hey
                               OUTPUT: NULLNOCITY
                               </EXAMPLE>
                               '''

                               ])


# chat_session = model.start_chat(
#     history=[
#         # {
#         # "role":"user",
#         # "parts":[
#         #     "I want to go to sweden"
#         # ],
#         # },
#         # {
#         #     "role":"model",
#         #     "parts":[
#         #         "Sure! let me know what kind of trip you are looking for"
#         #     ],
#         # },
#     ]
# )
st.title("Travel Bot ☺")
# st.text("What is your name")
# st.write("Shryes")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

def translate_role_for_streamlit(user_role):
        if user_role == "model":
            return "assistant"
        else:
            return user_role

for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

prompt = st.chat_input("Ask Gemini")
if prompt:
        st.chat_message("user").markdown(prompt)
        #resp = st.session_state.chat_session.send_message(prompt)
        city_resp = model2.generate_content(prompt)
        city = city_resp.text.strip()
        if city != "NULLNOCITY":
            weather = call_weather(city)
            combined_prompt = f"{prompt} \n\nWeather is {weather}"
            resp = st.session_state.chat_session.send_message(combined_prompt)
            with st.chat_message("assistant"):
                st.markdown(resp.text)

        else:
            resp = st.session_state.chat_session.send_message(prompt)
            with st.chat_message("assistant"):
                st.markdown(resp.text)


# if prompt:=st.chat_input("Please enter your query here "):
#     st.chat_message("user").markdown(prompt)
#     resp = f"{st.session_state.chat_session.send_message(prompt).text}"
#     with st.chat_message("assistant"):
#         st.markdown(resp)

# prompt = ""
# while prompt!="exit":
#     prompt=input("please enter query or type exit")
#     #resp = model.generate_content(prompt)
#     resp = chat_session.send_message(prompt)
#     print(resp.text)
