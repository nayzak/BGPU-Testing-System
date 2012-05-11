(function() {
  $(function() {
    var updateComplexityFields, updateModuleFields, updateQuestionList, updateSubjectFields;
    $('.field-list-item .remove-item').live('click', function() {
      $(this).parent().remove();
      return false;
    });
    $('.field-list-item .add-item').live('click', function() {
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
    $.ajax_loader = $('<i class="ajax-loader">');
    $.ajax_loader.hide();
    $('form select#group_id').after($.ajax_loader);
    $('form select#organization_id').live('change', function() {
      var org_id, select;
      org_id = $(this).find('option:selected').attr('value');
      select = $('form select#group_id');
      $.ajax_loader.show();
      select.prop('disabled', true);
      $.ajax({
        url: '/admin/student/updatelist',
        data: org_id,
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len;
          if (response[0]) {
            select.empty();
          }
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            select.append('<option value="' + r.group_id + '">' + r.name + '</option>');
          }
          $.ajax_loader.hide();
          return select.prop('disabled', false);
        }
      });
      return false;
    });
    updateQuestionList = function() {
      var complexity, module, select, subject, type;
      select = $('form select#questions_list');
      type = $('form select#type').find('option:selected').attr('value');
      subject = $('form select#subject').find('option:selected').attr('value');
      module = $('form select#module').find('option:selected').attr('value');
      complexity = $('form select#complexity').find('option:selected').attr('value');
      $.ajax({
        url: '/admin/template/updateQuestionList',
        data: {
          type: type,
          subject: subject,
          module: module,
          complexity: complexity
        },
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len, _results;
          select.empty();
          _results = [];
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            _results.push(select.append('<option value="' + r.i_id + '">' + r.body + '</option>'));
          }
          return _results;
        }
      });
      return false;
    };
    updateComplexityFields = function() {
      var module, select, subject, type;
      select = $('form select#complexity');
      type = $('form select#type').find('option:selected').attr('value');
      subject = $('form select#subject').find('option:selected').attr('value');
      module = $('form select#module').find('option:selected').attr('value');
      $.ajax({
        url: '/admin/template/updateComplexityFields',
        data: {
          type: type,
          subject: subject,
          module: module
        },
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len;
          select.empty();
          select.append('<option value="none">Любая</option>');
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            select.append('<option value="' + r.complexity + '">' + r.complexity + '</option>');
          }
          return updateQuestionList();
        }
      });
      return false;
    };
    updateModuleFields = function() {
      var select, subject, type;
      select = $('form select#module');
      type = $('form select#type').find('option:selected').attr('value');
      subject = $('form select#subject').find('option:selected').attr('value');
      $.ajax({
        url: '/admin/template/updateModuleFields',
        data: {
          type: type,
          subject: subject
        },
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len;
          select.empty();
          select.append('<option value="none">Любая</option>');
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            select.append('<option value="' + r.module + '">' + r.module + '</option>');
          }
          return updateComplexityFields();
        }
      });
      return false;
    };
    updateSubjectFields = function() {
      var select, type;
      select = $('form select#subject');
      type = $('form select#type').find('option:selected').attr('value');
      $.ajax({
        url: '/admin/template/updateSubjectFields',
        data: {
          type: type
        },
        dataType: "json",
        type: "POST",
        success: function(response) {
          var r, _i, _len;
          select.empty();
          select.append('<option value="none">Любой</option>');
          for (_i = 0, _len = response.length; _i < _len; _i++) {
            r = response[_i];
            select.append('<option value="' + r.subject + '">' + r.subject + '</option>');
          }
          return updateModuleFields();
        }
      });
      return false;
    };
    $('form select#type').live('change', updateSubjectFields);
    $('form select#subject').live('change', updateModuleFields);
    $('form select#module').live('change', updateComplexityFields);
    $('form select#complexity').live('change', updateQuestionList);
    return $('form select#questions_list').live('change', function() {
      return console.log("asd");
    });
  });
}).call(this);
