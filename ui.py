import gradio as gr
from example import chain


def chat(question,history):
    if question ==" ":
     return"Please ask a question"
    
    else:
       return chain.invoke(question)

gr.ChatInterface(
    fn=chat,
    type = "messages"
).launch(
   share =True,
   )
with gr.Blocks(title="chatbot") as demo:
   with gr.column():
      chatbox = gr.chatbot(type="messages")
      with gr.Row():
       textbox = gr.Textbox(scale=7)
      submit = gr.Button(text="Submit",scale=3)

demo.launch(
   server_name="0.0.0.0",
   server_port="7860"
)