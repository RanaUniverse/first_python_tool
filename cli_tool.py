"""
Here i will keep my logic of the things
"""


def count_characters():
    user_input = input("Write any sentence here: ")
    total_len = len(user_input)
    output_sen = (
        f"Hello User, The number of character in this sentence is:\n" f"{total_len}"
    )
    print(output_sen)


def count_bananas():
    user_input = input("Write any sentence here: ")
    total_len = len(user_input)
    bananas = "🍌" * total_len  # Repeat the 🍌 emoji based on input length

    output_sen = (
        f"Hello User, The number of characters in this sentence is: {total_len}\n"
        f"Here are your bananas: \n{bananas}"
    )
    print(output_sen)


# Call the function
