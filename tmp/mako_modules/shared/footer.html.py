# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.636268
_template_filename=u'/home/nayzak/Development/BGPU-Testing-System/application/views/shared/footer.html'
_template_uri=u'/shared/footer.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<div id="footer">\n\t<div id="footer-inner">\n\t\t<div id="copyright">\n\t\t\t&copy; <script>document.write(Date.today().toString("yyyy"));</script>. All rights reserved.\n\t\t</div>\n\t</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


