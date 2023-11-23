import openai 
import gradio as gr

openai.api_key = "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"


def openai_chat(message, past_messages=[]):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."}] + past_messages + [{"role": "user", "content": message}]
    )
    return response.choices[0].message["content"]


def chatbot(input, history=[]):
    history.append(("user", input))
    output = openai_chat(input, history)
    history.append(("assistant", output))
    return history, history


# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=chatbot,
    inputs=[gr.components.Textbox(lines=2, placeholder="여기에 질문 또는 문장을 입력하세요..."), "state"],
    outputs=[gr.components.Chatbot(), "state"]
)
iface.launch(debug=True, server_name='222.109.212.92', share=True, server_port=80)