def file_words_chars_count(filename):
    words_count = 0
    characters_count = 0

    with open(filename, "r") as file:
        text = file.read()
        text = text.replace("  ", "")
        for chars in text:
            characters_count +=1
        text = text.split()
        for word in text:
            words_count += 1
        
        return f"The file has {characters_count} characters, and {words_count} words."

print(file_words_chars_count("guess_the_number.py"))