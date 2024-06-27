JAZZMIN_SETTINGS = {
    # Исправим смотря на тз
    "site_title": "admin",  # Заголовок сайта
    "site_header": "admin",  # Заголовок на экране входа
    "site_brand": "admin",  # Выходит на сайте вместо Django-admin.(Администрирование сайта)
    "welcome_sign": "admin",  # Приветственный текст на экране входа
    "copyright": "admin",  # Авторское право (footer)
    "search_model": ["auth.User", "auth.Group"],

    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # telega
        {"name": "Support", "url": "https://t.me/cunchik", "new_window": True},

        {"name": "Support(Технический)", "url": "https://t.me/Savadatsu", "new_window": True},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],
    "show_sidebar": True,

    "changeform_format": "horizontal_tabs",

}

# Выбрал только то что мне понравилось если что можем поменять тему
JAZZMIN_UI_TWEAKS = {
    # белый фон:
    # "theme": "flatly",
    # "theme" : "simplex",  # белый фон с цветами - RGB
    # "theme": "sketchy",     #  мультяшный

    # темный фон:
    "theme": "darkly",
    # "theme": "slate",    # темный (серьезный , полностью)

}
