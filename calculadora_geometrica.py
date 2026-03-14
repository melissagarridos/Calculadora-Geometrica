# Melissa Garrido
pi = 3.14

print()
print("Welcome!")
print("This is a geometric calculator")
print()

calculator = input("Do you want to perform an operation? (yes / no): ").lower().strip()

while calculator == "yes":

    print()
    print("""Please select one option:
          - 2D
          - 3D
          - Exit""")
    print()

    choice = input("Write your choice: ").lower().strip()


    while choice == "2d":

        print("""You have the following options:
            1. Square
            2. Rectangle
            3. Triangle
            4. Circle
            5. Triangle Rectangle
            6. Go back""")
        
        shape = input("Choose a number: ").strip()

        try:
            shape = int(shape)

            if shape == 1:

                print("Square")

                try:
                    l = float(input("Please insert length: ").strip())
                    area = l ** 2
                    perimeter = 4 * l
                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 2:

                print("Rectangle")

                try:
                    l = float(input("Please insert length: ").strip())
                    w = float(input("Please insert width: ").strip())
                    perimeter = 2 * l + 2 * w
                    area = l * w
                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 3:

                print("Triangle")

                try:
                    a1 = float(input("Please insert angle 1: ").strip())
                    a2 = float(input("Please insert angle 2: ").strip())
                    b = float(input("Please insert base: ").strip())
                    h = float(input("Please insert height: ").strip())
                    area = (b * h) / 2
                    a3 = 180 - a1 - a2
                    hypotenuse = (b ** 2 + h ** 2) ** 0.5
                    perimeter = b + h + hypotenuse
                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Angle 3: ", a3)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 4:

                print("Circle")

                try:
                    r = float(input("Please insert radius: ").strip())
                    d = r * 2
                    area = pi * r ** 2
                    perimeter = 2 * pi * r
                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Diameter: ", d)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 5:

                print("Triangle Rectangle")

                try:
                    a1 = float(input("Please insert one angle: ").strip())
                    a2 = 90.0
                    b = float(input("Please insert base: ").strip())
                    h = float(input("Please insert height: ").strip())
                    area = (b * h) / 2
                    a3 = 180 - a1 - a2
                    hypotenuse = (b ** 2 + h ** 2) ** 0.5
                    perimeter = b + h + hypotenuse
                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Angle 1:", a1)
                    print("Angle 2:", a2)
                    print("Angle 3: ", a3)
                    print("Hypotenuse: ", hypotenuse)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 6:
                break

            else:
                print("Choose a valid option")
                continue

        except ValueError:
            print("Choose a valid option")
            continue
    
    while choice == "3d":

        print("3D")

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
                    surface_area = 6 * l ** 2
                    volume = l ** 3
                    print("Surface Area: ", surface_area)
                    print("Volume: ", volume)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 2:

                print("Sphere")

                try:
                    r = float(input("Please insert radius: ").strip())
                    area = 4 * pi * r ** 2
                    volume = (4/3) * pi * r ** 3
                    print("Surface Area: ", area)
                    print("Volume: ", volume)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 3:
                
                print("Cylinder")

                try:
                    r = float(input("Please insert radius: ").strip())
                    h = float(input("Please insert height: ").strip())
                    area = 2 * pi * r * (r + h)
                    volume = pi * r ** 2 * h
                    print("Surface Area: ", area)
                    print("Volume: ", volume)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 4:
                
                print("Rectangular Prism")

                try:
                    l = float(input("Please insert length: ").strip())
                    h = float(input("Please insert height: ").strip())
                    w = float(input("Please insert width: ").strip())
                    area = 2 * (l*w + l*h + w*h)
                    volume = l * w * h
                    print("Surface Area: ", area)
                    print("Volume: ", volume)
                    break

                except ValueError:
                    print("Insert a valid number")
                    continue

            elif shape == 5:
                break

            else:
                print("Choose a valid option")
                continue

        except ValueError:
            print("Choose a valid option")
            continue

    while choice == "exit":

        print("See you soon!")
        calculator = "no"
        break

    else: 
        continue

if calculator == "no":
    print("See you soon!")