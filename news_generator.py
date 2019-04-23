from abc import ABC, abstractmethod
import numpy
import pickle


def is_next_title(word):
    return word[-1] in ['.', '!', '?']


def preprocess(word: str, is_title):
    if (is_title):
        return word[0].upper() + word[1:]
    else:
        return word


class NewsGenerator(ABC):
    def __init__(self):
        self.dictionary = {}

    @abstractmethod
    def generate(self, length):
        pass


class ITNewsGenerator(NewsGenerator):
    def __init__(self):
        super().__init__()

        with open("./news_data/it", "rb") as it_dict_data:
            self.dictionary = pickle.load(it_dict_data)

    def generate(self, length):
        words = []

        next_title = True

        word = numpy.random.choice(list(self.dictionary))
        words.append(preprocess(word, next_title))

        next_title = is_next_title(word)

        while word in self.dictionary:
            total_followers = sum(self.dictionary[word].values())

            probabilities = [follower / total_followers for follower in self.dictionary[word].values()]

            word = numpy.random.choice(list(self.dictionary[word]), p=probabilities)
            words.append(preprocess(word, next_title))

            next_title = is_next_title(word)

        if len(words) < length:
            return self.generate(length - 1)
        else:
            return ' '.join(words)
