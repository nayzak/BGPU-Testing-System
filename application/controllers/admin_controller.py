# coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route, role_required
from application.models.admin import Admin
from application.forms.manage_admin import CreateAdminForm, EditAdminForm
from tornado.web import HTTPError


@route('/admin')
class IndexHandler(BaseRequest):
    @role_required('admin')
    def get(self):
        self.render_template('/admin/index.html', user=self.current_user)


@route('/admin/init')
class CreateAdminHandler(BaseRequest):
    def get(self):
        if Admin.is_admin_created():
            self.redirect('/admin/login')

        self.render_template('/admin/create_admin.html', form=CreateAdminForm())

    def post(self):
        if Admin.is_admin_created():
            self.redirect('/admin/login')

        form = CreateAdminForm(self.get_all_arguments())

        if not form.validate():
            self.render_template('/admin/create_admin.html', form=form)

        Admin.create_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data,
            form.password.data
        )

        self.redirect('/admin/login')


@route('/admin/profile/edit')
class EditAdminHandler(BaseRequest):
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
        self.render_template('/admin/edit_admin.html', form=form)

    @role_required('admin')
    def post(self):
        if self.current_user['_type'] != 'Admin':
            raise HTTPError(403)
        form = EditAdminForm(self.request.arguments)
        if not form.validate():
            self.render_template('/admin/edit_admin.html', form=form)
            return
        Admin.edit_admin(
            form.first_name.data,
            form.last_name.data,
            form.middle_name.data,
            form.email.data
        )
        self.redirect('/admin')
