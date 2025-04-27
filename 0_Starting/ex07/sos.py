import sys

def main():
	morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
	try:
		if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
			raise AssertionError("the arguments are bad")
		input_str = sys.argv[1]
		complete_morse_list = []
		for c in input_str.upper():
			if c in morse_code_dict:
				complete_morse_list.append(morse_code_dict[c])
			else:
				raise AssertionError("the arguments are bad")
		print(' '.join(complete_morse_list))
	except AssertionError as e:
		print("AssertionError:", e)
	except Exception as e:
		print(f"{e.__class__.__name__}:", e)

if __name__ == "__main__":
    main()
