import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time
import urllib.request
import os


def googleCrawling(searchingList, gender, entertainment):
    for keyword in searchingList:
        URL = f'https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=1200&bih=890&ei=JcLwX62ZPKaymAXqoYOABA&q={keyword}'

        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.get(url=URL)

        SCROLL_PAUSE_SEC = 1

        scrollCnt = 0
        
        while True:
            print(keyword, scrollCnt, '스크롤중...')
            if scrollCnt == 10:
                break
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_SEC)
            scrollCnt += 1
            try:
                # 1초 대기
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                continue


        imagesList = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        for idx, image in enumerate(imagesList):
            print(f'{keyword} {idx} 다운로드 중...')
            if idx > 100:
                break
            imageURL = image.get_attribute('src')
            if imageURL:  
                directory = f'./images/{entertainment}/{gender}/{keyword}'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                urllib.request.urlretrieve(imageURL, f"./{directory}/{keyword}_{idx}.jpg")

    

smManList = [
"엑소 수호", "엑소 카이", "엑소 시우민", "엑소 백현", "엑소 찬열", "엑소 첸", "엑소 레이", "엑소 디오", "엑소 세훈",
"유노윤호", "최강창민", 
"슈퍼주니어 이특", "슈퍼주니어 희철", "슈퍼주니어 예성", "슈퍼주니어 신동", "슈퍼주니어 성민", "슈퍼주니어 은혁", "슈퍼주니어 동해", "슈퍼주니어 시원", "슈퍼주니어 려욱", "슈퍼주니어 규현",
"샤이니 민호", "샤이니 온유", "샤이니 Key", "샤이니 태민",
"NCT 태일", "NCT 쟈니", "NCT 태용", "NCT 유타", "NCT 쿤", "NCT 도영", "NCT 텐", "NCT 재현", "NCT 윈윈", "NCT 정우", "NCT 루카스", "NCT 마크", "NCT 런쥔", "NCT 제노", "NCT 해찬","NCT 재민", "NCT 천러", "NCT 지성", "NCT 샤오쥔", "NCT 양양", "NCT 헨드리", "NCT 쇼타로", "NCT 성찬"
]


smWomenList = [
"소녀시대 태연", "소녀시대 써니", "소녀시대 효연", "소녀시대 유리", "소녀시대 윤아",
"레드벨벳 아이린", "레드벨벳 슬기", "레드벨벳 웬디", "레드벨벳 조이", "레드벨벳 예리",
"에스파 카리나", "에스파 지젤", "에스파 윈터", "에스파 닝닝"
]



jypManList = [
    "2PM 준케이", "2PM 닉쿤", "2PM 택연", "2PM 우영", "2PM 준호", "2PM 찬성",
    "GOT7 JB", "GOT7 마크", "GOT7 잭슨", "GOT7 진영", "GOT7 영재", "GOT7 뱀뱀", "GOT7 유겸",
    "데이식스 성진", "데이식스 Jae", "데이식스 영케이", "데이식스 원필", "데이식스 도운",
    "스트레이 키즈 방찬", "스트레이 키즈 리노", "스트레이 키즈 창빈", "스트레이 키즈 현진", "스트레이 키즈 한", "스트레이 키즈 필릭스", "스트레이 키즈 승민", "스트레이 키즈 아이엔"
]

jypWomenList = [
    "트와이스 지효", "트와이스 나연", "트와이스 정연", "트와이스 모모", "트와이스 사나", "트와이스 미나", "트와이스 다현", "트와이스 채영", "트와이스 쯔위",
    "ITZY 예지", "ITZY 리아", "ITZY 류진", "ITZY 채령", "ITZY 유나"
]

ygManList = [
    "빅뱅 지드래곤", "빅뱅 탑", "빅뱅 태양", "빅뱅 대성",
    "위너 송민호", "위너 김진우", "위너 강승윤", "위너 이승훈",
    "아이콘 김진환", "아이콘 송윤형", "아이콘 BOBBY", "아이콘 김동혁", "아이콘 구준회", "아이콘 정찬우",
    "트레저 방예담", "트레저 윤재혁", "트레저 하루토", "트레저 소정환", "트레저 준규", "트레저 박정우", "트레저 최현석", "트레저 마시호", "트레저 도영", "트레저 요시", "트레저 지훈", "트레저 아사히"
]


googleCrawling(smManList, "men", "sm")
googleCrawling(smWomenList, "women", "sm")

googleCrawling(jypManList, "men", "jyp")
googleCrawling(jypWomenList, "women", "jyp")

googleCrawling(ygManList, "men", "yg")
googleCrawling(ygWomenList, "women", "yg")

