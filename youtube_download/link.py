from bs4 import BeautifulSoup as bs

# manually extract the scroll all the way down html part, exclude those unnecessary
def get_links():
    url = 'www.youtube.com'
    html_document = open('geohotz.html','r')

    soup = bs(html_document, 'html.parser')
    results = soup.find_all(id='video-title')
    links = []
    for result in results:
        links.append([url+result['href'],result.get_text()])
    return links

if __name__ == '__main__':
    print(get_links())

