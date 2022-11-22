from newscatcherapi import NewsCatcherApiClient

API_KEY = 'jR1Vt6UMiNQcxXRgFqc3rU2asiOiUfdzPvY-HUfTW1Y'

newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)

news_articles = newscatcherapi.get_search(q="Larreta",
                                            lang='es',
                                            countries='AR',
                                            page_size=100).user_input

for item in news_articles:
    print(item)

