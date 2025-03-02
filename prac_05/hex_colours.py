COLOR_TO_CODE = {"Aliceblue": "#f0f8ff", "Amaranth": "#e52b50", "Beaver": "#9f8170", "Bittersweet": "#fe6f5e",
                 "Black": "#000000", "Cadetblue": "#5f9ea0", "Cardinal": "#c41e3a", "Daffodil": "#ffff31",
                 "Dark Byzantium": "#5d3954", "Electric Lime": "#ccff00"}
color_name = input("Enter the name of the color: ").title()
while color_name != "":
    try:
        print(f"{color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color")
    color_name = input("Enter the name of the color: ").title()
