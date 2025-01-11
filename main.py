def char_count(lowered_string):
    char_dict = {}

    #Loop through string
    for i in range(len(lowered_string)):

        #Only deal with a..z characters
        if lowered_string[i].isalpha():

            #See if character is already in dictionary
            if lowered_string[i] in char_dict:
                #If it is, increment count
                char_dict[lowered_string[i]] += 1
            else:
                #If not, add it
                char_dict[lowered_string[i]] = 1
    
    #Print results, sorted in frequency used order (largest to smallest)
 
    #Sort the dictonary
    sorted_dict = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}

    #Convert to list
    char_list = list(sorted_dict.items())

   #print results
    print("--- Begin report of books/frankenstein.txt ---")
    for j in range(len(char_list)):
        print(f"The '{char_list[j][0]}' character was found {char_list[j][1]} times")
    #print(char_dict)

def main():

    #Load book into file_content string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    #Get character count; Force lowercase to eliminate duplicates
    char_count(lowered_string = file_contents.lower())

    #Create a list of words from file_content
    words = file_contents.split()

    #Get the word count of the book
    word_count = len(words)
    
    #Print out the word count
    print("")
    print(f"{word_count} words found in the document")
    print("--- End report ---")

main()