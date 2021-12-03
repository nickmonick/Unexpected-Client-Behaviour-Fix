import os
import asyncio
print("Tool made by ! Grim#1811")
username = os.environ['USERPROFILE']
local = "\AppData\Local\Roblox\\"
location = username + local
path = os.path.join(location, "GlobalBasicSettings_13.xml")
if os.path.exists(path):
    os.remove(path)
    print ("Success Fully Removed {path}")
else:
    print("File does not exist or has already been deleted")
asyncio.sleep(4)

