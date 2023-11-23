import openai

# OpenAI API 키 설정
openai.api_key = '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'

def chat_with_gpt4(message, chat_log=[]):
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=chat_log + [{"role": "user", "content": message}]
    )
    answer = response.choices[0].message["content"]
    chat_log.append({"role": "system", "content": answer}) # 시스템(봇)의 응답을 대화 이력에 추가
    return answer, chat_log

# 사용 예시
chat_log = []
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    answer, chat_log = chat_with_gpt4(user_input, chat_log)
    print(f"AI: {answer}")
