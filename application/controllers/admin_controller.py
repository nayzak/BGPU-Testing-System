# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from lib.decorators import role_required
from application.models.admin import Admin
from application.forms.manage_admin import CreateAdminForm, EditAdminForm
from application.forms.manage_tutor import ChpassForm, AdminChpassForm
from tornado.web import HTTPError
from pymongo.objectid import ObjectId


@route('/admin')
class IndexHandler(BaseRequest):
    title = 'Панель управления'
    template = '/admin/index.html'

    @role_required('tutor')
    def get(self):
        self.render_template()


@route('/admin/init')
class CreateAdminHandler(BaseRequest):
    title = 'Регистрация администратора'
    template = '/admin/create_admin.html'

    def get(self):
        if Admin.is_admin_created():
            self.flash.notice = 'Администратор уже зарегистрирован.'
            self.redirect('/admin')
            return
        self.render_template(form=CreateAdminForm())

    def post(self):
        if Admin.is_admin_created():
            self.redirect('/admin')

        form = CreateAdminForm(self.request.arguments)
        if not form.validate():
            self.render_template(form=form)

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
        self.render_template(form=form)

    @role_required('admin')
    def post(self):
        if self.current_user['_type'] != 'Admin':
            raise HTTPError(403)
        form = EditAdminForm(self.request.arguments)
        if not form.validate():
            self.render_template(form=form)
            return
        Admin.edit_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data
        )
        self.flash.success = 'Профиль администратора успешно сохранен.'
        self.redirect('/admin')


@route('/admin/profile/show')
class ViewTutorHandler(BaseRequest):
    title = 'Профиль администратора'
    template = '/admin/view_tutor.html'

    @role_required('tutor')
    def get(self):
        admin = Admin.get_admin()
        self.render_template(tutor=admin)


@route(r'/admin/profile/chpass/([0-9a-f]{24})')
class ChpassHandler(BaseRequest):
    title = 'Смена пароля'
    template = '/admin/create_admin.html'

    @role_required('tutor')
    def get(self, _id):
        _id = ObjectId(_id.decode('hex'))
        if self.current_user['_type'] != 'Admin' and self.current_user['_id'] != _id:
            raise HTTPError(403)
        form = None
        if self.current_user['_id'] == _id:
            form = ChpassForm(userid=unicode(_id))
        elif self.current_user['_type'] == 'Admin':
            form = AdminChpassForm()
        else:
            raise HTTPError(403)
        self.render_template(form=form)

    @role_required('tutor')
    def post(self, _id):
        _id = ObjectId(_id.decode('hex'))
        if self.current_user['_type'] != 'Admin' and self.current_user['_id'] != _id:
            raise HTTPError(403)
        form = None
        if self.current_user['_id'] == _id:
            form = ChpassForm(self.request.arguments)
        elif self.current_user['_type'] == 'Admin':
            form = AdminChpassForm(self.request.arguments)
        else:
            raise HTTPError(403)
        if not form.validate():
            self.render_template(form=form)
            return
        Admin.chpass(_id, form.data['password'])
        self.flash.success = 'Пароль успешно изменен'
        if self.current_user['_id'] == _id:
            self.redirect('/logout')
        else:
            Admin.destroy_session(_id)
            self.redirect('/admin/tutor/list')
