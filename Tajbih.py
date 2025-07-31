def tasbih_counter():
    count = 0
    while True:
        print(f"\n Current Count: {count}")
        print("Press [Enter] to count, type 'r' to reset, 'q' to quit.")
        user_input = input(">> ").lower()

        if user_input == "":
            count += 1
        elif user_input == "r":
            count = 0
            print(" Counter reset to 0.")
        elif user_input == "q":
            print(f" Exiting... Final count: {count}")
            break
        else:
            print(" Invalid input. Use only [Enter], 'r' or 'q'.")

tasbih_counter()


