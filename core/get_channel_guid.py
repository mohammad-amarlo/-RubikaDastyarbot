from rubka.adaptorrubka.client.client import Client

client = Client(session="ChannelSession", platform="web")
channel_link = input("🔗 لینک کانالت (مثلاً rubika.ir/MohammadAmmarlu): ")

guid = client.methods.network.request(
    method="getObjectByUsername",
    input={"username": channel_link.split("/")[-1]},
    tmpSession=True
)["object"]["object_guid"]

print("\n✅ GUID کانال شما (برای CHANNEL_GUID):")
print(guid)
