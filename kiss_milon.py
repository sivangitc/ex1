SEARCH = "1"
ADD = "2"
DELETE = "3"
EXIT = "4"


def get_choice() -> str:
    """Prints menu and returns user's choice"""
    print("1. Get word")
    print("2. Add word")
    print("3. Delete word")
    print("4. Exit")
    return input("Enter choice: ")


def search_word(milon: dict) -> None:
    """Prints translation of user's word from given dictionary"""
    word = input("Word to get: ")
    translate = milon.get(word, "")
    if translate:
        print(f"{word} means {translate}")
    else:
        print(f"The word {word} doesnt exist!")


def add_word(milon: dict) -> None:
    """Adds user's word and its translation to given dictionary"""
    word = input("Word to add: ")
    translate = input(f"Meaning of {word}: ")
    milon[word] = translate
    print(f"{word}={translate} was added.")


def delete_word(milon: dict) -> None:
    """Deletes user's word from given dictionary"""
    word = input("Word to delete: ")
    if word in milon:
        del milon[word]
        print(f"{word} has been erased")
    else:
        print("Word does not exist")


def main() -> None:
    milon: dict[str, str] = {}
    options = {SEARCH: search_word,
               ADD: add_word,
               DELETE: delete_word}
    choice = ""
    while choice != EXIT:
        choice = get_choice()
        if choice not in options:
            continue
        options[choice](milon)
    print("Goodbye!")


if __name__ == "__main__":
    main()
