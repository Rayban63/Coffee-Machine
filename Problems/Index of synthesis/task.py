index = float(input())

if index < 2:
    print("Analytic")
elif 1 < index < 4:
    print("Synthetic")
else:
    print("Polysynthetic")
