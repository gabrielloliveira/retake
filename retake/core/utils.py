from bs4 import BeautifulSoup
from django.conf import settings

PROCESS_01 = f"{settings.BASE_DIR / 'data'}/processo-01.html"
PROCESS_02 = f"{settings.BASE_DIR / 'data'}/processo-02.html"


class ProcessData:
    def __init__(self, filename):
        self.filename = filename
        self.html = self.get_data_from_file()

    def get_data_from_file(self):
        with open(self.filename) as process:
            bs = BeautifulSoup(process, 'html.parser')
        return bs

    @property
    def number(self):
        tag = self.html.find("h4", {"class": "mr-auto"})
        return list(tag.children)[0].strip()

    @property
    def class_name(self):
        tag = self.html.find_all('h6', {'class': 'text-muted'})[0]
        children = tag.parent()[-1]
        return children.text

    @property
    def subject(self):
        tag = self.html.find_all('h6', {'class': 'text-muted'})[2]
        children = tag.parent()[-1]
        return children.text

    @property
    def judge(self):
        tag = self.html.find_all('h6', {'class': 'text-muted'})[6]
        children = tag.parent()[-1]
        return children.text

    @property
    def parts(self):
        parts = list()
        ul = self.html.find_all('ul')[0]
        li_list = ul.find_all('li')
        for li in li_list:
            parts_list = li.find('span', {'class': 'mr-auto'})
            parts_list = parts_list.text.split("Advogados:")
            parts_list = [x.strip() for x in parts_list]
            category = li.find('span', {'class': 'badge badge-warning'}).text.strip()

            parts.append(dict(part=parts_list[0], category=category))
            if len(parts_list) > 1:
                parts.append(dict(part=parts_list[-1], category=f"ADVOGADOS {category}"))

        return parts
