Maximum = 100.00
Minimum = 0.00
Sensitivity = 100.00
ftime = True

while True:
    n = input().lower()
    if n=='d':
        print(f"{Sensitivity:.2f}?")
        print(f"Your sensitivity is {Sensitivity:.2f}.")
        break
    if n=='s' and ftime:
        print(f"{Sensitivity:.2f}?")
        Minimum = Sensitivity
        Maximum = Maximum*2
        Sensitivity = Maximum
        ftime = False
    elif n=='s':
        print(f"{Sensitivity:.2f}?")
        OldMinimum = Minimum
        Minimum = Sensitivity
        Maximum = Maximum - (Maximum-OldMinimum)/2
        Sensitivity = Maximum
    elif n=='f':
        oldMaximum = Maximum
        print(f"{Sensitivity:.2f}?")
        Maximum = Minimum
        Minimum = Maximum
        Minimum += (oldMaximum-Minimum)/2
        Sensitivity = Minimum
