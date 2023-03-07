import os, sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from slack_sdk import WebClient
client = WebClient(os.environ["SLACK_BOT_TOKEN"])

def lambda_handler(event, context):
  if "channel" in event:
    channel = event['channel']
  else:
    logger.error("ERROR: specify slack channel.")
    sys.exit()
    
  if "text" in event:
    text = event["text"]
  else:
    logger.error("ERROR: specify text to post.")
    sys.exit()
  
  api_response = client.chat_postMessage(
    channel=channel,
    text=text
  )
  