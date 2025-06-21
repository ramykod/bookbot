def words_counter (TEXT):
	words = TEXT.split()
	return len(words)

def chars_counter (TEXT):

	chars_dic = {}
	for chars in TEXT:
		chars = chars.lower() 
		if chars in chars_dic:
			chars_dic[chars] = chars_dic[chars] + 1			
		else:
			chars_dic.update({chars: 1})

	return chars_dic

def sort_on(d):
    return d["num"]

def sorting_charsdic (chars_dic):

	chars_list = []
	for item in chars_dic.items():
		the_key = item[0]
		the_count = item[1]
		if the_key.isalpha():
			neodict = {"char" : the_key , "num" : the_count}
			chars_list.append(neodict)
	
	chars_list.sort(reverse=True, key=sort_on)
	
	return chars_list
	

