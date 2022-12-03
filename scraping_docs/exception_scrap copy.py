import requests
from bs4 import BeautifulSoup
import json


def get_sub_topics(bes, depth=0, name=None):
    # subtopics = bes.find_all("div", class_="toctree-wrapper compound")
    #if depth > 2:
        #return []
    # if depth == 0:
    topics = bes.find_all(f"h{depth + 1}")
    topic_name = topics[0].text[:-1]
    sec_name = topic_name.lower().replace(" ", "-")
    sec_name = sec_name.replace(",", "")
    sec_name = sec_name.replace("—", "")
    sec_name = sec_name.replace("--", "-")
    tag=bes.body
    # print(topics)
    if topics:
        # chapters = texts.find_all("a")
        topic_lst = []
        body=[]
        topic_dict = {}
        topic_dict['topic']=sec_name
        for string in tag.stripped_strings:
            # topic_info = topic.find_all(lambda tag: tag.name == 'a')
            # print(topic_info)
            # if topic_info:
            
            body.append(string)
            
            # topic_url = url.removesuffix("index.html") + topic_info[0].get('href')
            # topic_name = topic_info[0].get('href')[1:]
            
            # print(topic_name)
            
            # topic_dict['content'] = [p.text for p in bes.find_all("p")]
            # topic_dict['url'] = topic_url
            # topic_dict['content'] = topic_info[0].find("p").text
            # print(topic)
            # print(topic_name.lower().replace(" ", "-"))
        topic_dict['content']=body
        
            
        return topic_dict


if __name__ == '__main__':
    url = "https://docs.python.org/3/library/functions.html"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    req = requests.get(url=url,headers = header)
    req.encoding = 'utf-8'
    html = req.text
    bes = BeautifulSoup(html, "lxml")
    # topics_section = bes.find("section", id="built-in-types")
    # print(topics_section)
    data = get_sub_topics(bes)
    with open("functions.json", "w") as final:
        json.dump(data, final)
