#coding: utf-8


def render_form(form):
    html = '<form class="form-horizontal" method="POST">'
    html += '<fieldset>'
    html += '<legend>{}</legend>'.format(form.title)
    for field in form:
        if type(field).__name__ is 'SubmitField':
            html += '<div class="form-actions">'
            html += unicode(field(class_='btn btn-success'))
            html += '</div>'
        elif type(field).__name__ is 'FieldList':
            html += render_field_list(field)
        else:
            if type(field).__name__ is 'HiddenField':
                html += '<div style="display: none;">'
            else:
                html += '<div class="control-group' + (' error' if len(field.errors) else '') + '">'
            if field.flags.required:
                field.label.text += ' *'
            html += unicode(field.label)
            html += '<div class="controls">'
            html += unicode(field)
            if len(field.errors):
                html += '<span class="help-inline">'
                for index, error in enumerate(field.errors):
                    html += error + (' | ' if index < (len(field.errors) - 1) else '')
                html += '</span>'
            html += '<p class="help-block">{}</p>'.format(field.description)
            html += '</div>'
            html += '</div>'
    html += '</fieldset>'
    html += '</form>'
    return html


def render_field_list(field_list):
    html = ''
    for form in field_list:
        html += '<div class="control-group" id="{}">'.format(form.id)
        html += unicode(field_list.label)
        html += '<a class="add-button" href="#" title="Добавить еще одно поле"><i class="icon-plus-sign"></i></a>'
        html += '<a class="remove-button" href="#" title="Удалить поле"><i class="icon-remove-sign"></i></a>'
        html += '<div class="controls ' + (form.class_ if hasattr(form, 'class_') else '') + '">'
        for field in form:
            if type(field).__name__ is 'FieldList':
                html += render_field_list(field)
            else:
                if type(field).__name__ is 'HiddenField':
                    html += '<div style="display: none;">'
                else:
                    html += '<div class="control-group' + (' error' if len(field.errors) else '') + '">'
                html += '<div class="controls">'
                if field.flags.required:
                    field.label.text += ' *'
                html += unicode(field(placeholder=field.label.text))
                if len(field.errors):
                    html += '<span class="help-inline">'
                    for index, error in enumerate(field.errors):
                        html += error + (' | ' if index < (len(field.errors) - 1) else '')
                    html += '</span>'
                html += '<p class="help-block">{}</p>'.format(field.description)
                html += '</div>'
                html += '</div>'
        html += '</div>'
        html += '</div>'
    return html
