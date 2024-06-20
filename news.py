from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='60da179b3ec446838fdbe7f835fc1cb7')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q=input('enter topic :'),
                                          category=input('enter category :'),
                                          language='en')

dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')


