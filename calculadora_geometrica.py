# Melissa Garrido

pi = 3.14

print("Welcome!")
print("This is a geometric calculator")

calculator = 0

while calculator == 0:

    print("""Posible options
          - 2D
          - 3D
          - Exit""")

    choice = input("Write your choice: ").lower().strip()

    if choice == "2d":

        print("""You have the following options:
            1. Square
            2. Rectangle
            3. Triangle
            4. Circle
            5. Triangle Rectangle
            6. Go back""")
        
        shape = input("Choose a number: ").strip()

        if shape.isdigit():

            shape = int(shape)

            if shape == 1:

                print("Square")

                l = input("Please insert length: ").strip()

                if l.isdigit():

                    l = float(l)

                    area = l ** 2

                    perimeter = 4 * l

                    print("Area: ", area)
                    print("Perimeter: ", perimeter)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 2:

                print("Rectangle")

                l = input("Please insert length: ").strip()

                w = input("Please insert width: ").strip()

                if l.isdigit() and w.isdigit():

                    l = float(l)

                    w = float(w)

                    area = 2 * l + 2 * w

                    perimeter = l * w

                    print("Area: ", area)
                    print("Perimeter: ", perimeter)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 3:

                print("Triangle")

                a1 = input("Please insert angle 1: ").strip()

                a2 = input("Please insert angle 2: ").strip()

                b = input("Please insert base: ").strip()

                h = input("Please insert height: ").strip()

                if a1.isdigit() and a2.isdigit() and b.isdigit() and h.isdigit():

                    a1 = float(a1)

                    a2 = float(a2)

                    b = float(b)

                    h = float(h)

                    area = (b * h) / 2

                    a3 = 180 - a1 - a2

                    perimeter = a1 + a2 + a3

                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Angle 3: ", a3)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 4:

                print("Circle")


                r = input("Please insert radius: ").strip()


                if r.isdigit():

                    r = float(r)

                    d = r * 2

                    area = pi * r ** 2

                    perimeter = 2 * pi * r

                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Diameter: ", d)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 5:

                print("Triangle Rectangle")

                a1 = input("Please insert one angle: ").strip()

                a2 = 90

                b = input("Please insert base: ").strip()

                h = input("Please insert height: ").strip()

                if a1.isdigit() and b.isdigit() and h.isdigit():

                    a1 = float(a1)

                    a2 = float(a2)

                    b = float(b)

                    h = float(h)

                    area = (b * h) / 2

                    a3 = 180 - a1 - a2

                    perimeter = a1 + a2 + a3

                    hypotenuse = (b ** 2 + h ** 2) ** 0.5

                    print("Area: ", area)
                    print("Perimeter: ", perimeter)
                    print("Angle 1", a1)
                    print("Angle 2", a2)
                    print("Angle 3: ", a3)
                    print("Hypotenuse: ", hypotenuse)
                
                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 6:
                continue

        else:
            print("Choose a valid option")
            continue

    elif choice == "3d":

        print("3D")

        print("""You have the following options:
            1. Cube
            2. Sphere
            3. Cylinder
            4. Rectangular Prism
            5. Go back""")
        
        shape = input("Choose a number: ").strip()

        if shape.isdigit():

            shape = int(shape)

            if shape == 1:

                print("Cube")

                l = input("Please insert length: ").strip()

                if l.isdigit():

                    l = float(l)

                    surface_area = 6 * l ** 2

                    volumen = l ** 3

                    print("Surface Area: ", surface_area)
                    print("Volumen: ", volumen)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 2:

                print("Sphere")

                r = input("Please insert radius: ").strip()

                if r.isdigit():

                    r = float(r)

                    area = 4 * pi * r ** 2

                    volume = (4/3) * pi * r ** 3

                    print("Surface Area: ", area)
                    print("Volume: ", volume)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 3:
                
                print("Cylinder")

                r = input("Please insert radius: ").strip()

                h = input("Please insert height: ").strip()

                if r.isdigit() and h.isdigit():

                    r = float(r)

                    h = float(h)

                    area = 2 * pi * r * (r + h)

                    volume = pi * r ** 2 * h

                    print("Surface Area: ", area)
                    print("Volume: ", volume)

                else:
                    print("Insert a valid digit")
                    continue


            elif shape == 4:
                
                print("Rectangular Prism")

                l = input("Please insert length: ").strip()

                h = input("Please insert height: ").strip()

                w = input("Please insert width: ").strip()

                if l.isdigit() and h.isdigit() and h.isdigit():

                    l = float(l)

                    h = float(h)

                    w = float(w)

                    area = 2 * (l*w + l*h + w*h)

                    volume = l * w * h

                    print("Surface Area: ", area)
                    print("Volume: ", volume)

                else:
                    print("Insert a valid digit")
                    continue

            elif shape == 5:
                continue

            else:
                print("Choose a valid option")
                continue
    
    elif choice == "exit":

        print("See you soon!")
        break


    else: 
        print("Choose a valid option")
        continue