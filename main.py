import os
username = os.environ['USERPROFILE']
local = "\AppData\Local\Roblox\\"
location = username + local
path = os.path.join(location, "GlobalBasicSettings_13.xml")
print (path)
os.remove(path)
