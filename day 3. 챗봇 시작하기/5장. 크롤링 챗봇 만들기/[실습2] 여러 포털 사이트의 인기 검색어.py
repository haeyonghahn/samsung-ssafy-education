# -*- coding: utf-8 -*-
import re
import urllib.request

from bs4 import BeautifulSoup

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


SLACK_TOKEN = "xoxb-675155583329-683378410599-1VlHmmJv29rq6LbYtvzAg2jN"
SLACK_SIGNING_SECRET = "65c4f9e8b51a7306120d438c36aaa58e"


app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


# 크롤링 함수 구현하기
def _crawl_portal_keywords(text):
    
  url = re.search(r'(https?://\S+)', text.split('|')[0]).group(0)
  sourcecode = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(sourcecode, "html.parser")
  
  #함수를 구현해 주세요
  keywords = []
  if "naver" in url :
    for naver_text in soup.find_all("span", class_="ah_k") :
      if not naver_text.get_text() in keywords :
        if len(keywords) >= 10 :
          break
        keywords.append(naver_text.get_text())
  elif "daum" in url :
    for daum_text in soup.find_all("a", class_="link_issue") :
      # if not을 사용해보면 class_="link_issue를 우리가 원하는 
      # 데이터 외에 다른 곳에 link_issue가 있어서 if not을 사용하여
      # 데이터가 중복되는 것을 방지하기 위해서이다.
      if not daum_text.get_text() in keywords :
        if len(keywords) >= 10 :
          break
        keywords.append(daum_text.get_text())
          
  # 한글 지원을 위해 앞에 unicode u를 붙혀준다.
  return u'\n'.join(keywords)

# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
  channel = event_data["event"]["channel"]
  text = event_data["event"]["text"]

  keywords = _crawl_portal_keywords(text)
  slack_web_client.chat_postMessage(
      channel=channel,
      text=keywords
  )


# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
  return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
  app.run('0.0.0.0', port=8888)
