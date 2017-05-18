## 1. Overview ##

file = open('dictionary.txt','r')
vocabulary = file.read()
print(vocabulary)

## 2. Tokenizing the Vocabulary ##

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(" ")
print(tokenized_vocabulary[0:5])

## 3. Replacing Special Characters ##

f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("'","")
story_string = story_string.replace(";","")
story_string = story_string.replace("\n","")
print(story_string)

## 5. Practice: Creating a Function that Cleans Text ##

f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string):
    cleaned_string = text_string.replace(".","") #Take out periods
    cleaned_string = cleaned_string.replace(",","") #Take out commas
    cleaned_string = cleaned_string.replace("'","") #Take out '
    cleaned_string = cleaned_string.replace(";","") # Take out semicolons
    cleaned_string = cleaned_string.replace("\n","") #Take out new lines
    return(cleaned_string) #return cleaned text

cleaned_story = clean_text(story_string)

## 6. Changing Word Case ##

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
cleaned_story = clean_text(story_string)

## 7. Multiple Arguments ##

f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]


def clean_text(text_string,special_characters):
    cleaned_string=text_string
    
    #Clean The Story from all items in clean_chars list
    for char in special_characters:
        cleaned_string = cleaned_string.replace(char,"")
    
    #All upper case letters become lowercase
    cleaned_string = cleaned_string.lower()
    
    return(cleaned_string)

cleaned_story = clean_text(story_string, clean_chars)

## 8. Tokenizing the Story ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string,special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)
#List of special chars
clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars) #Cleaned story

#Implement tokenized function of the uncleaned text story_string
tokenized_story = tokenize(story_string,clean_chars)
print(tokenized_story[0:10])

## 9. Finding Misspelled Words ##

#Strip off special characters from a given text document
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
#Put every word into a list 
def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)
#Instantiated list called misspelled_words
misspelled_words = []
#Special Character Conditions
clean_chars = [",", ".", "'", ";", "\n"]
#Tokenize given text
tokenized_story = tokenize(story_string, clean_chars)
#Tokenize our library
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

#Determine if words are mispelled by cross referencing vocabulary
for word in tokenized_story:
    if word not in tokenized_vocabulary:
        misspelled_words.append(word) #If misspelled, add to list 
print(misspelled_words)