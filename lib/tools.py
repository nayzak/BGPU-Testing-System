#coding: utf-8
'''
    Класс для примочек для упрощения работы с закроами к монги
    Весь говно код тут :)
'''
class Tools:

    @staticmethod
    def quary_from_params(params = None):
        try:
            for param, values in params.items():
                for value in values:
                    if (value == 'none'): del params[param]
                    elif (param == 'subject' or param == 'module'):
                        params.update({'position.' + param : value})
                        del params[param]
                    elif (param =='complexity'): params[param] = float(value)
                    else: params[param] = value
        except (e):
            print e
        return params


