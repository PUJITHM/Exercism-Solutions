def rotate(text, key):
	result = str()
	for char in text:
		if (char.lower() >= 'a' and char.lower() <= 'z'):
			Cipher = ord('a') + ((ord(char.lower()) - ord('a') + key) % 26)
			if char.isupper():
				result += chr(Cipher).upper()
			else:
				result += chr(Cipher)
		else:
			result += char
	return result