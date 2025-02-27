from stats import get_num_words
from stats import count_characters
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def sort_on(dict):
	return dict["value"]

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	#print(sys.argv)
	fpath = sys.argv[1]
	book_text = get_book_text(fpath)
	num_words = get_num_words(book_text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {fpath}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	char_dict = count_characters(book_text)
	print("--------- Character Count -------")
	delete_keys = []
	for key in char_dict:
		if key.isalpha() == False:
			delete_keys.append(key)
		#else:
		#	print(f"{key}: {char_dict[key]}")
	for key in delete_keys:
		del char_dict[key]
	sorted_chars = []
	for key in char_dict:
		temp_dict = {"char" : key, "value" : char_dict[key]}
		sorted_chars.append(temp_dict)
	sorted_chars.sort(key=sort_on, reverse=True)
	for i in range (0, len(sorted_chars)):
		temp_dict = sorted_chars[i]
		temp_char = temp_dict["char"]
		temp_value = temp_dict["value"]
		print(f"{temp_char}: {temp_value}")
	print("============= END ===============")
	#for key in char_dict:
		#print(f"{key}: {char_dict[key]}")
	#print(char_dict)
	return 0

main()
