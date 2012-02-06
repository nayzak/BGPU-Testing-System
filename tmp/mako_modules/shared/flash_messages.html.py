# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1328498051.630836
_template_filename=u'/home/nayzak/Development/BGPU-Testing-System/application/views/shared/flash_messages.html'
_template_uri=u'/shared/flash_messages.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from whirlwind.view.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        flash = context.get('flash', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        if flash:
            # SOURCE LINE 4
            __M_writer(u'<div id="flash-message" class="flash-message">\n\t<div id="flash-message-list"></div>\n</div>\n<script>\n\tvar message = "<ul id=\'flash-message-items\'>";\n')
            # SOURCE LINE 9
            if 'error' in flash:
                # SOURCE LINE 10
                for message in flash['error']:
                    # SOURCE LINE 11
                    __M_writer(u'\t\t\tmessage += "<li class=\'error\'>')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</li>";\n')
                    pass
                pass
            # SOURCE LINE 14
            if 'notice' in flash:
                # SOURCE LINE 15
                for message in flash['notice']:
                    # SOURCE LINE 16
                    __M_writer(u'\t\t\tmessage += "<li class=\'notice\'>')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</li>";\n')
                    pass
                pass
            # SOURCE LINE 19
            if 'info' in flash:
                # SOURCE LINE 20
                for message in flash['info']:
                    # SOURCE LINE 21
                    __M_writer(u'\t\t\tmessage += "<li class=\'info\'>')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</li>";\n')
                    pass
                pass
            # SOURCE LINE 24
            if 'success' in flash:
                # SOURCE LINE 25
                for message in flash['success']:
                    # SOURCE LINE 26
                    __M_writer(u'\t\t\tmessage += "<li class=\'success\'>')
                    __M_writer(filters.html_escape(unicode(message )))
                    __M_writer(u'</li>";\n')
                    pass
                pass
            # SOURCE LINE 29
            __M_writer(u'\tmessage += "</ul>";\n\tshowNotification(message, \'\', function(){});\n</script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


