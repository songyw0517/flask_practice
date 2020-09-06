from bs4 import BeautifulSoup
import requests

def get_keyword_number(keyword):
    #keyword = "나루토" 
    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    # 웹 요청
    res = requests.get(url, headers=headers)

    #print(type(res.text))

    # 구문 분석 - 파싱
    soup = BeautifulSoup(res.text, 'lxml')
    #print(type(soup))

    # 원하는 것 찾기
    number = soup.select_one('#result-stats').text
    print(number)

    # 필요한 부분만 찾기
    print(number[number.find('약')+2:number.rfind('개')].replace(',',''))
    number = int(number[number.find('약')+2:number.rfind('개')].replace(',',''))
    print(number)

    # #result-stats

    return number

if __name__ == "__main__":
    print(get_keyword_number('침착맨?'))