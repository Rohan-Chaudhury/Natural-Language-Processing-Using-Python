from nltk.tokenize import sent_tokenize,word_tokenize



sample_text='Hello Mr. Rhan Chaudhury, how are you doing. The weather seems fine and it is a nice day to go out'


for i in word_tokenize(sample_text):
    print(i)

for i in sent_tokenize(sample_text):
    print(i)
