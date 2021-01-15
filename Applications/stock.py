#Import the need modules
import re #regular expression module to look for matching string

from urllib.request import Request, urlopen #URL handling module

arrayofStocks = ["FB", "GOOG"] #Supported inputs, and others available in Google Finance website
stock = input("Enter your stock: ") #Taking the input data
url = Request("https://www.google.com/finance?q="+stock, headers={'User-Agent': 'Mozilla/5.0'})#The URL of the site where the data would be extracted

#search_url = url + stock #Getting the complete search URL

raw_data = urlopen(url).read() #This gives raw data that is unintelligble

readable_data = raw_data.decode("utf-8") #The raw data is decoded into a readable format
"""
What you have from line 21 to 32 is drilling down the readable data to extract the extract
data that is of importance and need.
"""
lookup_word = re.search('meta itemprop="price"', readable_data) #using the search method of the re module to find "meta itemprop='price'"

print(dir(lookup_word))
print(lookup_word)
#which is the tag of the stock data
start1 = lookup_word.start() #Getting the first position of the search word

end1 = start1 + 50 #Getting the last position of the search word

newWord= readable_data[start1:end1] #Extracting a new, but closer, word to the data of interest, based on the start and end position

lookup_word = re.search('content="', newWord) #A new look up, but re-assigned to the same variable lookup_word

start2 = lookup_word.end() #getting the first position of the word

nextWord = newWord[start2:]

lookup_word = re.search("/", nextWord) #A new look up

start3 = 0 #Assigning the first index position to

end3 = lookup_word.end()-3

final = nextWord[start3:end3]

print("The value of " + stock.upper() + " is " + final)
