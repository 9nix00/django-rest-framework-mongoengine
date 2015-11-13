from distutils.core import setup

setup(
    name='django-rest-framework-mongoengine-hack',
    version='1.0.0',
    description='Hack for django-rest-framework-mongoengine to support newer mongoengine and drf',
    packages=['rest_framework_mongoengine', ],
    license='see https://github.com/9nix00/django-rest-framework-mongoengine/blob/master/LICENSE',
    long_description='see https://github.com/9nix00/django-rest-framework-mongoengine/blob/master/README.md',
    url='https://github.com/9nix00/django-rest-framework-mongoengine',
    download_url='https://github.com/9nix00/django-rest-framework-mongoengine/releases/',
    keywords=['mongoengine', 'serializer', 'django rest framework'],
    author='WANG WENPEI',
    author_email='wangwenpei@nextoa.com',
    requires=[
        'mongoengine',
        'djangorestframework'
    ],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Internet',
                 'Topic :: Internet :: WWW/HTTP :: Site Management',
                 'Topic :: Text Processing :: Markup :: HTML',
                 'Intended Audience :: Developers'
                 ],
)
