import datetime as datetime
import requests
import json
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime

# Start the scheduler
schedule = BackgroundScheduler()
schedule.start()
problem_list = {
    datetime.date(2021, 1, 19): 12865,
    datetime.date(2021, 1, 20): 1655,
    datetime.date(2021, 1, 21): 3197,
    datetime.date(2021, 1, 22): 11401,
    datetime.date(2021, 1, 23): 10830,
    datetime.date(2021, 1, 24): 2933,
    datetime.date(2021, 1, 25): 2749,
    datetime.date(2021, 1, 26): 9376,
    datetime.date(2021, 1, 27): 6549,
    datetime.date(2021, 1, 28): 6087,
    datetime.date(2021, 1, 29): 11066,
    datetime.date(2021, 1, 30): 11049,
    datetime.date(2021, 1, 31): 4991,
    datetime.date(2021, 2, 1): 7579,
    datetime.date(2021, 2, 2): 10942,
    datetime.date(2021, 2, 3): 1039,
    # datetime.date(2021, 1, 20): 9370,
    # datetime.date(2021, 1, 20): 1981,
    # datetime.date(2021, 1, 20): 11657,
    # datetime.date(2021, 1, 20): 2931,
    # datetime.date(2021, 1, 20): 11404,
    # datetime.date(2021, 1, 20): 10217,
    # datetime.date(2021, 1, 20): 2151,
    # datetime.date(2021, 1, 20): 16954,
    # datetime.date(2021, 1, 20): 1956,
}

def job():
    s = requests.Session()
    today = datetime.date.today()
    nojamURL = "https://www.acmicpc.net/problem/" + str(problem_list[today])
    nojamRes = s.get(nojamURL)
    soup = BeautifulSoup(nojamRes.text, 'html.parser')
    제목 = soup.find('span', {'id': 'problem_title'})
    문제 = soup.find('div', {'id': 'problem_description'}).contents
    입력 = soup.find_all('div', {'id': 'problem_input'})
    샘플 = soup.find_all('pre', {'class': 'sampledata'})

    # print(문제, 입력, 샘플)
    print(f'문제: {문제}\n\n\n\n 입력: {입력}\n\n\n\n 샘플: {샘플}')
    #
    URL = "http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub&dum=dum&command2=getEmailList&searchName=김승진&searchBirth=19990806&memberSeq=247459929"
    res = s.get(URL)
    INFO = {'': ''}
    req = s.post("http://www.airforce.mil.kr:8081/user/emailPicEmailIntro.action", data=INFO)
    print(req.status_code)
    print(req.text)
    print("==================================================")
    LETTER_INFO = {'senderZipcode': '1234',
                   'senderAddr1': '서울시 강남구 논현동',
                   'senderAddr2': '논현역',
                   'senderName': '존예진',
                   'relationship': '백준봇',
                   'title': f'백준{problem_list[today]}번: {제목}',
                   'contents': f'손코딩 해서 보내면 컴파일 해서 알려줄게...\n 문제: {문제}\n\n\n\n 입력: {입력}\n\n\n\n 샘플: {샘플}',
                   'password': '1234'}
    req2 = s.post("http://www.airforce.mil.kr:8081/user/emailPicSaveEmail.action", LETTER_INFO)
    print(req2.status_code)
    print(req2.text)

schedule.add_job(job, 'interval', minutes=1440)
while True:
    time.sleep(1)
