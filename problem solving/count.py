def word_counter():
    text = input("Enter a string: ")
    words = text.split()
    word_count = len(words)
    print(f"The number of words in the string is: {word_count}")
word_counter()
