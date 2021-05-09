"""
The program is trying to translate a sentence captured as user input.
We first read in the test file textese.txt
then from the text file, we create a list of strings from each line in the text file
Then, we create a dictionary list
Onece the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into a 
array of strings ("Enjoy the excellent band tonight")

Once we have the array of strings representing the user's input sentence, we
loop through each words, find the words, find the key matching the word and returns back the valuetied to the 
word in our dictionary. 

After each word is translated, we then 
print out the translated sentence to the user. 
"""

"""

main():
    set_dictionary = translate()
    translate(sentence, dictionary)

translate:(sentence, dictionary):
    words = for each of the words in the sentece
    for each words, translae the word
    print translated sentence to user 

create_dictionary():
    read in textese.txt
    create list = each line from file 
    close the file
    creeate a dict off of the list
    return the dict

main()

"""
def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split() 
    for word in words: 
        print(dictionary.get(word, word), " ", end="")

main()
