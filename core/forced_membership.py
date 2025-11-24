from rubka import Robot
from core.config import CHANNEL_GUID, BOT_TOKEN

bot = Robot(BOT_TOKEN)
def check_member(chat_id):
    try:
        return bot.check_join(CHANNEL_GUID, chat_id)
    except:
        return False
