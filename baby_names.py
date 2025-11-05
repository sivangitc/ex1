import os


def process_file(folder: str, filename: str) -> None:
    """gets most common boy and girl name from given file and prints them"""
    with open(os.path.join(folder, filename)) as f:
        line = f.readline()
    year = filename[len("baby"):].split(".")[0]

    print(f"most common boy name in {year} is {line.split(',')[1]}")
    print(f"most common girl name in {year} is {line.split(',')[2]}")


def main() -> None:
    folder = input("Enter path to directory of poll results: ")
    try:
        files = [file for file in os.listdir(folder) if file.startswith("baby")]
        for file in files:
            process_file(folder, file)

    except FileNotFoundError:
        print("Could not find your directory sorry bye")


if __name__ == "__main__":
    main()
