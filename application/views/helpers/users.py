#coding: utf:8


def render_profile_menu(user):
    if not user:
        return ''
    name = ' '.join((user.name.last, user.name.first))
    ch_pass = '/admin/profile/chpass/{}'.format(user._id)
    logout = '/logout'
    if user._type == 'Admin':
        show = '/admin/profile/show'
        edit = '/admin/profile/edit'
    elif user._type == 'Tutor':
        show = '/admin/tutor/{}'.format(user._id)
        edit = '/admin/tutor/edit/{}'.format(user._id)
    else:
        return ''
    header = '<ul class="nav pull-right">\
                <li class="dropdown">\
                   <a href="#" class="dropdown-toggle" data-toggle="dropdown">{}<b class="caret"></b></a>\
                   <ul class="dropdown-menu">\
                      <li><a href="{}"><i class="icon-user"></i>&nbsp;Просмотр</a></li>\
                      <li><a href="{}"><i class="icon-edit"></i>&nbsp;Редактировать</a></li>\
                      <li><a href="{}"><i class="icon-qrcode"></i>&nbsp;Сменить пароль</a></li>\
                      <li class="divider"></li>\
                      <li><a href="{}"><i class="icon-off"></i>&nbsp;Выйти</a></li>\
                   </ul>\
                </li>\
              </ul>'.format(name, show, edit, ch_pass, logout)
    return header
