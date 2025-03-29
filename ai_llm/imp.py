import PIL
import google.generativeai as genai

def get_api_key(file_name):
    with open(file_name,'r') as file:
        return file.read().strip()

genai.configure(api_key=get_api_key("p.txt"))
image_file = PIL.Image.open("image.jpg")

model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(
    history=[

    ]
)

prompt = ""
while prompt!="exit":
    prompt=input("please enter query or type exit")
    #resp = model.generate_content(prompt)
    resp = chat_session.send_message([prompt,image_file])
    print(resp.text)
