def parse_map(main_file):
    lab_map = [list(line) for line in main_file.splitlines()]
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    # Locate the guard's position and facing direction
    for r, row in enumerate(lab_map):
        for c, cell in enumerate(row):
            if cell in directions:
                return lab_map, (r, c), cell
    raise ValueError("No guard found in the map.")

def turn_right(facing):
    turn_map = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return turn_map[facing]

def move_forward(position, facing, directions):
    r, c = position
    dr, dc = directions[facing]
    return r + dr, c + dc

def is_out_of_bounds(position, lab_map):
    r, c = position
    return r < 0 or c < 0 or r >= len(lab_map) or c >= len(lab_map[0])

def do_main_things(main_file):
    lab_map, guard_position, facing = parse_map(main_file)
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    visited = set()
    r, c = guard_position

    while True:
        if is_out_of_bounds((r, c), lab_map):
            break
        visited.add((r, c))
        dr, dc = directions[facing]
        next_r, next_c = r + dr, c + dc

        if is_out_of_bounds((next_r, next_c), lab_map) or lab_map[next_r][next_c] == '#':
            # Turn right if an obstacle is ahead or out of bounds
            facing = turn_right(facing)
        else:
            # Move forward
            r, c = next_r, next_c

    return len(visited)

def main():
    with open("day6-data.txt") as file:
        main_file = file.read()
    
    result = do_main_things(main_file)
    print(result)

if __name__ == "__main__":
    main()
