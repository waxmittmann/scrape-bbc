- To switch from crawl-local (using ./bbcsite to crawl) to remote (crawling bbc.com) manually replace start_urls in BBCSpider.py.
    Better alternative coming soon.

- To switch from local mongodb (default port etc) to the compose.io version or vice versa, comment in the appropriate
    file in './config/environment.cfg'. (Yep, the password for my trial account db is out on github, heh). Prod = compose.io

- Run the crawler: crawlBBC

- Run the server: startServer

- RESTful calls:
> GET http://localhost:8091/articles
    returns all articles crawled (warning, this could be big)
> GET http://localhost:8091/words
    returns all words in the index (words that have been found in articles) and the urls in which they occur
> GET http://localhost:8091/words/{word}
    returns all articles for the provided word (should probably be "/articles?word={word}" instead)
