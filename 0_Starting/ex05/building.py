import sys


def main():
    """
    This program takes a single string argument
    and isplays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces.
    """
    str_input = ""
    str_length = 0

    try:
        if len(sys.argv) < 2:
            str_input = input("What is the text to count?\n")
            str_input += "\n"
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            str_input = sys.argv[1]
    except AssertionError as e:
        print("AssertionError:", e)
        exit()

    str_length = len(str_input)
    upper_cnt = 0
    lower_cnt = 0
    punc_cnt = 0
    space_cnt = 0
    digit_cnt = 0
    for s in str_input:
        if s.isupper():
            upper_cnt += 1
        elif s.islower():
            lower_cnt += 1
        elif s in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punc_cnt += 1
        elif s.isspace():
            space_cnt += 1
        elif s.isdigit():
            digit_cnt += 1
    print(f"The text contains {str_length} characters:")
    print(f"""{upper_cnt} upper letters
{lower_cnt} lower letters
{punc_cnt} punctuation marks
{space_cnt} spaces
{digit_cnt} digits""")


if __name__ == "__main__":
    main()
