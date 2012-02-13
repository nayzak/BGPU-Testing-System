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