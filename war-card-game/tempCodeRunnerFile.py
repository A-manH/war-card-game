):
    if str(rank) in deck:
        print(f"Rank {rank} exists")
        deck[str(rank)].append(1)
    else:
        deck.update({"1": []})

rank += 1
print(f"Completed Rank 1: {deck}")