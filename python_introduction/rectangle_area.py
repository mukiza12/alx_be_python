#area of a rectangle
while True:
     length = 10
     width = 5
     try:
        length_i = float(length)
        width_i = float(width)
     except ValueError:
         print('invalid input')
         continue
     print("let's continue")

     area = float(length_i * width_i)

     print(f"the area is: {area}")
     break





