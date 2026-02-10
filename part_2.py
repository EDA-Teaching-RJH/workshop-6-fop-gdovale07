rover_status = {
    "battery": 100,
    "heater": "off",
    "camera": "standby"

}

print(rover_status["battery"])

rover_status["battery"] = 85
rover_status["heater"] = "on"
rover_status["speed"] = 5

print(rover_status)

mission_log = [
    {"site": "crater a", "radiation": "low", "water": False},
    {"site": "dune b", "radiation": "high", "water": True}
]

for site in mission_log:
    print(f"site {site['site']} has {site['radiation']} radiation.")
    