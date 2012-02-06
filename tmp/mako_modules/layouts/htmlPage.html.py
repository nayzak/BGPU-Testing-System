# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.623046
_template_filename=u'/home/nayzak/Development/BGPU-Testing-System/application/views/layouts/htmlPage.html'
_template_uri=u'/layouts/htmlPage.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = ['scripts', 'page_title', 'head_tags']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'<!DOCTYPE html>\n<html id="home" lang="en">\n\t<head>\n\t\t\n\t\t<meta charset=utf-8 />\n\t\t<meta name="keywords" content="" />\n\t\t<meta name="description" content="" />\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0" />\n\t\t\n\t\t<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>\n        <script type="text/javascript" src="/static/js/application.js"></script>\n\t\t<script type="text/javascript" src="/static/js/whirlwind.js"></script>\n\t\t<script type="text/javascript" src="/static/js/flash-messages.js"></script>\t\t\n\t\t<!--[if lt IE 9]>\n\t\t\t<script src="http://html5shim.googlecode.com/svn/trunk/html5-els.js"></script>\n\t\t<![endif]-->\n\t\t\n\t\t<link rel="stylesheet" type="text/css" href="/static/css/common.css" />\n\t\t<link rel="stylesheet" type="text/css" href="/static/css/layout.css" />\n\t\t<link rel="stylesheet" type="text/css" href="/static/css/flash-messages.css" />\n\t\t<!--[if !IE 7]>\n\t\t\t<style type="text/css">\n\t\t\t\t#wrap {display:table;height:100%}\n\t\t\t</style>\n\t\t<![endif]-->\n\t\t\n\t\t')
        # SOURCE LINE 30
        __M_writer(u'\n\t\t<title>\n\t\t\t')
        # SOURCE LINE 32
        __M_writer(unicode(self.page_title()))
        __M_writer(u'\n\t\t</title>\n\t\t\t\t\n\t\t')
        # SOURCE LINE 35
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 36
        __M_writer(u'\n\t</head>\n\t<body>\n\t\t')
        # SOURCE LINE 39
        __M_writer(unicode(next.body()))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 40
        __M_writer(unicode(self.scripts()))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 41
        __M_writer(u'\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'welcome to whirlwind')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


