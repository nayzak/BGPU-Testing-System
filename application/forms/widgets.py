#coding: utf-8
from wtforms.widgets import HTMLString, html_params


class TypeheadInput(object):
    def __init__(self, autocomplete_list):
        self.autocomplete_list = '["{}"]'.format('","'.join(autocomplete_list))

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', 'text')
        kwargs.setdefault('data-provide', 'typeahead')
        kwargs.setdefault('data-source', self.autocomplete_list)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        return HTMLString(u'<input %s />' % html_params(name=field.name, **kwargs))


class FieldListWidget(object):
    def __init__(self):
        pass

    def render_field_list_item(self, item):
        html = '<div class="field-list-item form-inline" id="%s">' % item.id
        html += '<a class="add-item" title="Добавить поле"><i class="icon-plus-sign"></i></a>'
        html += '<a class="remove-item" title="Удалить поле"><i class="icon-remove-sign"></i></a>'
        html += self.render_subfields(item)
        html += '</div>'
        return html

    def render_subfields(self, field):
        html = ''
        if hasattr(field, '__iter__'):
            for subfield in field:
                if type(subfield).__name__ == 'FieldList':
                    html += self(subfield, display_label=True)
                else:
                    html += self.render_subfields(subfield)
        else:
            if field.flags.required:
                field.label.text += ' *'
            html += '<div class="control-group' + (' error' if len(field.errors) else '') + '">'
            html += '<div class="controls">'
            html += unicode(field(placeholder=field.label.text))
            if len(field.errors):
                html += '<span class="help-inline">'
                for index, error in enumerate(field.errors):
                    html += error + (' | ' if index < (len(field.errors) - 1) else '')
                html += '</span>'
            html += '<p class="help-block">{}</p>'.format(field.description)
            html += '</div></div>'
        return html

    def __call__(self, field_list, display_label=False, **kwargs):
        html = '<div class="control-group">'
        html += unicode(field_list.label) if display_label else ''
        for item in field_list:
            html += self.render_field_list_item(item)
        html += '</div>'
        return html


class TabbedFieldsWidget(object):
    def __init__(self):
        self.active = 0

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = ['<div class="tabbable tabs-bottom" {}>'.format(html_params(**kwargs))]
        html.append('<ul class="nav nav-tabs">')
        for i, subfield in enumerate(field):
            _class = 'class="active"' if i == self.active else ''
            html.append('<li {}><a href="#{}" data-toggle="tab">{}</a></li>'.format(_class, i, field.tabs[i]))
        html.append('</ul>')
        html.append('<div class="tab-content">')
        for i, subfield in enumerate(field):
            _class = ' active' if i == self.active else ''
            content = unicode(subfield)
            html.append('<div class="tab-pane{}" id="{}">{}</div>'.format(_class, i, content))
        html.append('</div>')
        html.append('</div>')
        html.append('<input type="hidden" name="{}" value="0"/>'.format('selected-tab-' + kwargs['id']))
        return HTMLString(''.join(html))
