def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    apple_positions = [a + d for d in apples]
    
    orange_positions = [b + d for d in oranges]

    
    apples_in_house = sum(1 for pos in apple_positions if s <= pos <= t)
    
    oranges_in_house = sum(1 for pos in orange_positions if s <= pos <= t)

    
    print(apples_in_house)
    print(oranges_in_house)

