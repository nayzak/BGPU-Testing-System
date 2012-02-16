#coding: utf-8
from whirlwind.view.paginator import Paginator
from mongokit.document import Document
LINKS = {
    'remove': {
        'title': 'Удалить',
        'icon': 'icon-trash'
    },
    'edit': {
        'title': 'Редактировать',
        'icon': 'icon-edit'
    },
    'view': {
        'title': 'Подробный просмотр',
        'icon': 'icon-list-alt'
    },
    'chpass': {
        'title': 'Сменить пароль',
        'icon': 'icon-qrcode'
    }
}


def render_data_list(data, fields, actions, url):
    table = '<table class="table table-striped table-bordered">'
    table += '<thead><tr>'
    for field in fields:
        db_field, field, render_fn = field[0], field[1], field[2] if len(field) > 2 else None
        table += '<th><a href="{}" title="Сортировать">{}</a></th>'.format(_generate_sorter_link(url, db_field), field)
    table += '<th>Действия</th>'
    table += '</tr></thead><tbody>'
    for doc in data:
        table += '<tr>'
        for field in fields:
            db_field, field, render_fn = field[0], field[1], field[2] if len(field) > 2 else None
            field = db_field.split('.')
            val = doc
            for f in field:
                try:
                    is_callable = callable(val.__getattribute__(f))
                except:
                    is_callable = False
                if is_callable:
                    val = val.__getattribute__(f)()
                elif hasattr(val, '__getitem__') and f in val:
                    val = val[f]
                elif type(val).__name__ == 'list' and len(val):
                    val = val[0][f]
                else:
                    val = ''
            if render_fn:
                val = render_fn(val, doc)
            table += '<td>{}</td>'.format(val)
        table += '<td>'
        for type_, link in actions.items():
            link = link[0].format(*[doc[key] for key in link[1:]])
            table += '<a href="{}" title="{}" class="action"><i class="{}"></i></a>'.format(link, LINKS[type_]['title'], LINKS[type_]['icon'])
        table += '</td>'

        table += '</tr>'
    table += '</tbody></table>'

    return table


def _generate_sorter_link(url, db_field):
    import re
    if url.find('?') == -1:
        return '{}?sort={}&dest={}'.format(url, db_field, 1)
    r = re.search(r'sort=([A-Za-z0-9._-]+)', url)
    if r and db_field == r.groups()[0]:
        r = re.search(r'dest=([-1]+)', url)
        if r:
            return url.replace(r.group(), 'dest=' + str(-1 * int(r.groups()[0])))
        return url
    elif r:
        return url.replace(r.group(), 'sort=' + db_field)
    else:
        return '{}&sort={}&dest={}'.format(url, db_field, 1)


class Paginator(Paginator):
    def __init__(self, collection, url, page_number=0, limit=20):
        total = collection.count()
        super(Paginator, self).__init__(collection, page_number, limit, total)
        self.url = url

    @property
    def has_next(self):
        return self.current_page != self.page_count

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
        if self.page_count == 1:
            return ''

        paginator = '<div class="pagination"><ul>'

        class_ = '' if self.has_previous else 'disabled'
        link = self.build_url(self.previous_page) if self.has_previous else '#'
        paginator += '<li class="{}"><a href="{}">«</a></li>'.format(class_, link)

        for i in range(0, self.page_count):
            class_ = 'active' if i == self.current_page - 1 else ''
            link = self.build_url(i)
            paginator += '<li class="{}"><a href="{}">{}</a></li>'.format(class_, link, i + 1)

        class_ = '' if self.has_next else 'disabled'
        link = self.build_url(self.next_page) if self.has_next else '#'
        paginator += '<li class="{}"><a href="{}">»</a></li>'.format(class_, link)

        paginator += '</ul></div>'
        return paginator

    def __str__(self):
        return self.__unicode__()
