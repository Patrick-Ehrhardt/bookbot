def get_num_words(book_text):
        word_count = 0
        split_words = book_text.split()
        for word in split_words:
                word_count += 1
        return word_count

def count_characters(book_text):
	book_text = book_text.lower()
	char = ''
	char_dict = {}
	#char_dict = dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
	for i in range (0, len(book_text)):
		char = book_text[i]
		if char not in char_dict:
			char_dict[char] = 0
		#print(type(char))
		char_dict[char] += 1
	return char_dict
