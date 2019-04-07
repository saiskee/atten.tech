from bs4 import BeautifulSoup

def scrape(text):
    # soup = BeautifulSoup(text, "html.parser")
    # # elements = soup.find_all(" ")
    # i = 0
    # for elem in soup.contents:
    #     try:
    #         print(str(elem['class']))
    #     except:
    #         print("hello")
    #     # elem['class'] = str(elem['class']) + str(i)
    #     i += 1
    return ('<iframe style="position:fixed; top: 0px; left: 0px; height:100vh; width:100vw;y"src='+text+'></iframe>')
