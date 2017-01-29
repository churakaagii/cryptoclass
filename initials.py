def get_initials(fullname):
	'''given a name, return initials (uppercase)'''
	initials = [subname[0].upper() for subname in fullname.split()]
	return "".join(initials)
	
def main():
	getname = input("What is your full name? ")
	print(get_initials(getname))
	
if __name__ == "__main__":
	main()