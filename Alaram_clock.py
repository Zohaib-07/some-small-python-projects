import time
from datetime import datetime

def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM:SS) in 24-hour format: ")
        
  
    #The datetime.strptime function successfully parses this input into a datetime.time object.
    valid_time = datetime.strptime(alarm_time, "%H:%M:%S").time()  
    print(f"Alarm set for {valid_time}")
    return valid_time


alarm_time = set_alarm()
if alarm_time is None:
    print(f"Alarm set for {alarm_time}")

while True:
        # Get the current time
        current_time = datetime.now().time()
        
        # Check if the current time matches the alarm time
        if current_time >= alarm_time:
            print("Time's up! The alarm is ringing!")
            break
        
        # Sleep for a short amount of time to avoid excessive CPU usage
        time.sleep(1)


