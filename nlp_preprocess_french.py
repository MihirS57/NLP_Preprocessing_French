import nltk
import spacy
import re
import unicodedata
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer
from num2words import num2words
 
french_stopwords = stopwords.words('french')
print("French Stopwords List",french_stopwords)
stemmer = FrenchStemmer()
nlp = spacy.load('fr_core_news_md')

#Lowercase
french_text = "Je m'appelle Mihir Shah et je suis étudiant en génie informatique. J'ai 21 ans !"
low_french_text = french_text.lower()
print("Lower Case",low_french_text)

#Extra Whitespaces
def remove_extra_whitespaces(text):
    string = ""
    text = text.strip()
    text = text.split(' ')
    blank_spaces = text.count('')
    for i in range(0,blank_spaces):
        text.remove('')
    for x in text: 
        string = string + x + " "
    return string
french_text = remove_extra_whitespaces(french_text)
print("Extra Whitespaces: ",french_text)

#Tokenization
french_words = word_tokenize(french_text)
print("Tokenization: ",french_words)

#Removing Stopwords
clean_french_text = ""
for word in french_words:
    if word not in french_stopwords:
        clean_french_text = clean_french_text+word+" "
print("Removing Stopwords: ",clean_french_text)

#Lemmatization 
doc = nlp(french_text)
print("Lemmatization:")
for token in doc:
    print(token, token.lemma_)

#Stemming
print("Stemming:")
for word in french_words:
    print(f'{word} -> {stemmer.stem(word)}')

#Removal of HTML Tags
def remove_tag(text):
    text=''.join(text)
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)
print("Removal of HTML Tags")
tagged_frenchtext = "<h1> Je m'appelle Mihir Shah et je suis étudiant en génie informatique </h1> "
print("     Tagged: ",tagged_frenchtext)
untagged_frenchtext = remove_tag(tagged_frenchtext)
print("     Untagged: ", untagged_frenchtext)

#POS tagging
tagged = nltk.pos_tag(french_words)
print("POS tagged: ",tagged)

#Removing accents
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
print("Removing accents: ",strip_accents(french_text))

#To numeric words
print("To numeric words: ")
for word in french_words:
    if word.isdigit():
        print(num2words(word,lang="fr"))

#Remove numbers & special characters
clean_frenchtext = re.sub('[^a-zA-Z]', ' ', french_text)
clean_frenchtext = re.sub(' +', ' ', clean_frenchtext)
print("Removed Numbers & special characters: ",clean_frenchtext)