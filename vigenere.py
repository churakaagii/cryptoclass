import string
import helpers

find_pos = helpers.alphabet_position
rotate_chr = helpers.rotate_character

def encrypt(text, cypher):
    # takes str text, str cypher
    # returns encrypted str of text in vigenere cypher
    newtext = []
    cyp_pos = 0
    for char in text:
        if find_pos(char) is not None:
            rot = find_pos(cypher[cyp_pos % len(cypher)])
            cyp_pos += 1
        newtext.append(rotate_chr(char, rot))
    return "".join(newtext)

def main():
    intext = input("Type a message: ")
    key = input("Encryption key: ")
    print(encrypt(intext, key))

if __name__ == "__main__":
    main()
