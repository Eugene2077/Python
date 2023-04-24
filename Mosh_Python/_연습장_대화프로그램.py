
# 대화 프로그램
# dic 에 미리 어떤 질문이 오면 어떤 답을할지 정해서 수많은 예시를 넣어놓고, 사용자의 input 이 dic 에 있는 key 와 일치하면 그 value를 출력한다


dic = {
    "hello":"Hello", 
    "how are you?": "I am good, and you?", 
    "i am good":"what's up today?",
    "yes": "Okay, I'm listening",
    "who are you?": "I'm a computer, talking computer",
    "can you talk?": "Yes, I can talk, and a good listener"
    }

random_opening = "Hey, do you wanna talk?"

print(random_opening)

while True:
    input_text = input(">>: ")
    input_text = input_text.lower()

    if input_text in dic:
        print(dic[input_text])


    if input_text == "quit":
        break
