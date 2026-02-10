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

