#grab the current path so we can set some thing automatically
import sys
app_path = sys.path[1]

#run mode
mode = "development"

#define a port for testing
port = 8000

#set static resources path
static_path = "%s/static" % app_path

#define a dir for mako to look for templates - relative to the app directory
template_dir = "%s/application/views" % app_path

#define a dir for mako to cache compiled templates
mako_modules_dir = "%s/tmp/mako_modules" % app_path

#define a log file... optionally just use the string 'db' to log it to mongo
log = "%s/tmp/log/application.log" % app_path

#define a database host
db_host = 'localhost'

#define the database port
db_port = 27017

#define the database name
db_name = 'testing_system'

#uncomment the following if when using redis session middleware

#redis host
#redis_host = 'localhost'

#redis port
#redis_port = 6379

#redis db name
#redis_db = 'whirlwind'

#uncomment the following when using memcache session middleware

#memcache host
#memcache_host = 'localhost'

#you must define a cookie secret. you can use whirlwind-admin.py --generate-cookie-secret
cookie_secret = "sVkiz6R+R9aLJaaStyS642Cqqegef0NPv+liICE0uIk="

middleware_classes = [
    "whirlwind.middleware.flash.middleware.FlashMiddleware",
    "whirlwind.middleware.session.middleware.SessionMiddleware",
    #"whirlwind.middleware.session.redis.middleware.SessionMiddleware"
    #"whirlwind.middleware.session.memcache.middleware.SessionMiddleware"
]

mako_extra_imports = [
    "from application.views.helpers.forms import render_form"
]

smtp_host = "smtp.mail.ru"
smtp_port = 25
smtp_user = "krest_yan"
smtp_password = "qwerty6"
email_notification_address = "krest_yan@mail.ru"
email_notification_name = "Testing System Admin"
