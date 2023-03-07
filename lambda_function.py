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
    api_response = client.chat_postMessage(
      channel=channel,
      text=text
    )
  elif "blocks" in event:
    blocks = event["blocks"]
    api_response = client.chat_postMessage(
      channel=channel,
      blocks=blocks
    )
  else:
    logger.error("ERROR: specify text to post.")
    sys.exit()

  