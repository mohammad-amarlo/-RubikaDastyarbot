from rubka.adaptorrubka.client.client import Client

client = Client(session="OwnerSession", platform="web")

phone = input("📱 شماره روبیکای خود را بدون صفر وارد کنید (مثلاً 935xxxxxxx): ")

code_info = client.send_code(phone)
print("📩 کد تایید به روبیکا ارسال شد.")

code = input("🔑 کد تأیید را بنویس: ")

data = client.sign_in(phone, code_info["phone_code_hash"], code)
me = data["user"]

print("\n✅ GUID حساب شما (برای OWNER_ID):")
print(me["user_guid"])
