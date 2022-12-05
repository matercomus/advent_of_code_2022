with open('input.txt','r') as input:
    rucksacks = input.read().split('\n')[:-1]
    #print(rucksacks)

    def divide_into_compartments(rucksack):
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        return [first_half,second_half]

    def find_duplicates(rucksack):
        pass
    print(rucksacks[0],divide_into_compartments(rucksacks[0]))