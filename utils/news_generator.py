from abc import ABC, abstractmethod
import numpy
import pickle
import utils.configs as configs


def is_next_title(word: str) -> bool:
    return word[-1] in ['.', '!', '?']


def preprocess(word: str, is_title: bool) -> str:
    if (is_title):
        return word[0].upper() + word[1:]
    else:
        return word


class NewsGenerator(ABC):
    def __init__(self) -> None:
        self.dictionary = {}
        self.words = []

    @abstractmethod
    def generate(self, min_length: int) -> str:
        if len(self.words) < min_length:
            return self.generate(min_length - 1)
        else:
            return ' '.join(self.words)


class ITNewsGenerator(NewsGenerator):
    def __init__(self) -> None:
        super().__init__()

        with open(configs.IT_DATA, "rb") as it_dict_data:
            self.dictionary = pickle.load(it_dict_data)

    def generate(self, min_length: int) -> str:
        self.words = []

        next_title = True

        word = numpy.random.choice(list(self.dictionary))
        self.words.append(preprocess(word, next_title))

        next_title = is_next_title(word)

        while word in self.dictionary:
            total_followers = sum(self.dictionary[word].values())

            probabilities = [follower / total_followers
                             for follower in
                             self.dictionary[word].values()]

            word = numpy.random.choice(list(self.dictionary[word]),
                                       p=probabilities)

            self.words.append(preprocess(word, next_title))

            next_title = is_next_title(word)

        return super().generate(min_length)


class ImprovedITNewsGenerator(NewsGenerator):
    def __init__(self) -> None:
        super().__init__()

        with open(configs.IMPROVED_IT_DATA, "rb") as it_dict_data:
            self.dictionary = pickle.load(it_dict_data)

    def generate(self, min_length: int) -> str:
        self.words = []

        next_title = True

        word_pair = numpy.random.choice(list(self.dictionary))
        self.words.append(preprocess(word_pair, next_title))

        next_title = is_next_title(word_pair)

        while word_pair in self.dictionary:
            total_followers = sum(self.dictionary[word_pair].values())

            probabilities = [follower / total_followers
                             for follower in
                             self.dictionary[word_pair].values()]

            next_word = numpy.random.choice(list(self.dictionary[word_pair]),
                                            p=probabilities)

            word_pair = "{0} {1}".format(word_pair.split(' ')[1], next_word)

            self.words.append(preprocess(next_word, next_title))

            next_title = is_next_title(word_pair)

        return super().generate(min_length)
