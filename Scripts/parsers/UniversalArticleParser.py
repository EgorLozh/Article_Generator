import requests
from bs4 import BeautifulSoup as BS

def get_article(url):
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')
    text_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    texts = soup.find_all(text_tags)
    same_class_texts = {}

    for text in texts:
        classes = str(text.parent.get('class'))
        if classes in same_class_texts.keys():
            same_class_texts[classes] += '\n'+text.text
        else:
            same_class_texts[classes] = text.text
    return max(same_class_texts.values(), key=len)


if __name__ == '__main__':
    url ='https://vtomske.ru/news/204985-letnee-solncestoyanie-2024-kogda-nastupit-primety-interesnye-fakty'
    text = get_article(url)
    print(text)
