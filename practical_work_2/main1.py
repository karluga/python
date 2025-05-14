pattern = [
    "           *",
    "           *",
    "           *",
    "         ***",
    "*      *    ",
    "  *  *  ****",
    "    *  *****",
    "   * ****   ",
    "   * ****   ",
    "    * ******",
    "     *  ****",
]

def print_full_star_8_vertical():
    vertical_mirrored = pattern + pattern[-2::-1]
    
    # Mirror the combined shape on X-axis
    full_pattern = []
    for line in vertical_mirrored:
        full_pattern.append(line + line[::-1][1:])
    
    for line in full_pattern:
        print(line)

print_full_star_8_vertical()