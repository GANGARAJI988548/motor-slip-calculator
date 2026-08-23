# Motor Slip Calculator

synchronous_speed = float(input("Enter synchronous speed (RPM): "))
rotor_speed = float(input("Enter rotor speed (RPM): "))

if synchronous_speed <= 0 or rotor_speed < 0:
    print("Please enter valid speed values.")
else:
    slip = (synchronous_speed - rotor_speed) / synchronous_speed
    slip_percentage = slip * 100

    print(f"Slip = {slip_percentage:.2f}%")
