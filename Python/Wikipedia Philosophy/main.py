from os import system

#Install packages
system('pip install wikipedia')
system('pip install beautifulsoup4')
system('pip install requests')

#Import libraries
from wikipedia import search, page
from bs4 import BeautifulSoup
from requests import get
from time import sleep

#Returns the first link in the main text that is not in a bracket
def firstLink(link):
    request = get(link)
    soup = BeautifulSoup(request.content, 'html.parser')
    title = ' '.join(soup.find('title').find(text = True).split()[:-2])
    soup = soup.find('div', id = 'mw-content-text')
    for paragraph in soup.find_all('p'):
        paragraphText = paragraph.find(text = True)
        for link in paragraph.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href') and tag['href'] != None):
            url = link['href']
            if url[:6] == '/wiki/' and link in paragraph and '.' not in url:
                prefix = str(paragraph).split(str(link), 1)[0]
                if prefix.count('(') == prefix.count(')'):
                    return 'https://www.wikipedia.org' + url, title

#Main function to start the process
def main(currURL):
    visited = []
    completed = set()

    while len(visited) < maxVisits:
        currURL, title = firstLink(currURL)
        if title in completed:
            return -1
            break
        completed.add(title)
        visited.append(title)
        if currURL == 'https://www.wikipedia.org/wiki/Philosophy':
            break
        sleep(2)
    
    visited.append('Philosophy')
    return visited

maxVisits = 50
randomPage = 'https://wikipedia.org/wiki/Special:Random'

#Driver Code
if __name__ == '__main__':
    if input('Random(R) / Manual(M) Starting Page: ').upper() == 'R':
        currURL = randomPage
    else:
        currURL = page(search(input('Starting Page: '), 1)[0]).url
    visited = main(currURL)
    if visited == -1:
        print('Circular Loop entered')
    else:
        if len(visited) == maxVisits:
            print('Crawl was stopped. Took too long')
        else:
            for i, r in enumerate(visited):
                print(f'{i + 1}. {r}')
            print(f'Steps: {len(visited)}')