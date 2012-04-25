$ ->
    #удалить элемент из FieldList
    $('.field-list-item .remove-item').live 'click', ->
        $(@).parent().remove()
        return false

    #добавить элемент в FieldList
    $('.field-list-item .add-item').live 'click', ->
        template = $(@).parent()
        tmp_id = template.attr('id').split('-')
        tmp_id.pop()
        tmp_id = tmp_id.join('-')
        template = template.parent().find('>[id^=' + tmp_id + ']:last')
        clone = template.clone()
        t_id = template.attr('id')
        id = t_id.split('-')
        id[id.length - 1] = parseInt(id[id.length - 1]) + 1
        id = id.join('-')
        clone.attr('id', id)
        for el in clone.find('[id^=' + t_id + ']')
            el = $(el)
            el.attr('id', el.attr('id').replace(t_id, id)) if el.attr('id')
            el.attr('name', el.attr('name').replace(t_id, id)) if el.attr('name')
            el.attr('value', '')
        template.after(clone)
        return false


    # фильтер в добавление студента
    $.ajax_loader = $('<i class="ajax-loader">')
    $.ajax_loader.hide()
    $('form select#group_id').after($.ajax_loader)
    $('form select#organization_id').live 'change', () ->
        org_id = $(@).find('option:selected').attr('value')
        select = $('form select#group_id')
        $.ajax_loader.show()
        select.prop('disabled', true)
#@TODO запилить защитную хуету из куков!!!
        $.ajax({
                url: '/admin/student/updatelist',
                data: org_id,
                dataType: "json",
                type: "POST",
                success: (response) ->
                        if (response[0])
                            select.empty()
                        for r in response
                            select.append('<option value="'+r.group_id+'">'+r.name+'</option>')
                        $.ajax_loader.hide()
                        select.prop('disabled', false)
        })
        return false

# фильтры в добавление шаблона
    updateQuestionList = ->
        type = $('form select#type').find('option:selected').attr('value')
        subject = $('form select#subject').find('option:selected').attr('value')
        module = $('form select#module').find('option:selected').attr('value')
        complexity = $('form select#complexity').find('option:selected').attr('value')
        $.ajax({
                url: '/admin/template/updateQuestionList',
                data: {type, subject, module, complexity},
                dataType: "json",
                type: "POST",
                success: (response) ->
                        console.log(response)
        })
        return false

    updateComplexityFields = ->
        select = $('form select#complexity')
        type = $('form select#type').find('option:selected').attr('value')
        subject = $('form select#subject').find('option:selected').attr('value')
        module = $('form select#module').find('option:selected').attr('value')
        $.ajax({
                url: '/admin/template/updateComplexityFields',
                data: {type, subject, module},
                dataType: "json",
                type: "POST",
                success: (response) ->
                        select.empty()
                        select.append('<option value="none">Любая</option>')
                        for r in response
                            select.append('<option value="'+r.complexity+'">'+r.complexity+'</option>')
                        updateQuestionList()
        })
        return false

    updateModuleFields = ->
        select = $('form select#module')
        type = $('form select#type').find('option:selected').attr('value')
        subject = $('form select#subject').find('option:selected').attr('value')
        $.ajax({
                url: '/admin/template/updateModuleFields',
                data: {type, subject},
                dataType: "json",
                type: "POST",
                success: (response) ->
                        select.empty()
                        select.append('<option value="none">Любая</option>')
                        for r in response
                            select.append('<option value="'+r.module+'">'+r.module+'</option>')
                        updateComplexityFields()
        })
        return false

    updateSubjectFields = ->
        select = $('form select#subject')
        type = $('form select#type').find('option:selected').attr('value')
        $.ajax({
                url: '/admin/template/updateSubjectFields',
                data: {type},
                dataType: "json",
                type: "POST",
                success: (response) ->
                        select.empty()
                        select.append('<option value="none">Любой</option>')
                        for r in response
                            select.append('<option value="'+r.subject+'">'+r.subject+'</option>')
                        updateModuleFields()
        })
        return false

# типы
    $('form select#type').live 'change', updateSubjectFields

# предмет
    $('form select#subject').live 'change', updateModuleFields

# дидактическая единица
    $('form select#module').live 'change', updateComplexityFields

# сложность вопроса
    $('form select#complexity').live 'change', updateQuestionList
