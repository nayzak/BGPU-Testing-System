#coding: utf-8
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
