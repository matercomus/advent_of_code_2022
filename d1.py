with open("input.txt","r") as input:
    elfs = str.split(input.read(),'\n\n')

    elfs2 = []
    for elf in elfs:
       elfs2.append(elf.split()) 
    
    elfs3 = []
    for elf in elfs2:
        elfs3.append(list(map(int,elf)))
    
    elfs3sorted = sorted(elfs3, key=sum, reverse=True)
    
    #print(elfs3sorted[0])

    print("The elf carrying most calories is carrying: "+ str(sum(elfs3sorted[0])))

    top3elfs = elfs3sorted[:3]

    print("The top 3 elves are carrying: "+ str(sum([i for j in top3elfs for i in j])))