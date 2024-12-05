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
    page_positions = {page: index for index, page in enumerate(update)}

    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:
                return False

    return True


def get_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]


def order(inordered, rules):
    precedence = {page: set() for page in inordered}

    for x, y in rules:
        if x in inordered and y in inordered:
            precedence[y].add(x)

    return sorted(inordered, key=lambda page: len(precedence[page]))


def parse_data(sec1, sec2):
    rules = parse_rules(sec1)

    sum_middle_pages = 0
    for line in sec2:
        update = list(map(int, line.split(",")))  # Parse update into integers
        if not is_update_ordered(update, rules):
            corrected_update = order(update, rules)
            sum_middle_pages += get_middle_page(corrected_update)

    return sum_middle_pages


def main():
    with open("day5-data.txt") as file:
        main_file = file.read()

    sec1, sec2 = seperate_sections(main_file)
    result = parse_data(sec1, sec2)

    print(result)


if __name__ == "__main__":
    main()
