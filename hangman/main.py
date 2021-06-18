# get a word
word = "cherry"
word_len = len(word)
answer_string = list("-" * word_len)
#letter = input("Please enter a letter:")
#print("".join(answer_string))
while "-" in answer_string:	
	letter = input("Please enter a letter:")
	for x in range(0,word_len):
		if word[x] == letter: 
			answer_string[x] = letter
	
	print("".join(answer_string))	

print("bingo ",word," is the word")
		
