from fastapi import FastAPI
from core.config import BOT_TOKEN, PROJECT_VERSION, CREATOR_NAME_FA
from rubka import Robot
from core.control_panel import register_panel

app = FastAPI(title="RubikaDastyarbot 🎖 API")

@app.get("/")
async def root():
    return {
        "status": "active",
        "version": PROJECT_VERSION,
        "creator": CREATOR_NAME_FA
    }

bot = Robot(token=BOT_TOKEN)
register_panel(bot)
bot.run()
