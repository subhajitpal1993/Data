import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHSBC: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative and provides automated queries.\n\nHSBC: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHSBC: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=250,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" HSBC:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


with gr.Blocks(css=".gradio-container {background-color: grey}") as demo:
    gr.Markdown("""<h1><center>Get Automated Query</center></h1>
    """)
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input")
            with gr.Row():
                submit = gr.Button("Submit")
        with gr.Column():
            chatbot = gr.Textbox(label="Automated Query")

    submit.click(openai_create, input_text, chatbot)

demo.launch(debug=True)