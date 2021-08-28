# -*- coding: utf-8 -*-
import re
import urllib.request

from bs4 import BeautifulSoup

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


SLACK_TOKEN = ""
SLACK_SIGNING_SECRET = ""


app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
  #여기에 함수를 구현해봅시다.
  url = re.search(r'(https?://\S+)', text.split('|')[0]).group(0)
  
  sourcecode = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(sourcecode, "html.parser")
  
  keywords = []
  for naver_text in soup.find_all("span", class_="ah_k") :
    if not naver_text.get_text() in keywords :
      # 10위까지만 크롤링 하겠다
      if len(keywords) >= 10 :
        break
      keywords.append(naver_text.get_text())
  # 한글 지원을 위해 앞에 unicode u를 붙힙니다. 
  return u'\n'.join(keywords)


# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
  channel = event_data["event"]["channel"]
  text = event_data["event"]["text"]

  keywords = _crawl_naver_keywords(text)
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
