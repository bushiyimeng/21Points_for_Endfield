import pyautogui
import time
import sys
import pydirectinput
from pathlib import Path

#!!!!!重要!!!!! 使用时用管理员权限运行，否则不对zmd生效
#打开抽牌界面使用

current_dir = Path(__file__).parent
Asset = current_dir / "Asset"

for i in range(1,4):
    print("start in "+str(4-i)+" seconds...")
    time.sleep(1)

def search(x,y,w,h):
    print("search started")
    ans = 0
    
    for i in range(1,6):
        print("searching "+str(i))
        try:
            location = pyautogui.locateOnScreen(
            str(Asset)+'/'+str(i)+'.png',
            confidence=0.9,
            region=(x,y,w,h),
            )
            #查找的图片
            if location is not None:
                ans = i
                print(ans)
                break
            else:
                print("search"+str(i)+"failed")
        except pyautogui.ImageNotFoundException as e:
            continue
    return ans

while True:
    for i in range(1,6):
        pyautogui.click(1751,813)
        time.sleep(1.5)
    sum = 0
    for i in range(0,5):
        ans = search(280+300*i,215,60,70)
        if ans is not None:
            sum+=int(ans)
    print("sum of points:"+str(sum))
    if sum>=21:
        print("-End-")
        sys.exit()
    time.sleep(3)
    print("next round","\n","-----------")
    pyautogui.click(214,983)
    time.sleep(1.5)
    pydirectinput.press('f')
    time.sleep(1.5)
