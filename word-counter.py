with open("text.txt", "r") as txtFile:
    text = txtFile.read()

search_words = ["Python", "C", "OOP", "Hello", "Java"]  # Original

low_search_words = [word.lower() for word in search_words] # Lowercase

word_count = {word: 0 for word in search_words}

words = text.split()

for word in words:
    if word.lower() in low_search_words:
        word_count[search_words[low_search_words.index(word.lower())]] += 1

for word in search_words:  
    print(f"{word} -> {word_count[word]}")
