def count_xmas(grid_string):
    grid = [list(line) for line in grid_string.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # directions for row and column offsets
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Horizontal left (reverse)
        (-1, 0), # Vertical up (reverse)
        (-1, -1),# Diagonal up-left (reverse)
        (-1, 1)  # Diagonal up-right (reverse)
    ]

    def is_valid(x, y):
        """Check if the position is within the grid."""
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        """Check if the word can be found starting at (x, y) in direction (dx, dy)."""
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    # iterate over every position in the grid
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if find_word(i, j, dx, dy):
                    count += 1

    return count

def main():
    with open("day4-data.txt") as file:
        grid_content = file.read()
        result = count_xmas(grid_content)

    print(result)

if __name__ == "__main__":
    main()
