"""
1. The Smart Warehouse (Security & Temperature)
You are programming a climate-controlled warehouse. You have three inputs: sensor_active (bool), internal_temp (float), and emergency_override (bool).
Your job is to decide the system status.
The system should only check the temperature if the sensor is actually active.
If the sensor is off, the system is "Offline," unless the override is on (then it's "Manual").
If the sensor is on, the temperature determines if it's "Optimal," "Warning," or "CRITICAL."
Goal: Print the final system status.
"""
sensor = str(input("Is sensor working(Y/N): "))
sensor_active = sensor.lower() == "y"
override = str(input("Is it on Emergency override?(Y/N): "))
emergency_override = override.lower() == "y"

if sensor_active:
    internal_temp = float(input("enter temperature: "))
    if 10 <= internal_temp <= 30:
        print("Optimal")
    elif 0 <= internal_temp <= 40:
        print("warning!")
    else:
        print("CRITICAL!!!")
elif emergency_override:
    print("System in Emergency oevrride mode!!!")
else:
    print("System is offline!")