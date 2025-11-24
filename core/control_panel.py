from rubka import Robot
from rubka.context import Message
from core.config import OWNER_ID, CREATOR_NAME_FA, PROJECT_VERSION
from datetime import datetime
import os, json, platform, psutil

def register_panel(bot: Robot):

    @bot.on_message(commands=["panel", "!panel"])
    def open_panel(bot: Robot, message: Message):
        if message.sender_id != OWNER_ID:
            return message.reply("🚫 دسترسی فقط برای مالک اصلی فعال است.")
        message.reply(
            f"🔐 RubikaDastyarbot Admin Panel v1.0\n"
            f"👑 Developer: {CREATOR_NAME_FA}\n"
            f"⚙️ Version: {PROJECT_VERSION}\n"
            "📋 دستورات:\n"
            "`/info_server`, `/users`, `/reload`, `/shutdown`"
        )

    @bot.on_message(commands=["info_server"])
    def info_server(bot: Robot, message: Message):
        if message.sender_id != OWNER_ID: return
        info = (
            f"💻 {platform.system()} {platform.release()}\n"
            f"CPU: {os.cpu_count()} cores\n"
            f"RAM: {round(psutil.virtual_memory().total / (1024**3),2)} GB\n"
            f"Time: {datetime.now():%Y-%m-%d %H:%M:%S}"
        )
        message.reply(info)

    @bot.on_message(commands=["users"])
    def users(bot: Robot, message: Message):
        if message.sender_id != OWNER_ID: return
        try:
            data = json.load(open("data/user_registry.json"))
            message.reply(f"👥 Users: {len(data)}")
        except:
            message.reply("⚠️ No registry file found.")

    @bot.on_message(commands=["reload"])
    def reload(bot: Robot, message: Message):
        if message.sender_id != OWNER_ID: return
        message.reply("♻️ Config reloaded successfully.")

    @bot.on_message(commands=["shutdown"])
    def shutdown(bot: Robot, message: Message):
        if message.sender_id != OWNER_ID: return
        message.reply("🔻 System shutting down...")
        os._exit(0)
