import time  
import winsound  
  
def focus_timer(minutes):  
    # 播放欢迎消息  
    print("专注时间开始了！")  
  
    # 倒计时开始  
    while minutes > 0:  
        print(minutes, "分钟剩余...")  
        winsound.Beep(1000, 1000)  # 播放提示音  
        time.sleep(1)  # 等待1秒钟  
        minutes -= 1  
  
    # 倒计时结束  
    print("时间到！")  
    winsound.Beep(1000, 500)  # 播放结束音  
    print("你已经完成了专注时间。")  
  
# 从用户输入获取专注时间  
focus_time = int(input("请输入你要专注的时间（分钟）： "))  
  
# 开始专注时间  
focus_timer(focus_time)
