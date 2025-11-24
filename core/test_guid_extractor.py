from rubka.adaptorrubka.client.client import Client

def extract_guid(channel_guid):
    client = Client(session="RubikaTestSession", platform="web")
    members = client.get_all_members(channel_guid, just_get_guids=True)
    print("GUID Members:", members)

if __name__ == "__main__":
    extract_guid("c0XXXXXXX")
