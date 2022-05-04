# imagePositionFinding = 0 변수
# IMAGEPOSITIONFINDING = 0 상수

# Only for Window!!!!!!!! ㅠㅠ

import pyautogui as pg

imageLocation = pg.locateOnScreen('naver.png') # 이 이미지가 있는 위치 가져옴
point = pg.center(imageLocation)
print(imageLocation[0], imageLocation[1]) # Left = x, top = y, width = 너비, height = 높이

