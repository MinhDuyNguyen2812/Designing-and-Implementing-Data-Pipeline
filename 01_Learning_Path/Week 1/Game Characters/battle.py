def simulate_battle(characters):
    print("\n--- Battle Start ---")
    for char in characters:
        char.attack()
        char.defend()
    print("--- Battle End ---\n")