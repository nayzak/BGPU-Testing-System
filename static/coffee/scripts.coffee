$ ->
    #удалить элемент из FieldList
    $('.control-group .remove-button').live 'click', ->
        block = $(@).parent()
        block.prev().find('> .add-button').show()
        block.prev().find('> .remove-button').show()
        block.remove()
        return false

    #добавить элемент в FieldList
    $('.control-group .add-button').live 'click', ->
        template = $(@).parent()
        clone = template.clone()
        t_id = template.attr 'id'
        id = t_id.split('-')
        id[id.length - 1] = parseInt(id[id.length - 1]) + 1
        id = id.join('-')
        clone.attr('id', id)
        for el in clone.find('[id^=' + t_id + ']')
            $(el).attr('id', $(el).attr('id').replace(t_id, id))
        template.after(clone)
        template.find('> .add-button').fadeOut()
        template.find('> .remove-button').fadeOut()
        return false