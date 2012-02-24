
  $(function() {
    var ajax_loader;
    $('.control-group .remove-button').live('click', function() {
      $(this).parent().remove();
      return false;
    });
    $('.control-group .add-button').live('click', function() {
      var clone, el, id, t_id, template, tmp_id, _i, _len, _ref;
      template = $(this).parent();
      tmp_id = template.attr('id').split('-');
      tmp_id.pop();
      tmp_id = tmp_id.join('-');
      template = template.parent().find('>[id^=' + tmp_id + ']:last');
      clone = template.clone();
      t_id = template.attr('id');
      id = t_id.split('-');
      id[id.length - 1] = parseInt(id[id.length - 1]) + 1;
      id = id.join('-');
      clone.attr('id', id);
      _ref = clone.find('[id^=' + t_id + ']');
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        el = _ref[_i];
        el = $(el);
        if (el.attr('id')) el.attr('id', el.attr('id').replace(t_id, id));
        if (el.attr('name')) el.attr('name', el.attr('name').replace(t_id, id));
        el.attr('value', '');
      }
      template.after(clone);
      return false;
    });
    ajax_loader = $('<i class="ajax-loader">');
    ajax_loader.hide();
    $('form select#group_id').after(ajax_loader);
    return $('form select#organization').live('change', function() {
      var org_id, select;
      org_id = $(this).find('option:selected').attr('value');
      select = $('form select#group_id');
      ajax_loader.show();
      select.prop('disabled', true);
      $.ajax({
        url: '/admin/student/updatelist',
        data: org_id,
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len;
          if (response[0]) select.empty();
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            select.append('<option value="' + r.group_id + '">' + r.name + '</option>');
          }
          ajax_loader.hide();
          return select.prop('disabled', false);
        }
      });
      return false;
    });
  });
