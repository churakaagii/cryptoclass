import string

def alphabet_position(letter):
	# takes char letter
	# returns its position in the alphabet, regardless of caps
	if letter.isalpha():
		return string.ascii_lowercase.find(letter.lower())
	else:
		return None

def rotate_character(char, rot):
	# takes char char and int rot
	# returns new char based off new rot position in a caesar cypher
	currpos = alphabet_position(char)
	if currpos is not None:
		pos = (currpos + rot) % 26

	if char.islower():
		return string.ascii_lowercase[pos]
	elif char.isupper():
		return string.ascii_uppercase[pos]
	else:
		return char
