def render_form(form):
    html = u'<form class="form-horizontal", method="POST">'
    html += u'<fieldset>'
    html += u'<legend>{}</legend>'.format(form.title)
    for field in form:
        if type(field).__name__ is 'SubmitField':
            html += u'<div class="form-actions">'
            html += unicode(field(class_='btn btn-success'))
        else:
            html += u'<div class="control-group' + (' error' if len(field.errors) else '') + '">'
            if field.flags.required:
                field.label.text += u' *'
            html += unicode(field.label)
            html += u'<div class="controls">'
            html += unicode(field)
            if len(field.errors):
                html += '<span class="help-inline">'
                for index, error in enumerate(field.errors):
                    html += error + (' | ' if index < (len(field.errors) - 1) else '')
                html += '</span>'
            html += u'<p class="help-block">{}</p>'.format(field.description)
            html += u'</div>'
        html += u'</div>'
    html += u'</fieldset>'
    html += u'</form>'
    return html
