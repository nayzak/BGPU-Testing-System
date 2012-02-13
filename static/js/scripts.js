(function() {
  $(function() {
    $('.control-group .remove-button').live('click', function() {
      var block;
      block = $(this).parent();
      block.prev().find('> .add-button').show();
      block.prev().find('> .remove-button').show();
      block.remove();
      return false;
    });
    return $('.control-group .add-button').live('click', function() {
      var clone, el, id, t_id, template, _i, _len, _ref;
      template = $(this).parent();
      clone = template.clone();
      t_id = template.attr('id');
      id = t_id.split('-');
      id[id.length - 1] = parseInt(id[id.length - 1]) + 1;
      id = id.join('-');
      clone.attr('id', id);
      _ref = clone.find('[id^=' + t_id + ']');
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        el = _ref[_i];
        $(el).attr('id', $(el).attr('id').replace(t_id, id));
      }
      template.after(clone);
      template.find('> .add-button').fadeOut();
      template.find('> .remove-button').fadeOut();
      return false;
    });
  });
}).call(this);
