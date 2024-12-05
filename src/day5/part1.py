def seperate_sections(file):
    sections = file.strip().split("\n\n")

    section1 = sections[0].strip().split("\n")
    section2 = sections[1].strip().split("\n")

    return section1, section2

def parse_rules(rules_section):
    rules = []
    for line in rules_section:
        x, y = line.split('|')
        rules.append((int(x), int(y)))
    return rules

def is_update_ordered(update, rules):
    page_positions = {page: index for index, page in enumerate(update)} # so [75, 47, 61, 53, 29] would create {75: 0, 47: 1, 61: 2, 53: 3, 29: 4}
    print(page_positions)

    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:
                return False
            
    return True

def get_middle_page(update):
    mid_index = len(update) // 2 # this was the easiest bit lmao
    return update[mid_index]

def parse_data(sec1, sec2):
    rules = parse_rules(sec1)

    total_middle_sum = 0
    for line in sec2:
        update = list(map(int,line.split(","))) # parse into ints
        if is_update_ordered(update, rules):
            total_middle_sum += get_middle_page(update)

    return total_middle_sum

def main():
    with open("day5-data.txt") as file:
        main_file = file.read()

    sec1, sec2 = seperate_sections(main_file)
    result = parse_data(sec1, sec2)

    print(result)

if __name__ == "__main__":
    main()
