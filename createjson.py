import json

x = {
  "Playing": [
    "Terraria",
    "Undertale",
    'Satisfactory',
    'ROBLOX',
    'Team Fortress 2',
    "Chess"],
    "Watching": [
        {"WindyTreeOfficial": "https://twitch.tv/windytreeofficial"}
    ],
    "Listening": [
        "Your Mother",
        "Skrillex"
    ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

f = open("activity.json", "w")
f.write(json.dumps(x, indent=4))
f.close()
