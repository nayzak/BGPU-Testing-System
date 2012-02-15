# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route, role_required
from application.models.admin import Admin
from application.forms.manage_admin import CreateAdminForm, EditAdminForm
from tornado.web import HTTPError


@route('/admin')
class IndexHandler(BaseRequest):
    title = 'Панель управления'
    template = '/admin/index.html'

    @role_required('tutor')
    def get(self):
        self.render_template(self.template, title=self.title)


@route('/admin/init')
class CreateAdminHandler(BaseRequest):
    title = 'Регистрация администратора'
    template = '/admin/create_admin.html'

    def get(self):
        if Admin.is_admin_created():
            self.flash.notice = 'Администратор уже зарегистрирован.'
            self.redirect('/admin')
            return
        self.render_template(self.template, form=CreateAdminForm(), title=self.title)

    def post(self):
        if Admin.is_admin_created():
            self.redirect('/admin')

        form = CreateAdminForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, form=form, title=self.title)

        Admin.create_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data,
            form.password.data
        )

        self.flash.success = 'Администратор успешно зарегистрирован. Войдите в систему.'
        self.redirect('/admin/login')


@route('/admin/profile/edit')
class EditAdminHandler(BaseRequest):
    title = 'Редактирование администратора'
    template = '/admin/create_admin.html'

    @role_required('admin')
    def get(self):
        if self.current_user['_type'] != 'Admin':
            raise HTTPError(403)
        form = EditAdminForm(
            userid=self.current_user._id,
            email=self.current_user.email,
            first_name=self.current_user.name.first,
            last_name=self.current_user.name.last,
            middle_name=self.current_user.name.middle,
        )
        self.render_template(self.template, form=form, title=self.title)

    @role_required('admin')
    def post(self):
        if self.current_user['_type'] != 'Admin':
            raise HTTPError(403)
        form = EditAdminForm(self.request.arguments)
        if not form.validate():
            self.render_template(self.template, form=form, title=self.title)
            return
        Admin.edit_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data
        )
        self.flash.success = 'Профиль администратора успешно сохранен.'
        self.redirect('/admin')
