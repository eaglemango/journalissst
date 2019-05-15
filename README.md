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
{"some_word":
    {"one_of_the_following_words": 13,
     "another_one": 37
    },
 "another_word":
    {"pen": 132,
     "notebook": 42
    },
 "MIPT":
    {"calculus": 1000,
     "physics": 500,
     "sleep": 1
    }
}
```

That means, that in input data `pen` follows `another_word` in `132` сases and `notebook` follows it only in `42` cases. 

Obviously, we need to store such an exciting data structure on hard drive. Python module `pickle` is used for that purpose. Files with precomputed data are located in `news_data` folder.

Messages generation is provided by `/utils/news_generator.py`. It works in three simple steps:

1. Take a random word from dictionary and make it first in output.
2. Take a random word from previous word's followers and make it last in current output.
3. If last word has no followers in dictionatry, stop generation. Otherwise, go to step 2.

It's noticeable, that script uses `numpy` for picking random words, because that module supports `random.choice` with probability for each variant.

You also can add you own generator. It should be inherited from `NewsGenerator` class (consequently, it must have the same method `generate`).

## How does it collect information

Journalissst must be trained before usage. Training means creating a dictionary (structure was shown above) from input text:

1. If current word isn't from dictionary, then add it to dictionary.
2. If current word isn't from previous word's followers, then add it to previours word's followers. Otherwise, increment occurence counter.

In order to get information for proccessing, Journalissst uses `/utils/news_parser.py`. That module is based on `requests` (for getting information from news sites) and `bs4` (for parsing it). 

You also can add your own news parser. It should be inherited from `NewsParser` class (consequently, it must have the same method `parse`).

## Usage

Journalissst is amazingly user-friendly bot. My original bot has only three commands:

`/help` - get a list of supported commands

`/it` - generate IT news

`/political` - generate political news

## Setting up the bot

Feel free to fork my repository and create your own bots. Journalissst's code is suitable for many purposes, that requires Markov chain, like generating text using incoming messages, books, memes, quotes and so on.

At first, you need to talk to `@BotFather` and get your bot's API token. Put it in `TOKEN` field in `/utils/configs.py` file. You also need to have a web server for running Journalissst (using own computer for it is OK). Fill `WEBHOOK_HOST` and `WEBHOOK_PORT` in the same file.

Then you have to generate SSL certificate for the server (Telegram won't even talk to your bot if it has no certificate). 

Install `openssl` on your Linux machine (if there's no Linux, install it) and write the following commands in the terminal:

```
$ openssl genrsa -out webhook_pkey.pem 2048
```

```
$ openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
```

The second command will ask you for `CommonName`. Write your server's address there.

Put certificate and private key in `/certificates/`.

Final step is checking if all required modules are installed (if something is missing, ask `pip3` for help).

Now you can run your own Markov chain bot:

```
$ python3 journalissst_bot.py
```