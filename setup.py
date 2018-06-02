from setuptools import find_packages, setup

setup(
    name='lidarts',
    version='0.4.0-a3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'alembic',
        'bcrypt',
        'coverage',
        'eventlet',
        'Flask-Babel',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Migrate',
        'Flask-Security',
        'Flask-SocketIO',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'gunicorn',
        'hashids',
        'numpy',
        'psycopg2-binary',
        'pytest',
        'python-dotenv'
    ],
)
