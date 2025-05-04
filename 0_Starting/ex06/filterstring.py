import sys
from ft_filter import ft_filter


def main():
    """
    This programs takes two arguments.
    The program outputs a list of words from S
    that have a length greater than N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        word_list = sys.argv[1].split()
        length = 0
        try:
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(lambda word: len(word) > length, word_list)))
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)


if __name__ == "__main__":
    main()
