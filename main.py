def get_book_text():
	import sys
	
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	with open(book_path) as file1:
		return file1.read()
		
def main():
	from stats import words_counter
	from stats import chars_counter
	from stats import sorting_charsdic
	TEXT = get_book_text()
	words_num = words_counter(TEXT)
	# adding the data onto the "chars variable"
	charsd = chars_counter(TEXT) 
	sorted_charsdic = sorting_charsdic(charsd)
	
	
	print(f"============ BOOKBOT ============\nAnalyzing book found at SOMEPLACE ...")
	print("----------- Word Count ----------")
	print(f"Found {words_num} total words")
	# Declare print func to print the chars!
	#print(f"{charsd}")
	print("--------- Character Count -------")
	for node in sorted_charsdic:
		print(f"{node["char"]}: {node["num"]}")
	print("============= END ===============")

main()
