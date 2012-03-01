#coding: utf-8
from lib.request import BaseRequest
from whirlwind.view.decorators import route
from application.forms.login import LoginForm
from application.models.user import User


@route('/admin/login')
class LoginHandler(BaseRequest):
    title = 'Вход в панель управления'
    template = '/admin/login.html'

    def get(self):
        self.render_template(form=LoginForm())

    def post(self):
        form = LoginForm(self.request.arguments)
        print(self.request)
        print(self.request.arguments)
        if not form.validate():
            self.render_template(form=form)
            return

        user = User.get_by('email', form.email.data)
        user.update_history()
        self.session['username'] = user._id
        self.session['keep_logged_in'] = form.remember.data
        self.set_current_user(user)
        self.redirect('/admin')


@route('/logout')
class LogOutHandler(BaseRequest):
    def get(self):
        self.session['user_id'] = None
        self.session.destroy()
        self.redirect('/admin')
