import requests
from bs4 import BeautifulSoup
from csv import writer

with open('rokomari.csv','w') as csv_file:
    header=['Book','Author','Available','Price']
    csv_writer=writer(csv_file)
    csv_writer.writerow(header)
    res=requests.get('https://www.rokomari.com/book/category/90/%E0%A6%87%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%A8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%82?ref=mm_p13')
    soup=BeautifulSoup(res.content,'html5lib')
    found=soup.find_all('div',attrs={'class':'col-4 col-xl-3'})
    for i in range(1,100):

        

        for book in found:
            wrapper=book.find('div',attrs={'class':'book-list-wrapper'})
            try:
                info=wrapper.find('div',attrs={'class':'book-text-area'})
                try:
                    titles=info.find('p',attrs={'class':'book-title'}).text
                    author=info.find('p',attrs={'class':'book-author'}).text
                    available=info.find('p',attrs={'class':'book-status text-capitalize'}).text
                    price=info.find('p',attrs={'class':'book-price'}).span.text
                    csv_writer.writerow([titles,available,price])
                except:
                    pass
            except:
                pass
        query={'page':str(i)}
        res=requests.get('https://www.rokomari.com/book/category/90/%E0%A6%87%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%A8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%82?ref=mm_p13',params=query)
        soup=BeautifulSoup(res.content,'html5lib')
        found=soup.find_all('div',attrs={'class':'col-4 col-xl-3'})
    print('done')


        


