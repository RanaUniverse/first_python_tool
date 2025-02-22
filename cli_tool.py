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
