from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid(cl_args):
    if len(cl_args) <= 1:
        return False
    elif cl_args[1] == 0:
        return False
    elif cl_args[1].isdigit():
        return True
    else:
        return False

def encrypt(text, rot):
	'''takes str text and int rot
	returns caesar encrypted text by rot position'''
	newtext = []
	for char in text:
		newtext.append(rotate_character(char, rot))
	return "".join(newtext)
	
def main():
	if not user_input_is_valid(argv):
	    print("usage: python3 caesar.py n")
	    exit()
	message = input("Type a message: \n")
	print(encrypt(message, int(argv[1])))
	
if __name__ == "__main__":
	main()
