meme_dict = {
	"cringe": "Something weird, disgusting or just not in the favor of everyone else",
	"lol": "The short for \"laughing out loud\", used when something's funny",
}

print("[ GenZ Translator TM V1.0 ]\nEnter a Gen Z keyword in all lowercase:")

while True:
	word = input(">")
  
	if word in meme_dict.keys():
		print(meme_dict[word])
	elif word == "exit":
		break
	else:
		print("Invalid Keyword")
