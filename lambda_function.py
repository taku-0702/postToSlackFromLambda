import os
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
client = WebClient(os.environ["SLACK_BOT_TOKEN"])

def lambda_handler(event, context):
  api_response = client.chat_postMessage(
    channel="#practice",
    text="こんにちは"
  )
