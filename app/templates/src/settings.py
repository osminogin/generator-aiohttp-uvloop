import os

SECRET_KEY = os.getenv('SECRET_KEY', '^^CHANGE^^ME^^')

<%_ if (use_postgres) { _%>
PGHOST = os.getenv('PGHOST', 'postgres')
PGUSER = os.getenv('PGUSER', 'postgres')
PGPASSWORD = os.getenv('PGPASSWORD', 'postgres')
PGDATABASE = os.getenv('PGDATABASE', 'postgres')
<% } %>

<%_ if (use_redis) { _%>
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost')
REDIS_DB = os.getenv('REDIS_DB', 0)     # By default
REDIS_POOLSIZE = os.getenv('REDIS_POOLSIZE', 10)
REDIS_TIMEOUT = os.getenv('RsEDIS_TIMEOUT', 60)
<%_ } _%>

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s:%(lineno)d - %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'asyncio': {
            'level': 'WARNING',
            'propagate': True,
        },
        'asyncio_redis': {
            'level': 'WARNING',
            'propagate': True,
        },
    }
}
