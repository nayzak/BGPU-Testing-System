def render_form(form):
    html = '<form class="form-horizontal", method="POST">'
    html += '<fieldset>'
    html += '<legend>{}</legend>'.format(form.title)
    for field in form:
        if type(field).__name__ is 'SubmitField':
            html += '<div class="form-actions">'
            html += unicode(field(class_='btn btn-success'))
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
