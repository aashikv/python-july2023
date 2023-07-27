import math

def find_area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = find_area_of_circle(radius)
    print(f"The area of the circle is: {area:.2f}")

if __name__ == "__main__":
    main()
