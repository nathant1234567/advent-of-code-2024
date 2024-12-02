def main():
    def is_safe(levels):
        """Check if a sequence of levels is safe."""
        differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
        return (
            all(1 <= diff <= 3 for diff in differences) or
            all(-3 <= diff <= -1 for diff in differences)
        )
    
    safe_count = 0
    with open("day2-data.txt") as file:
        for line in file:
            levels = list(map(int, line.split()))
            
            # Check if the report is safe as-is
            if is_safe(levels):
                safe_count += 1
                continue

            # Try removing each level and check if it's safe
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i+1:]
                if is_safe(modified_levels):
                    safe_count += 1
                    break  # Stop checking after finding one valid removal

    print(f"Number of safe reports: {safe_count}")


if __name__ == "__main__":
    main()
