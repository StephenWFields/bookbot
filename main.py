def main():

    #Load book into file_content string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    #Create a list of words from file_content
    words = file_contents.split()

    #Get the word count of the book
    word_count = len(words)
    
    #Print out the word count
    print(word_count)

main()