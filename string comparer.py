print("Simple string comparer v2.0 by Mipirakas\n\nWelcome to this state of the art ;) string comparer.\nInput your 2 strings below and i'll compare them for you.\n")

str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")

print("\n")

if str1 == str2:
	print("String 1 and 2 are equal.")
else:
	print("The two strings are different and are arranged alphabetically and from smallest number to biggest number. (does not work for negative numbers)\n")

	if str1 > str2:
		print("String 2) " + str2 + "\nString 1) " + str1)

	if str1 < str2:
		print("String 1) " + str1 + "\nString 2) " + str2)
