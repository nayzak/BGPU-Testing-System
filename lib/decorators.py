#coding: utf-8
import urllib
from tornado.web import HTTPError


def role_required(role):
    def wrap(view_func):
        def has_role(self, *args, **kwargs):
            if not self.current_user:
                if self.request.method == "GET":
                    url = self.get_login_url()
                    if "?" not in url:
                        url += "?" + urllib.urlencode(dict(next=self.request.uri))
                    self.redirect(url)
                    return
                raise HTTPError(403)
            else:
                if not self.current_user.has_role(role):
                    self.flash.error = "У Вас недостаточно прав для совершения запрошенного действия."
                    self.redirect(self.request.headers.get('Referer', '/admin'))
                    return

                return view_func(self, *args, **kwargs)

        return has_role
    return wrap
