from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
# import numpy
from collections import Counter

# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("averaged_perceptron_tagger")
# nltk.download("maxent_ne_chunker")
# nltk.download("words")


class NameExtractor:

    @staticmethod
    def extract_noun(quote):
        """Parses a sentence of words and returns the nouns"""
        words = word_tokenize(quote)
        tags = nltk.pos_tag(words)
        tree = nltk.ne_chunk(tags, binary=True)
        return list(
            " ".join(i[0] for i in t)
            for t in tree
            if hasattr(t, "label") and t.label() == "NE"
        )

    def extract_name(self, sentences: list):
        """Takes a list of sentences and returns the most likely name"""
        sentence_nouns = []
        stop_words = set(stopwords.words("english"))

        # print("\nEXTRACT NAME\n")
        for sentence in sentences:
            # print(sentences.index(sentence), sentence)
            sentence_nouns.append(self.extract_noun(sentence))
        for idx in range(len(sentence_nouns)):
            sentence_nouns[idx] = [element for element in sentence_nouns[idx] if element. lower() not in stop_words]

        name_counts = Counter([element for sublist in sentence_nouns for element in sublist])
        name = self.__select_name(name_counts)
        return name

    @staticmethod
    def __select_name(dict_of_names: dict):
        """Takes a list of names and returns the highest priority name"""
        name_score = 0
        selected_name = None
        for name in dict_of_names.keys():
            if dict_of_names[name] > name_score and len(name.split(" ")) < 3:
                name_score = dict_of_names[name]
                selected_name = name
        # for name in dict_of_names.keys():
        #     if len(name.split(" ")) > 1 and selected_name in name.split(" "):
        #         selected_name = name
        return selected_name
# import pandas
# file = pandas.read_csv("Names in Google Sheet Test - Sheet1.csv", names=["link", "name", "rating", "a_num", "phone", "address", "ceo"])
# file.dropna(inplace=True)
# pandas.set_option('display.max_columns', None)
# print(file[:5])
# print("here", file.loc[2]["name"])