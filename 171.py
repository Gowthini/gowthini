def reverseWordSentences(Sentences):
	return ' '.join(word[::-1] for word in Sentences.split(" "))
Sentences = "uyutyutuyutyututyutyu"
print(reverseWordSentences(Sentences)) 
