import datetime
import requests
import sys

'''凌晨 (0-4点): 0 <= hour < 5,
早上 (5-11点): 5 <= hour < 12,
中午 (12-13点): 12 <= hour < 14,
下午 (14-17点): 14 <= hour < 18,
晚上 (18-23点): 18 <= hour < 24'''

def get_greeting()->str:
    '''根据当前时间返回问候语'''
    hour = datetime.datetime.now().hour
    if 0 <= hour < 5:
        return "凌晨好"
    elif 5 <= hour < 12:
        return "早上好"
    elif 12 <= hour < 14:
        return "中午好"
    elif 14 <= hour < 18:
        return "下午好"
    else:
        return "晚上好"
def ask(prompt:str)->bool:
    '''向用户提问返回yes or no，判断接下来是否继续进行'''
    while True:
        response=input(prompt).strip().lower()
        if response=="yes" :
            return True
        elif response=="no":
            return False
        else:
            print('请用“yes”或“no”回答，谢谢。') # 提示用户输入正确的格式
def greet_user():
    '''简单打招呼输入名字'''
    guest_name = input("你叫什么名字呢？").title().strip()
    greeting = get_greeting()
    print(f"{greeting}! {guest_name}!\n")

def get_proverbs()->str:
    try:
        response=requests.get("https://v1.hitokoto.cn/?encode=json&charset=utf-8")
        response.raise_for_status() # 确保请求成功
        data = response.json()
        proverb=f"“{data['hitokoto']}” - {data['from']}"
        return proverb
    except requests.RequestException as e:
        print("网络错误，无法获取到名言。")
        return "请检查网络连接。"
    
if __name__ == "__main__":
    greet_user()
    hour = datetime.datetime.now().hour
    if 0<=hour<5:
        print("你还不睡觉吗？好好休息吧！")
        sys.exit(0)  # 如果是凌晨，直接退出程序
        

    while True:
        if ask("你想用一些鸡汤开启今天吗？ (yes/no) "):
            print(get_proverbs())
            while True:
                if not ask("你还想要么？ (yes/no) "):
                    print("好，今日顺遂!")
                    sys.exit(0)  # 如果用户不想继续，退出程序
                else:
                    print(get_proverbs())
        else:
            print("\n好的，玩的开心!")
            break
        