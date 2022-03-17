#You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

#
#    If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
#        For example, the word "apple" becomes "applema".
#    If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
#        For example, the word "goat" becomes "oatgma".
#    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
#Input: sentence = "I speak Goat Latin"
#Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

input="I speak Goat Latin"
i=0
output=""
for x in input.split(" "):
	i+=1
	word=x
	print(x)
	if x[0].lower() in "aeiou":
		x=x+"ma"+"a"*i
	else:
		x=x[1:]+x[0]+"a"*i
	output+=x+" "
print(output)


		
		

