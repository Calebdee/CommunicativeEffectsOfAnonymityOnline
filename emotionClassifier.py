from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

from textblob.classifiers import NaiveBayesClassifier
import pandas as pd


'''
A class that performs emotional classification
The class uses the ISEAR dataset as the training model for predicting the emotional tag for a given text
It also returns the probabilistic value for any given text
'''


class emotion_classify:
    def __init__(self):


        self.df = pd.read_csv('ISEAR.csv')
        self.a = pd.Series(self.df['joy'])
        self.b = pd.Series(self.df[
                               'On days when I feel close to my partner and other friends.When I feel at peace with myself and also experience a close contact with people whom I regard greatly.'])
        self.new_df = pd.DataFrame({'Text': self.b, 'Emotion': self.a})

        self.stop = set(stopwords.words('english'))  ## stores all the stopwords in the lexicon
        self.exclude = set(string.punctuation)  ## stores all the punctuations
        self.lemma = WordNetLemmatizer()

        ## lets create a list of all negative-words
        self.negative = ['not', 'neither', 'nor', 'but', 'however', 'although', 'nonetheless', 'despite', 'except',
                         'even though', 'yet']

        ## create a separate list to store texts and emotion
        self.em_list = []
        self.text_list = []

        ## create the training set
        self.train = []

         # stores the summarized text in a list
        self.sum_text_list = []

        # the e-score list stores the e-score for each document
        self.e_score_dict = {}

        # call the driver function
        self.main()

    '''
    A function for cleaning up all the documents
    # removes stop words
    # removes punctuations
    # uses lemmatizer 
    '''

    def clean(self, doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in self.stop if i not in self.negative])
        punc_free = "".join([ch for ch in stop_free if ch not in self.exclude])
        normalized = " ".join([self.lemma.lemmatize(word) for word in punc_free.split()])
        return normalized

    '''
    Function to iterate and clean up all texts
    '''

    def iterate_clean(self):
        for i in range(self.df.shape[0]):
            self.new_df.loc[i]['Text'] = self.clean(self.new_df.loc[i]['Text'])

    '''
    Function to iterate and populate text list
    '''

    def iterate_pop_text(self):
        for i in range(self.new_df.shape[0]):
            self.text_list.append(self.new_df.loc[i]['Text'])

    '''
    Function to iterate and populate emotion list
    '''

    def iterate_pop_emotion(self):
        for i in range(self.new_df.shape[0]):
            self.em_list.append(self.new_df.loc[i]['Emotion'])

    '''
    Function to create training set
    '''

    def create_train(self):
        for i in range(self.new_df.shape[0]):
            self.train.append([self.text_list[i], self.em_list[i]])

    '''
    Function to create model
    classify the query text
    and then summarize other texts
    classify them and return a dictionary containing the e-score for all documents
    '''

    def classify_text(self):

        cl = NaiveBayesClassifier(self.train)

        result = cl.classify("love sandwich!")

        print(result)




    '''
    A function which is the driver for the entire class

    '''

    def main(self):

        self.iterate_clean()
        self.iterate_pop_emotion()
        self.iterate_pop_text()
        self.create_train()
        self.classify_text()