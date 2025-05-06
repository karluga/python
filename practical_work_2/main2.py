pattern_params = [
    (11, 1),
    (11, 1),
    (11, 1),
    (9, 3),
    (0, 1, 6, 1, 4),
    (2, 1, 2, 1, 2, 4),
    (4, 1, 2, 5),
    (3, 1, 1, 4, 3),
    (3, 1, 1, 4, 3),
    (4, 1, 1, 6),
    (5, 1, 2, 4),
]

def generate_pattern(params):
    pattern = []
    for param in params:
        line = ''
        i = 0
        while i < len(param):
            if i % 2 == 0:
                line += ' ' * param[i]
            else:
                line += '*' * param[i]
            i += 1
        pattern.append(line)
    return pattern

def print_full_star_8_vertical():
    pattern = generate_pattern(pattern_params)
    
    vertical_mirrored = pattern + pattern[-2::-1] 
    
    full_pattern = [line + line[::-1][1:] for line in vertical_mirrored] 
    
    for line in full_pattern:
        print(line)

print_full_star_8_vertical()