import keyboard
keyboard.play(rk,speed_factor=10)


rk=keyboard.record(until="shift")
print(rk)