# relationship_app/__init__.py
default_app_config = 'relationship_app.apps.RelationshipAppConfig'

# OR simply import signals (if you use default AppConfig)
from . import signals  # ensures signals get registered
