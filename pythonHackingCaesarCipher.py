message = 'GUVF VF ZL FRPERG ZRFFNTR'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# loop through every possible key
for key in range(len(LETTERS)):
	# It is important to set translated to the blank string so that the
	# previous iteration's value for translated is cleared.
	translated = ''
	# The rest of the program is the same as the original Caesar program:
	for symbol in message:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			num = num - key
			if num < 0:
				num = num + len(LETTERS)
			# get the symbol at num
			translated = translated + LETTERS[num]
		else:
			# just add the symbol without encrypting/decrypting
			translated = translated + symbol
	# display the current key being tested, along with its decryption
	print('Key #%s: %s' % (key, translated))

