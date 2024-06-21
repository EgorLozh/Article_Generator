import requests
import json
def get_google_trends():
    headers = {
        'authority': 'trends.google.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        'dnt': '1',
        'referer': 'https://trends.google.com/trends/trendingsearches/daily?geo=RU&hl=ru',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = [
        ('hl', 'ru'),
        ('tz', '-240'),
        ('geo', 'RU'),
        ('hl', 'ru')
    ]

    response = requests.get('https://trends.google.com/trends/api/dailytrends', params=params,
                            headers=headers).text.replace(")]}',", "", 1)
    json_response = json.loads(response)
    main_info = json_response['default']['trendingSearchesDays'][0]['trendingSearches']
    articles = [{
        'title': article['title']['query'],
        'source_url': article['image']['newsUrl'],
    } for article in main_info]
    return articles

if __name__=="__main__":
    print(*get_google_trends(), sep="\n")
