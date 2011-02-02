from django.db.models.signals import class_prepared


def add_table_prefix(sender, *args, **kwargs):
    from django.conf import settings
    prefix = getattr(settings, 'DB_TABLE_PREFIX', '')
    sender._meta.db_table = prefix + sender._meta.db_table

class_prepared.connect(add_table_prefix)
