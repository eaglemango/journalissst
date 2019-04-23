# Journalissst

Journalissst is a Telegram bot that can generate messages using precomputed data.
It prefers newspapers for breaskfast, so the result of its work is something, that distantly looks like an article.

## Markov chain

According to Wikipedia, Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.

Whatever that means, it helps Journalissst to generate texts.

## How does it work

Journalissst bot is powered by Markov chain model.

It stores data in the following structure:

```
{"some_word": {"one_of_the_following_words": 13, "another_one": 37}, "another_word": {"pen": 132, "notebook": 42}, "MIPT": {"calculus": 1000, "physics": 500, "sleep": 1}}
```

That means, that in input data `pen` follows `another_word` in `132` сases and `notebook` follows it only in `42` cases. 

Obviously, we need to store such an exciting data structure on hard drive. Python module `pickle` is used for that purpose. Files with precomputed data are located in `news_data` folder.

The process of messages generating is shown in `utils/news_generator.py` script. First word is chosen absolutely randomly (it has the same probability as others). But on the each next iteration we need to count all probabilities for the following words and only after it choose the next word. Module `numpy` is used because it helps to choose random things with information about their probability.

