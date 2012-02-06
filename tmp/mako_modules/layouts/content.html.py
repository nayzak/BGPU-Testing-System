# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.614655
_template_filename=u'/home/nayzak/Development/BGPU-Testing-System/application/views/layouts/content.html'
_template_uri=u'/layouts/content.html'
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
    return runtime._inherit_from(context, u'/layouts/htmlPage.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        def body_content():
            context.caller_stack._push_frame()
            try:
                next = context.get('next', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 12
                __M_writer(u'\n\t\t\t\t\t')
                # SOURCE LINE 13
                __M_writer(unicode(next.body()))
                __M_writer(u'\n\t\t\t\t')
                return ''
            finally:
                context.caller_stack._pop_frame()
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t')
        # SOURCE LINE 6
        runtime._include_file(context, u'/shared/flash_messages.html', _template_uri)
        __M_writer(u'\n\t<div id="wrap">\n\t\t<div id="main">\n\t\t\t')
        # SOURCE LINE 9
        runtime._include_file(context, u'/shared/header.html', _template_uri)
        __M_writer(u'\n\t\t\t<div id="content">\n\t\t\t\t<div id="content-inner">\n\t\t\t\t')
        # SOURCE LINE 14
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 15
        __M_writer(unicode(body_content()))
        __M_writer(u'\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\t')
        # SOURCE LINE 20
        runtime._include_file(context, u'/shared/footer.html', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


