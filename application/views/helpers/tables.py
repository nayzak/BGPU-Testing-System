#coding: utf-8
from whirlwind.view.paginator import Paginator
LINKS = {
    'remove': {
        'title': 'Удалить',
        'icon': 'icon-trash'
    },
    'edit': {
        'title': 'Редактировать',
        'icon': 'icon-pencil'
    },
    'view': {
        'title': 'Подробный просмотр',
        'icon': 'icon-list-alt'
    },
}


def render_data_list(data, fields):
    table = '<table class="table table-striped table-bordered">'
    table += '<thead><tr>'
    for field in [v for k, v in fields.items() if k != 'links']:
        table += '<th>{}</th>'.format(field)
    if 'links' in fields:
        table += '<th>{}</th>'.format('Действия')
    table += '</tr></thead><tbody>'
    for doc in data:
        table += '<tr>'
        for field in fields:
            if field != 'links':
                field = field.split('.')
                val = doc
                for f in field:
                    if type(val).__name__ == 'dict':
                        val = val[f]
                    elif type(val).__name__ == 'list' and len(val):
                        val = val[0][f]
                    else:
                        val = 'n/a'
                table += '<td>{}</td>'.format(val)
        if 'links' in fields:
            table += '<td>'
            for type_, link in fields['links'].items():
                link = link[0].format(*[doc[key] for key in link[1:]])
                table += '<a href="{}" title="{}" class="action"><i class="{}"></i></a>'.format(link, LINKS[type_]['title'], LINKS[type_]['icon'])
            table += '</td>'

        table += '</tr>'
    table += '</tbody></table>'

    return table


class Paginator(Paginator):
    def __init__(self, collection, url, page_number=0, limit=20):
        total = collection.count()
        super(Paginator, self).__init__(collection, page_number, limit, total)
        self.url = url

    @property
    def has_next(self):
        return self.current_page != self.page_count - 1

    def build_url(self, page_num):
        import re

        #check if there is a query string
        if self.url.find('?') != -1:
            if re.search(r'page=\d', self.url) != None:
                page_str = "page=%d" % page_num
                return re.sub(r'page=\d+', page_str, self.url)
            else:
                return "%s&page=%d" % (self.url, page_num)

        else:
            return "%s?page=%d" % (self.url, page_num)

    def __unicode__(self):
        paginator = '<div class="pagination"><ul>'

        class_ = '' if self.has_previous else 'disabled'
        link = self.build_url(self.previous_page) if self.has_previous else '#'
        paginator += '<li class="{}"><a href="{}">«</a></li>'.format(class_, link)

        for i in range(1, self.page_count):
            class_ = 'active' if i == self.current_page else ''
            link = self.build_url(i - 1)
            paginator += '<li class="{}"><a href="{}">{}</a></li>'.format(class_, link, i)

        class_ = '' if self.has_next else 'disabled'
        link = self.build_url(self.next_page) if self.has_next else '#'
        paginator += '<li class="{}"><a href="{}">»</a></li>'.format(class_, link)

        paginator += '</ul></div>'
        return paginator

    def __str__(self):
        return self.__unicode__()
