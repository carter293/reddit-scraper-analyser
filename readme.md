# Reddit Scraper & Analyzer

This repo contains a scraper and analysis file to capture and attempt to

## Description

This project aims to scrape Reddit posts from specified subreddits and perform topic modeling and sentiment analysis on the fetched data. The primary goal is to find common problems within a corpus of reddit posts that could be solved using a SaaS application or other technology.

## Features

Reddit Scraper: Fetches posts and comments from a specified subreddit using the PRAW library.
**File** : scraper.py

Topic Modeling: Utilizes techniques such as Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF) to uncover the main topics being discussed in the subreddit.
Sentiment Analysis: Uses the TextBlob library to classify the sentiment (positive, negative, neutral) of each post or comment.
OpenAI Integration: Interpre
**File** : analysis.ipynb

## Setup

### Installation

#### Install Pipenv

```shell
pip install pipenv
```

#### Install required packages using `pipenv`

```shell
pipenv install
```

#### Activate the Pipenv Shell

```shell
pipenv shell
```

## Usage

### OpenAI & Reddit

This project also utilizes OpenAI and Reddit Apps, you will need to create an account and app respectively.

Reddit : https://www.reddit.com/prefs/apps
OpenAI : https://platform.openai.com/signup?launch

Once you have, create a `.env.local` file and enter the your details like so:

```shell
API_KEY=<OPENAI_KEY_HERE>

CLIENT_ID=<REDDIT_CLIENT_ID_HERE>
CLIENT_SECRET=<REDDIT_CLIENT_SECRET_HERE>
USER_AGENT=<REDDIT_USER_AGENT_HERE>
```

## Running scraper

Update your chosen subreddit and number of records you'd like to download with the `scraper.py` file. Then run the file like so:

```shell
python3 scraper.py
```

## Running Analysis

Install jupyter notebook plugins in VSCode or download the package to your machine and run the notebook.

Uncomment the downloads in the second code block on the first pass.

```python
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('vader_lexicon')
```
