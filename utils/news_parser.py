from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import pickle
import requests
import time

HEADERS = {
    "User-Agent": "Chrome/73.0.3683.103"
    }


class NewsParser(ABC):
    @abstractmethod
    def parse(self, page_count: int) -> None:
        pass


class IPhonesNewsParser(NewsParser):
    def parse(self, page_count: int) -> None:
        BASE_URL = "https://www.iphones.ru/page"

        post_list = []
        for page in range(1, page_count):
            response = requests.get("{0}/{1}".format(BASE_URL, page), headers=HEADERS)
            soup = BeautifulSoup(response.text, "html.parser")

            time.sleep(1)

            post_list.extend(soup.find_all("h2", {"class": "postitem__content-h"}))

        link_list = []
        for post in post_list:
            soup = BeautifulSoup(str(post), "html.parser")

            link_list.append(soup.find("a").get("href"))

        with open("./news_data/it", "rb") as it_dict_data:
            it_dict = pickle.load(it_dict_data)

        for link in link_list:
            response = requests.get(link, headers=HEADERS)
            soup = BeautifulSoup(response.text, "html.parser")

            for paragraph in soup.select(".post > p"):
                words = paragraph.text.split()

                for i in range(len(words) - 1):
                    if words[i] not in it_dict:
                        it_dict[words[i]] = {}

                    if words[i + 1] not in it_dict[words[i]]:
                        it_dict[words[i]][words[i + 1]] = 1
                    else:
                        it_dict[words[i]][words[i + 1]] += 1

        with open("./news_data/it", "wb") as it_dict_data:
            pickle.dump(it_dict, it_dict_data)


class ImprovedIPhonesNewsParser(NewsParser):
    def parse(self, page_count: int) -> None:
        BASE_URL = "https://www.iphones.ru/page"

        post_list = []
        for page in range(1, page_count):
            response = requests.get("{0}/{1}".format(BASE_URL, page), headers=HEADERS)
            soup = BeautifulSoup(response.text, "html.parser")

            time.sleep(1)

            post_list.extend(soup.find_all("h2", {"class": "postitem__content-h"}))

        link_list = []
        for post in post_list:
            soup = BeautifulSoup(str(post), "html.parser")

            link_list.append(soup.find("a").get("href"))

        with open("./news_data/improved_it", "rb") as it_dict_data:
            it_dict = pickle.load(it_dict_data)

        for link in link_list:
            response = requests.get(link, headers=HEADERS)
            soup = BeautifulSoup(response.text, "html.parser")

            for paragraph in soup.select(".post > p"):
                words = paragraph.text.split()

                for i in range(len(words) - 2):
                    word_pair = "{0} {1}".format(words[i], words[i + 1])

                    if word_pair not in it_dict:
                        it_dict[word_pair] = {}

                    if words[i + 2] not in it_dict[word_pair]:
                        it_dict[word_pair][words[i + 2]] = 1
                    else:
                        it_dict[word_pair][words[i + 2]] += 1

        with open("./news_data/improved_it", "wb") as it_dict_data:
            pickle.dump(it_dict, it_dict_data)
