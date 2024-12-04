def count_xmas(grid_string):
    grid = [list(line) for line in grid_string.strip().split('\n')]
    rows, cols = len(grid), len(grid[0]) 
    count = 0  

    # helper function to check if a given MAS is forward or backward
    def is_mas(x, y, dx, dy):
        mas = "".join(grid[x + i * dx][y + i * dy] for i in range(3))
        return mas in {"MAS", "SAM"}  

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (is_mas(i - 1, j - 1, 1, 1) and  is_mas(i + 1, j - 1, -1, 1)    
            ):
                count += 1 

    return count

def main():
    """
    Reads the word search grid from a file, counts occurrences of X-MAS,
    and prints the result.
    """
    with open("day4-data.txt") as file:
        grid_content = file.read() 

    result = count_xmas(grid_content)

    print(result)

if __name__ == "__main__":
    main()
