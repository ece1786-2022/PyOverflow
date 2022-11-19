import requests
from bs4 import BeautifulSoup
import json


def get_sub_topics(bes, depth=0, name=None):
    # subtopics = bes.find_all("div", class_="toctree-wrapper compound")
    if depth > 2:
        return []
    # if depth == 0:
    topics = bes.find_all(f"h{depth + 1}")
    # print(topics)
    if topics:
        # chapters = texts.find_all("a")
        topic_lst = []
        for topic in topics:
            # topic_info = topic.find_all(lambda tag: tag.name == 'a')
            # print(topic_info)
            # if topic_info:
            topic_dict = {}
            # topic_url = url.removesuffix("index.html") + topic_info[0].get('href')
            # topic_name = topic_info[0].get('href')[1:]
            topic_name = topic.text[:-1]
            # print(topic_name)
            topic_dict['Topic'] = topic_name.replace("\u2014 ", "")
            # topic_dict['content'] = [p.text for p in bes.find_all("p")]
            # topic_dict['url'] = topic_url
            # topic_dict['content'] = topic_info[0].find("p").text
            # print(topic)
            # print(topic_name.lower().replace(" ", "-"))
            sec_name = topic_name.lower().replace(" ", "-")
            sec_name = sec_name.replace(",", "")
            sec_name = sec_name.replace("—", "")
            sec_name = sec_name.replace("--", "-")
            # print(sec_name)
            topics_section = bes.find("section", id=sec_name)
            topic_dict['content'] = [p.text for p in topics_section.find_all("p", recursive=False)]
            notes_ol = topics_section.find("ol", recursive=False)
            if notes_ol:
                notes_content = [p.text for p in notes_ol.find_all("li", recursive=False)]
                topic_dict['content'].extend(notes_content)
            functions = topics_section.find_all("dl", class_="py method", recursive=False)
            func_lst = []
            if functions:
                for func in functions:
                    func_dict = {}
                    func_name = func.find("dt").text[:-1].replace("\n", "")
                    func_dict['name'] = func_name
                    dd = func.find("dd")
                    func_dict['content'] = [p.text for p in dd.find_all("p", recursive=False)]
                    func_dict['code_demo'] = [p.text for p in dd.find_all("div", recursive=False)]
                    if func_dict['code_demo'] and func_dict['code_demo'][-1][:5] == "\nNew ":
                        func_dict['code_demo'] = func_dict['code_demo'][:-1]
                    func_lst.append(func_dict)
            topic_dict['functions'] = func_lst
            topic_dict['code_demo'] = [p.text for p in topics_section.find_all("div", recursive=False)]
            # topic_dict['code_demo'] = [p.text for p in topics_section.find_all("pre", recursive=False)]
            # print(topics_section)
            topic_dict['Subtopics'] = get_sub_topics(topics_section, depth + 1, topic_name)
            topic_lst.append(topic_dict)
            # print(topic_name, topic_url)
            # get_sub_topics(topic_url)
        # print(topic_lst)
        return topic_lst
    else:
        # print("No subtopics found!")
        return []

if __name__ == '__main__':
    url = "https://docs.python.org/3/library/stdtypes.html"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    req = requests.get(url=url,headers = header)
    req.encoding = 'utf-8'
    html = req.text
    bes = BeautifulSoup(html, "lxml")
    # topics_section = bes.find("section", id="built-in-types")
    # print(topics_section)
    data = get_sub_topics(bes)
    with open("built-in-exceptions.json", "w") as final:
        json.dump(data, final)
