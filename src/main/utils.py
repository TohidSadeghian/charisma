import json
from django.core.exceptions import ImproperlyConfigured 


with open('./secrets.json') as f:
    secrets = json.load(f)

def get_secret(SECRET_KEY):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[SECRET_KEY]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(SECRET_KEY)
    raise ImproperlyConfigured(error_msg)