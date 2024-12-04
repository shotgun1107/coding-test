solved = {
    1: [11, "A B C D E F G H J L M"],
    2: [9, "A C E F G H I L M"],
    3: [9, "A C E F G H I L M"],
    4: [9, "A B C E F G H L M"]
}.get((N := int(input())), [8, "A C E F G H L M" if N < 10 else "A B C F G H L M"])

print(*solved, sep='\n')