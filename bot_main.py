from fastapi import FastAPI, Request
import requests, json, traceback
from core.config import BOT_TOKEN, WEBHOOK_URL, OWNER_ID, DEBUG_MODE
from modules.ai_features_placeholder import ai_response
from core.role_manager import get_role
from modules.event_logger import log_event

app = FastAPI()

# =====================================================
# Rubika Dastyarbot – v0.4-alpha (AI Bridge ready)
# Author: Mohammad_Amarloo
# =====================================================

def send_message(chat_id, text):
    """ارسال پیام متنی به گفت‌وگو"""
    try:
        url = "https://messengerg2c60.iranlms.ir/v1/sendMessage"
        payload = {"object_guid": chat_id, "rnd": "msg", "text": text}
        headers = {"Content-Type": "application/json"}
        requests.post(url, json=payload, headers=headers)
    except Exception as e:
        log_event("send_error", str(e))

@app.get("/")
async def root():
    return {"status": "Rubika Dastyarbot v0.4-alpha online"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        msg = data.get("data", {}).get("message", {})
        text = msg.get("text", "")
        chat_id = msg.get("object_guid")
        user_guid = msg.get("author_object_guid")

        # نقش کاربر
        role = get_role(user_guid)

        # فرمان‌ها
        if text == "help":
            send_message(chat_id, "⚙️ دستورات:\nhelp | info | ai <سؤال> | role\n")
        elif text == "info":
            send_message(chat_id, "🤖 Rubika Dastyarbot v0.4-alpha فعال است ✅")
        elif text.startswith("ai "):
            q = text.replace("ai ", "")
            answer = ai_response(q)
            send_message(chat_id, f"🧠 پاسخ خودکار:\n{answer}")
        elif text == "role":
            send_message(chat_id, f"👤 نقش شما: {role}")
        else:
            send_message(chat_id, "❔ دستور ناشناخته — استفاده کن از 'help'")

        # ثبت رخداد
        log_event("message", f"{user_guid}:{text}")
        return {"ok": True}
    except Exception as e:
        if DEBUG_MODE:
            traceback.print_exc()
        log_event("webhook_error", str(e))
        return {"ok": False, "error": str(e)}
