(function() {
  $(function() {
    $('.control-group .remove-button').live('click', function() {
      $(this).parent().remove();
      return false;
    });
    return $('.control-group .add-button').live('click', function() {
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
        if (el.attr('id')) {
          el.attr('id', el.attr('id').replace(t_id, id));
        }
        if (el.attr('name')) {
          el.attr('name', el.attr('name').replace(t_id, id));
        }
        el.attr('value', '');
      }
      template.after(clone);
      return false;
    });
  });
  $('form select#organization_id').live('change', function() {
    var org_id;
    org_id = $(this).find('option:selected').attr('value');
    $.ajax({
      url: '/admin/student/updatelist',
      data: org_id,
      dataType: "json",
      type: "POST",
      success: function(response) {
        var r, select, _i, _len, _results;
        select = $('form select#group_id');
        if (response[0]) {
          select.empty();
        }
        _results = [];
        for (_i = 0, _len = response.length; _i < _len; _i++) {
          r = response[_i];
          _results.push(select.append('<option value="' + r.group_id + '">' + r.name + '</option>'));
        }
        return _results;
      }
    });
    return false;
  });
}).call(this);
