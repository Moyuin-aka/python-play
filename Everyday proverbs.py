import random
#简单打招呼输入名字
guest_name = input("Your name:")
for_example=f"{guest_name}".title().strip()
print(f"Hello,{for_example}!\nGlad to see you!")

#构建随机谚语库
proverbs = ["Absence makes the heart grow fonder.",
            "Actions speak louder than words.",
            "A journey of a thousand miles begins with a single step.",
            "All good things must come to an end.",
            "A picture is worth a thousand words",
            "A watched pot never boils.",
            "Beggars can’t be choosers.",
            "Beauty is in the eye of the beholder.",
            "Better late than never.",
            "Birds of a feather flock together."]#我之后研究研究怎么从网页直接导入库
while True:
  everyday_saying_check=input("Do you wanna some common proverbs to embrace the brand new day?(yes/no)")
  if everyday_saying_check.lower().strip()==("yes"):
    print(random.choice(proverbs).title())#获取随机谚语
    #只有这个能循环，虽然有点小bug，循环到上一句有点烦
    while True:
      continue_check=input("Do you wanna get more?(yes/no)")
      if continue_check.strip().lower()=="yes":
        print(random.choice(proverbs).title())
      elif continue_check.strip().lower()=="no":
        print("OK.Have a nice day!")
        break 
      else:
        print('please answer it with "yes" or "no",thanks.' )#在回答yes添加问是否下一步的行为，逻辑更通畅
  elif everyday_saying_check.lower().strip() == ("no"):
    print("Alright.Have a good day!")
    break
  else:
    message='please answer it with "yes" or "no",thanks.' 
    print(message)
#免得大伙抖机灵乱答



