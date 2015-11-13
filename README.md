Django Rest Framework Mongoengine
==============================================================


This is a hack for django-rest-framework-mongoengine

the base version forked from [tweiand-10m2](https://github.com/tweiand-10m2/django-rest-framework-mongoengine).

he fix some bug but not merge into official code.

## Installation
`pip install django-rest-framework-mongoengine-hack`


Don't forget to add the package to installed apps.
```Python
INSTALLED_APPS = (
    ...
    'rest_framework_mongoengine',
)
```


## Change Note

version 1.0

* change OrderedDict import path to support newer drf
* make EmbeddedDocumentSerializer work
* support for mongoengine 0.9+
* fix error when exclude is not in DocumentSerializer
* add LongField support



