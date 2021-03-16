string1 = "My name is rajkumar My nmae is raj"
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))