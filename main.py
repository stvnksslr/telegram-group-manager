# settings.py
import os

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
################################################
channel_username = os.getenv('CHANNEL_USERNAME')
################################################

client = TelegramClient('session_name', api_id, api_hash)

assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

# ---------------------------------------
offset = 0
limit = 200
my_filter = ChannelParticipantsSearch('')
all_participants = []
while_condition = True
# ---------------------------------------
channel = client(GetFullChannelRequest(channel_username))
while while_condition:
    participants = client(
        GetParticipantsRequest(channel=channel_username, filter=my_filter, offset=offset, limit=limit, hash=0))
    all_participants.extend(participants.users)
    offset += len(participants.users)
    if len(participants.users) < limit:
        while_condition = False
