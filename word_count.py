import sys
from collections import Counter


def count_words(text):
    words = text.split()
    return len(words), Counter(words).most_common(5)


def main():
    if len(sys.argv) != 2:
        print("Usage: python word_count.py path/to/file.txt")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        text = f.read()

    total, top_words = count_words(text)
    print(f"Total words: {total}")
    print("Top 5 words:")
    for word, count in top_words:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
