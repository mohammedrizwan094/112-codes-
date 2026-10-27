"""Problem 041: Clock Angle : Given hour and minute, calculate the smaller angle between the two hands."""

hour = int(input("Enter hour (0-23): ")) % 12
minute = int(input("Enter minute (0-59): "))
if not 0 <= minute <= 59:
    print("Invalid minute")
else:
    hour_angle = hour * 30 + minute * 0.5
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    print("Smaller angle:", min(angle, 360 - angle), "degrees")
