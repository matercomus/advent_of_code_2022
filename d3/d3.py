with open('/home/matt/Dev/advent_of_code_2023/d3/input.txt','r') as input:
    rucksacks = input.read().split('\n')[:-1]
    #print(rucksacks)

    def divide_into_compartments(rucksack):
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        return [first_half,second_half]

    def find_duplicates_in_rucksack(rucksack):
        rucksack = divide_into_compartments(rucksack)
        return set(rucksack[0]).intersection(rucksack[1])

    def find_duplicates_between_rucksacks(three_rucksacks):
        # Convert each rucksack to a set of characters
        rucksack_sets = [set(r) for r in three_rucksacks]

        # Find the intersection of all three sets
        duplicates = rucksack_sets[0]
        for rucksack_set in rucksack_sets[1:]:
            duplicates &= rucksack_set

        return duplicates


    def set_to_str(input):
        return ''.join(str(element)for element in input)

    def get_item_priority(item_type):
        # Get ASCII value of the character

        ascii_value = ord(set_to_str(item_type))

        # Calculate priority for lowercase and uppercase characters
        if 97 <= ascii_value <= 122:  # a-z
            priority = ascii_value - 96
        elif 65 <= ascii_value <= 90:  # A-Z
            priority = ascii_value - 38
        else:
            priority = 0

        return priority

    def p1():
        list_of_duplicates = []
        sum_priorities = 0
        for rucksack in rucksacks:
            duplicates = find_duplicates_in_rucksack(rucksack)
            list_of_duplicates.append(duplicates)
            sum_priorities += get_item_priority(duplicates)
        print(sum_priorities)

    def p2():
        sum_badge_priorities=0
        for rucksack in range(0, len(rucksacks),3):
            three_racksacks = rucksacks[rucksack:rucksack+3]
            badge = find_duplicates_between_rucksacks(three_racksacks)
            sum_badge_priorities += get_item_priority(badge)
            #print(three_racksacks,badge,get_item_priority(badge))
        print(sum_badge_priorities)


p1()
p2()