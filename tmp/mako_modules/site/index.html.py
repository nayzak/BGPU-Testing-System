# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.568915
_template_filename='/home/nayzak/Development/BGPU-Testing-System/application/views/site/index.html'
_template_uri='/site/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/content.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<div id="page-header">\n\t<div class="title">\n\t\tWelcome to Whirlwind\n\t</div>\n\t<div class="subtitle">\n\t\tYou\'ve successfully setup a new whirlwind app!\n\t</div>\n</div>\n<div id="page-content">\n\t<div class="body">\n\t\t<a href="http://github.com/trendrr/whirlwind" target="new">Check out our docs on github.com to get started</a>\n\t</div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


