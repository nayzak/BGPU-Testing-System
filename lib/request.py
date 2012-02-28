from whirlwind.core import request
from tornado.options import options
from mako.lookup import TemplateLookup


class MultiValueDict(dict):
    def getlist(self, key, default=None):
        try:
            return super(MultiValueDict, self).__getitem__(key)
        except KeyError:
            if default is None:
                return []
            return default


class BaseRequest(request.BaseRequest):
    def __init__(self, application, request):
        super(BaseRequest, self).__init__(application, request)
        self.request.arguments = MultiValueDict(request.arguments)

    def _get_template_lookup(self):
        from whirlwind.view.filters import Cycler
        Cycler.cycle_registry = {}

        filter_imports = [
            'from whirlwind.view.filters import Filters, Cycler',
        ]

        if options.mako_extra_imports:
            filter_imports.extend(options.mako_extra_imports)

        if isinstance(options.template_dir, (list, tuple)):
            directory_paths = options.template_dir
        else:
            directory_paths = [options.template_dir]

        return TemplateLookup(
            directories=directory_paths,
            module_directory=options.mako_modules_dir,
            output_encoding='utf-8',
            encoding_errors='replace',
            imports=filter_imports,
            default_filters=options.mako_default_filters
        )

    def render_template(self, **kwargs):
        super(BaseRequest, self).render_template(self.template, title=self.title, **kwargs)
