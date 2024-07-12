def print_hexagon_pattern(rows, cols):
    def print_top_half():
        for col in range(cols):
            print("  __", end=" ")
        print()

    def print_middle_half(offset=False):
        for col in range(cols):
            if col == 0 and offset:
                print(" /  \\", end=" ")
            else:
                print("/  \\", end=" ")
        print()

    def print_bottom_half(offset=False):
        for col in range(cols):
            if col == 0 and offset:
                print(" \\__/", end=" ")
            else:
                print("\\__/", end=" ")
        print()

    for row in range(rows):
        if row % 2 == 0:
            print_top_half()
            print_middle_half()
            print_bottom_half()
        else:
            print("  ", end="")
            print_top_half()
            print("  ", end="")
            print_middle_half(offset=True)
            print("  ", end="")
            print_bottom_half(offset=True)
            
print("inputs: 4 7")
print_hexagon_pattern(4, 7)
print("\n inputs: 3 5")
print_hexagon_pattern(3, 5)
