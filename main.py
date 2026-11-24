import os

LINE_1 = "A traffic jam is a parking lot that forgot it was a road, where a hundred cars burn fuel just to stand still."
LINE_2 = "It works because both are full of cars going nowhere and burning fuel, but it leaves out the honking: nobody in a jam chose to stop, they are all still trying to leave."

TEXT = LINE_1 + "\n" + LINE_2


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
