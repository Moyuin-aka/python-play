from ollama import chat
from ollama import ChatResponse
response: ChatResponse=chat(model='deepseek-r1:7b',messages=[{'role':'user','content':'你好，Luv🥰',},])
print(response['message']['content'])