#simple interest program
print('Welcome to the simple interest calculator')
principle = 1000
rate = 0.05
time = 3

P = int(principle)
R = float(rate)
T = int(time)
I = P * R * T

print(f"The simple interest is: {I}")