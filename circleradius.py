def find_radius_from_diameter(diameter):
    radius = diameter / 2
    return radius

def main():
    diameter = float(input("Enter the diameter of the circle: "))
    radius = find_radius_from_diameter(diameter)
    print(f"The radius of the circle is: {radius}")

if __name__ == "__main__":
    main()
