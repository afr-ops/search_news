from requests_html import HTMLSession
#import urllib.parse
import pandas as pd

class GoogleSearchNews:
    def paginate(self, url):
        session = HTMLSession()
        header = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                }
        resp = session.get(url, headers = header)
        yield resp
        # next_page = resp.html.find("a#pnnext") #a#pnnexr es el id del link de next page
        # print(next_page)
        # if next_page is None: return
        # next_page_url = urlib.parse.urljoin("https://news.google.com/", next_page[0].attrs["href"])
        # yield from self.paginate(next_page_url, url)

    def scrape_articles(self):
        pages = self.paginate('https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2l2aGNPWkJoR3Y2ZF9acVR0UDRDZ0FQAQ?hl=es-419&gl=AR&ceid=AR%3Aes-419')
        NewList = []
        for page in pages:
            articles = page.html.find("article.MQsxIb")
            for article in articles:
                title = article.find("h4.ipQwMb")[0].text
                source = article.find("div.wsLqz")[0].text
                date = article.find("div.SVJrMe")[0].text
                # links = article.attrs["href"]

                NewList.append({

                            "Title": title,
                            "Source": source,
                            "Date": date
                })    

        return NewList                    
        # print(NewList)
                # print('----------------------------------------------') 
                # print(title)
                # print(source)
                # print(date)
                # print(links)
    def output_data(self, NewList):
        data_news = pd.DataFrame(NewList)
        # data_news.to_csv("GoogleNews.csv", index=False)
        data_news.to_html("GoogleNews.html", index=False)
        print(data_news)            

news = GoogleSearchNews()
data = news.scrape_articles()
news.output_data(data)












# from pygooglenews import GoogleNews

# def get_title(search):
#     gn = GoogleNews(Country = 'AR')
#     search = gn.search(search)
#     newsitem = search('entities')

#     for item in newsitem:
#         print(item.link)
#     return

# get_title('Messi')


# # DEPRECATED - - - pip install pygooglenews==0.1.0