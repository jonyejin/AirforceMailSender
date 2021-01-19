import requests
import json
from bs4 import BeautifulSoup

s = requests.Session()
URL = "http://www.airforce.mil.kr:8081/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub&dum=dum&command2=getEmailList&searchName=김승진&searchBirth=19990806&memberSeq=247459929"
res = s.get(URL)
# soup = BeautifulSoup(res.text, 'html.parser')
# 인터넷편지쓰기버튼 = soup.find('input', {'value': "인터넷 편지쓰기"})
# emailFormAction = soup.find('form', {'name': 'emailForm'})
# command2 = soup.find('input', {'name': 'command2'})
# command2["value"] = "writeEmail"
# emailFormAction["action"] = "/user/emailPicEmailIntro.action"
# # print(emailFormAction)
INFO = {'':''}
req = s.post("http://www.airforce.mil.kr:8081/user/emailPicEmailIntro.action", data=INFO)
print(req.status_code)
print(req.text)
print("==================================================")
LETTER_INFO = {'senderZipcode':'1234',
               'senderAddr1': '서울시 강남구 논현동',
               'senderAddr2':'논현역',
               'senderName': '존예진',
               'relationship': '컴공여신',
               'title': '이거 배포는 어케 하면 좋을까',
               'contents': '24시간 돌릴 수 있는 서버가 있나?',
               'password': '1234'}
req2 = s.post("http://www.airforce.mil.kr:8081/user/emailPicSaveEmail.action", LETTER_INFO)
print(req2.status_code)
print(req2.text)