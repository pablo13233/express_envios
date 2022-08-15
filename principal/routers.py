class KCRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Sistema models go to kraken_cargo.
        """
        if model._meta.app_label == 'Sistema':
            return 'kraken_cargo'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write Sistema models go to kraken_cargo.
        """
        if model._meta.app_label == 'Sistema':
            return 'kraken_cargo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the Sistema app is involved.
        """
        if obj1._meta.app_label == 'Sistema' or \
           obj2._meta.app_label == 'Sistema':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the Sistema app only appears in the 'kraken_cargo'
        database.
        """
        if app_label == 'Sistema':
            return db == 'kraken_cargo'
        return None 