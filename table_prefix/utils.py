from django.conf import settings


OMIT_MODELS = getattr(settings, 'OMIT_MODELS', [])
DB_PREFIX = getattr(settings, 'DB_PREFIX', '')


def get_table_name(table_name):
    """ guess new model's DB table name
    """
    if DB_PREFIX and DB_PREFIX not in table_name:
        return "_".join((DB_PREFIX, table_name))
    else:
        return table_name


def models_is_prefixed(model):
    """ check if we should prefix this model's DB table
    """
    model_path = ".".join((model._meta.app_label, model._meta.object_name))

    if model._meta.proxy:
        return models_is_prefixed(model.__bases__[0])

    return (model_path not in OMIT_MODELS) and model._meta.managed is True
