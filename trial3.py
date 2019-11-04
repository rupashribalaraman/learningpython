# Python program to calculate the area or volume of user-selected shape
import math


class Calculate():
    def __init__(self, l=0.0, b=0.0, h=0.0, r=0.0, ba=0.0, area=0.0, volume=0.0):
        self.l = l
        self.b = b
        self.h = h
        self.r = r
        self.ba = ba
        self.area = 0.0
        self.volume = 0.0

    def user_input(self):
        print("Which of the following shapes do you want to calculate area or volume for?")
        print("1.Square")
        print("2.Rectangle")
        print("3.Circle")
        print("4.Sphere")
        print("5.Cylinder")
        print("6.Hemisphere")
        print("7.Cone")
        print("8.Triangle")
        print("9.Parallelogram")
        print("10.Rhombus")
        print("Type the respective number of your shape of choice")
        choice1 = int(input())

        print("Type area or volume")
        choice2 = input()

        if choice1 == 1:
            self.l = float(input("Enter the length of the side:"))
            if choice2 == "area":
                self.area = self.l * self.l
                print("Area of the square is %d" % self.area)
            else:
                self.volume = self.l * self.l * self.l
                print("Volume of the square is %d" % self.volume)

        elif choice1 == 2 | 9 | 10:
            self.l = float(input("Enter the length: "))
            self.b = float(input("Enter the breadth:"))
            self.h = float(input("Enter the height: "))
            if choice2 == "area":
                self.area = self.l * self.b
                print("Area of the rectangle is %d" % self.area)
            else:
                volume = self.l * self.b * self.h
                print("The volume of the rectangle is %d" % volume)
        elif choice1 == 3:
            self.r = float(input("Enter the radius: "))
            if choice2 == "area":
                self.area = 3.142 * self.r * self.r
                print("Area of a circle is %d" % self.area)
            else:
                print("Sorry, we cannot calculate the volume of a square since it is two dimensional :/ %d")
        elif choice1 == 4:
            self.r = float(input("Enter the radius"))
            if choice2 == "area":
                self.area = 4 * 3.142 * self.r * self.r
                print("The area of the sphere is %d" % self.area)
            else:
                self.volume = (self.area * self.r) / 3
                print("The volume of the sphere is %d" % self.volume)
        elif choice1 == 5:
            self.r = float(input("Enter the radius: "))
            self.h = float(input("Enter the height: "))
            if choice2 == "area":
                self.area = (2 * 3.142 * self.r * self.h) + (2 * 3.142 * self.r * self.r)
                print("The area of the cylinder is %d" % self.area)
            else:
                self.volume = 3.142 * self.r * self.r * self.h
                print("The volume of the cylinder is %d" % self.volume)
        elif choice1 == 6:
            self.r = float(input("Enter the radius: "))
            if choice2 == "area":
                self.area = 2 * 3.142 * self.r * self.r
                print("The area of the hemisphere: %d" % self.area)
            else:
                self.volume = (self.area * self.r) / 3
                print("The volume of the hemisphere is %d" % self.volume)
        elif choice1 == 7:
            self.r = float(input("Enter the radius: "))
            self.h = float(input("Enter the height: "))
            if choice2 == "area":
                x = math.sqrt(self.h * self.h + self.r * self.r)
                y = self.r + x
                self.area = 3.142 * self.r * (y)
                print("The area of the cone is %d" % self.area)
            else:
                self.volume = (3.142 * self.r * self.r * self.h) / 3
                print("The volume of the cone is %d" % self.volume)
        elif choice1 == 8:
            self.h = float(input("Enter the height: "))
            self.ba = float(input("Enter the base length: "))
            if choice2 == "area":
                self.area = (self.ba * self.h) / 2
                print("The area of the triangle is %d" % self.area)
            else:
                self.volume = self.area * self.h
                print("The volume of the triangle is %d" % self.volume)


a1 = Calculate()
a1.user_input()
