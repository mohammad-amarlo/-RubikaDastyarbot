import datetime, json, os
from core.config import LOG_FILE

def log_event(event_type: str, content: str):
    """ثبت هر رخداد در فایل لاگ"""
    try:
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps({"time": t, "type": event_type, "content": content}, ensure_ascii=False) + "\n")
    except Exception as e:
        print("Log error:", e)
