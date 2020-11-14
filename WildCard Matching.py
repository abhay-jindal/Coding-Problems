def stringmatch(text, pattern, lenText, lenPattern): 
	if (lenPattern == 0): return (lenText == 0) 
		 
	i, j, indexText, indexPattern = 0, 0, -1, -1
	while(i < lenText-2): 
		if (j < lenPattern and (text[i] == pattern[j] or pattern[j] == '?')):
			i += 1
			j += 1	
		elif(j < lenPattern and pattern[j] == '*'): 
			indexText, indexPattern = i, j
			j += 1
		elif(indexText != -1): 
			i, j = indexText+1, indexPattern+1
			indexText += 1
		else: 
			return False

	while (j < lenPattern and pattern[j] == '*'): 
		j += 1

	if(j == lenPattern): return True
	return False

if __name__ == "__main__": 
	print("Wildcard Matching where '?' matches any single character and '*' mathces sequence of characters.")
	text = input("Enter the text: ")
	pattern = input("Enter the pattern which matches above text: ")
	if (stringmatch(text, pattern, len(text), len(pattern))): 
		print("Yes") 
	else: 
		print( "No") 

