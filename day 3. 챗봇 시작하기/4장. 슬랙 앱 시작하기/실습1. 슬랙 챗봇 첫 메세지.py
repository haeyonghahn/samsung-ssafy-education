# -*- coding: utf-8 -*-
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


# OAuth & Permissions로 들어가서
# Bot User OAuth Access Token을 복사하여 문자열로 붙여넣습니다
SLACK_TOKEN = ""
# Basic Information으로 들어가서
# Signing Secret 옆의 Show를 클릭한 다음, 복사하여 문자열로 붙여넣습니다
SLACK_SIGNING_SECRET = ""


app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
  # 슬랙 챗봇이 대답합니다.
  '''
  event_data = {
    'token': '', 
    'team_id': '', 
    'api_app_id': '', 
    'event': {
              'client_msg_id': '',
              'type': 'app_mention',
              'text': '',
              'user': '',
              ...
              'channel': ''
              },
    'type': ''
    }
  '''
  #print(event_data) 
  slack_web_client.chat_postMessage(
    channel=event_data["event"]["channel"],
    text="Hello, I am your chatbot!"
    # print(channel)
  )
    
# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
  return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
  app.run('0.0.0.0', port=8888)
