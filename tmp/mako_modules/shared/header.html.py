# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.634379
_template_filename=u'/home/nayzak/Development/BGPU-Testing-System/application/views/shared/header.html'
_template_uri=u'/shared/header.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_logged_in = context.get('is_logged_in', UNDEFINED)
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<div id="header">\n\t<div id="header-inner">\n\t\t<div id="logo">\n\t\t\t<h1>\n\t\t\t\t<a href="/">Whirlwind</a>\n\t\t\t</h1>\n\t\t</div>\n\t\t<div id="user-menu">\n')
        # SOURCE LINE 10
        if is_logged_in :
            # SOURCE LINE 11
            __M_writer(u'\t\t\t\t')
            __M_writer(unicode(current_user['_id']))
            __M_writer(u' : \n\t\t\t\t<a href="/logout">log-out</a>\n')
            # SOURCE LINE 13
        else :
            # SOURCE LINE 14
            __M_writer(u'\t\t\t\t<a href="/login">log-in</a> : \n\t\t\t\t<a href="/signup">sign-up</a>\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\t\t</div>\n\t\t<div class="clear"></div>\n\t</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


