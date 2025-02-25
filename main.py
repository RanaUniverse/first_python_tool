from cli_tool import count_characters, count_bananas

print(
    "This is My Project. You can enter a sentence and "
    "I will send you the letter count."
)


# Main execution block
if __name__ == "__main__":
    print(
        "This is My Project. You can enter a sentence and "
        "I will process it based on your choice."
    )

    while True:
        print("\nChoose an option:")
        print("1 - Count Characters")
        print("2 - Count Bananas")
        print("Q - Quit")

        choice = input("Enter your choice: (1,2,Q)").strip().lower()

        if choice in ("1", "character", "char"):
            count_characters()
        elif choice in ("2", "banana", "bananas"):
            count_bananas()
        elif choice in ("q", "quit", "exit"):
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or Q to quit.")
