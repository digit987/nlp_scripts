'''
We have been provided some sentences referred as documents. We have to generate TF-IDF vector for each.
'''

import  math

#Input
documents = ["It is the measure of the importance of a word.", "Term frequency (TF) does not consider the importance of words.", "Some words such as of, and, etc. can be most frequently present but are of little significance the.", "the IDF provides weightage to each word based on its frequency in the corpus D."]

num_of_documents = len(documents)

#Number of documents that contain a word. Required for the denominator of IDF.
num_of_documents_containing_the_word = {}

#Vocabulary is the collection of all unique words
vocabulary = []

#We populate vocabulary by traversing each document.
for document in documents:
    #In each document (sentence), we extract all the words to a list, last word is without full stop, for example, "hello." is taken as "hello"
    words_in_document = str(document)[:-1].split()
    for word in words_in_document:
        vocabulary.append(word)
        
#print(vocabulary)

#We populate the dictionary num_of_documents_containing_the_word. If a word exists in the dictionary, its count is incremented, otherwise it's inserted in it for the first time.
for word in vocabulary:
    for document in documents:
        if word in document:
            if word in num_of_documents_containing_the_word:
                num_of_documents_containing_the_word[word] += 1
            else:
                num_of_documents_containing_the_word[word] = 1

#tf_idf_list is a list whose each element is a vector for a document. This vector is stored as a dictionary for each document. Again, we go to each document, then each word of the document and store its count. TF = occurences of a word in the document / number of words in the document. IDF = ln(number of documents / num of documents containing the word). We already have the dictionary num_of_documents_containing_the_word. We calculate TF * IDF for words that are in the document; for the words that are absent, we store value 0.
tf_idf_list = []
for document in documents:
    document_length = len(document)
    tf_idf_dict = {}
    word_count = {}
    words_in_document = str(document)[:-1].split()
    for word in words_in_document:
        if word in word_count:
            word_count[word] = document.count(word)
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        tf_word = word_count[word] / document_length
        idf_word = math.log(num_of_documents / num_of_documents_containing_the_word[word])
        tf_idf_dict[word] = tf_word * idf_word
    for word in vocabulary:
        if word not in tf_idf_dict.keys():
            tf_idf_dict[word] = 0
    tf_idf_list.append(tf_idf_dict)
    
#Printing the output
for tf_idf_vector in range(len(tf_idf_list)):
    print("TF-IDF vector for document ", tf_idf_vector + 1, "is: ")
    print(tf_idf_list[tf_idf_vector])
    print("==============================================")
