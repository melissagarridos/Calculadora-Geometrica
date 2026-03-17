## Melissa Garrido
pi = 3.14


print()
print("Welcome!")
print("This is a geometric calculator")
print()

calculator = False

while not calculator:

    print()
    print("""Please select one option:
        - 2D
        - 3D
        - Units
        - Exit""")
    print()

    choice = input("Write your choice: ").lower().strip()


    while choice == "2d":

        print("""You have the following options:
            1. Square
            2. Rectangle
            3. Circle
            4. Right Triangle 
            5. Go back""")
        
        shape = input("Choose a number: ").strip()

        try:
            shape = int(shape)

            if shape == 1:

                print("Square")

                try:
                    l = float(input("Please insert length: ").strip())
                    if l > 0:
                        area = l ** 2
                        perimeter = 4 * l
                        print("Area: ", round(area,2))
                        print("Perimeter: ", round(perimeter,2))
                        choice = "back"
                    else:
                        print("Insert valid number")
                        continue

                except ValueError:
                    print("Insert valid number")
                    continue
                

            elif shape == 2:

                print("Rectangle")

                try:
                    
                        l = float(input("Please insert length: ").strip())
                        w = float(input("Please insert width: ").strip())

                        if l > 0 and w > 0:
                            perimeter = 2 * l + 2 * w
                            area = l * w
                            print("Area: ", round(area,2))
                            print("Perimeter: ", round(perimeter,2))
                            choice = "back"

                        else:
                            print("Insert valid number")                                
                            continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 3:

                print("Circle")

                try:
                    r = float(input("Please insert radius: ").strip())
                    if r > 0:
                        d = r * 2
                        area = pi * r ** 2
                        perimeter = 2 * pi * r
                        print("Area: ", round(area,2))
                        print("Perimeter: ", round(perimeter,2))
                        print("Diameter: ", round(d,2))
                        choice = "back"

                    else:
                            print("Insert valid number")
                            continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 4:

                print("Right Triangle")

                try:
                    
                    a1 = float(input("Please insert one angle: ").strip())
                    a2 = 90.0
                    b = float(input("Please insert base: ").strip())
                    h = float(input("Please insert height: ").strip())
                    if 90 > a1 > 0 and a2 > 0 and b > 0 and h > 0:

                        area = (b * h) / 2
                        a3 = 180 - a1 - a2
                        hypotenuse = (b ** 2 + h ** 2) ** 0.5
                        perimeter = b + h + hypotenuse
                        print("Area: ", round(area,2))
                        print("Perimeter: ", round(perimeter,2))
                        print("Angle 1:", a1)
                        print("Angle 2:", a2)
                        print("Angle 3: ", a3)
                        print("Hypotenuse: ", round(hypotenuse,2))
                    
                    else:
                        print("Insert valid number")
                        continue
                    
                    choice = "back"

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 5:
                choice = "back"

            else:
                print("Choose valid option")
                continue

        except ValueError:
            print("Choose valid option")
            continue
    
    while choice == "3d":

        print("""You have the following options:
            1. Cube
            2. Sphere
            3. Cylinder
            4. Rectangular Prism
            5. Go back""")
        
        shape = input("Choose a number: ").strip()

        try:
            shape = int(shape)

            if shape == 1:

                print("Cube")

                try:
                    l = float(input("Please insert length: ").strip())
                    if l > 0:
                        area = 6 * l ** 2
                        volume = l ** 3
                        print("Surface Area: ", round(area,2))
                        print("Volume: ", round(volume,2))
                        choice = "back"

                    else:
                        print("Insert valid number")
                        continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 2:

                print("Sphere")

                try:
                    r = float(input("Please insert radius: ").strip())
                    if r > 0:
                        area = 4 * pi * r ** 2
                        volume = (4/3) * pi * r ** 3
                        print("Surface Area: ", round(area,2))
                        print("Volume: ", round(volume,2))
                        choice = "back"
                    else:
                        print("Insert valid number")
                        continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 3:
                
                print("Cylinder")

                try:
                    r = float(input("Please insert radius: ").strip())
                    h = float(input("Please insert height: ").strip())

                    if r > 0 and h > 0:
                        area = 2 * pi * r * (r + h)
                        volume = pi * r ** 2 * h
                        print("Surface Area: ", round(area,2))
                        print("Volume: ", round(volume,2))
                        choice = "back"

                    else:
                        print("Insert valid number")
                        continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 4:
                
                print("Rectangular Prism")

                try:
                    l = float(input("Please insert length: ").strip())
                    h = float(input("Please insert height: ").strip())
                    w = float(input("Please insert width: ").strip())

                    if l > 0 and h > 0 and w > 0:
                        area = 2 * (l*w + l*h + w*h)
                        volume = l * w * h
                        print("Surface Area: ", round(area,2))
                        print("Volume: ", round(volume,2))
                        choice = "back"

                    else:
                        print("Insert valid number")
                        continue

                except ValueError:
                    print("Insert valid number")
                    continue

            elif shape == 5:
                choice = "back"

            else:
                print("Choose a valid option")
                continue

        except ValueError:
            print("Choose a valid option")
            continue

    while choice == "units":

        print()
        print("""Length converter - Please select one option:
            1. Inches
            2. Feet
            3. Yards
            4. Miles
            5. Go back""")

        from_unit = input("Convert from: ").strip()

        try:
            from_unit = int(from_unit)

            if from_unit in [1, 2, 3, 4]:

                try:
                    value = float(input("Enter value: ").strip())
                    if value < 0:
                        print("Insert valid number")
                        continue

                    # Convert everything to inches first
                    if from_unit == 1:
                        in_inches = value
                    elif from_unit == 2:
                        in_inches = value * 12
                    elif from_unit == 3:
                        in_inches = value * 36
                    elif from_unit == 4:
                        in_inches = value * 63360

                    print()
                    print("Results:")
                    print("Inches:", round(in_inches, 4))
                    print("Feet:  ", round(in_inches / 12, 2))
                    print("Yards: ", round(in_inches / 36, 2))
                    print("Miles: ", round(in_inches / 63360, 2))
                    choice = "back"

                except ValueError:
                    print("Insert valid number")
                    continue

            elif from_unit == 5:
                choice = "back"

            else:
                print("Choose valid option")
                continue

        except ValueError:
            print("Choose valid option")
            continue

    if choice == "exit":

        break

    else: 
        continue

if calculator == False:
    print("See you soon!")