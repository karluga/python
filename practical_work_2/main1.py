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
    full_pattern = [line + line[::-1][1:] for line in vertical_mirrored] 
    
    for line in full_pattern:
        print(line)

print_full_star_8_vertical()