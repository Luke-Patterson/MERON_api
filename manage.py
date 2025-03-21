#!/usr/bin/env python
import os
import sys
import environ

if __name__ == '__main__':
    # Load .env file
    env = environ.Env()
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.isfile(env_file):
        env.read_env(env_file)
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meron_api.settings.development')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)
