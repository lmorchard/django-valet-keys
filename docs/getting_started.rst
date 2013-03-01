Getting Started
===============

Installation
------------

These instructions will be temporarily cruddy. But, here's what I just did to
get started working with this app in another site I'm developing:

First, get the package itself installed. You may find it handy to try this::

    pip install -e 'git://github.com/lmorchard/django-valet-keys.git#egg=django-valet-keys`

This may or may not work, depending on whether I've yet done my job in
building a sensible `setup.py`. (`Pull requests welcome!`_)

Configuration
-------------

Add ``valet_keys`` to your ``INSTALLED_APPS`` list in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'django.contrib.auth',
        'valet_keys',
    )

Include ``valet_keys.urls`` in your site's ``urls.py``::

    urlpatterns = patterns('',
        ...
        (r'^keys/', include('valet_keys.urls')),
        (r'^admin/', include(admin.site.urls)),
    )

Finally, create all the models::

    $ ./manage.py syncdb
    $ ./manage.py migrate valet_keys

Of course, your mileage may vary, if you're not using `South`_ to manage your
model changes.

The app comes with `a basic set of Django templates`_ that you'll undoubtedly
want to copy up into your app's template path and customize.

You'll also probably want to link to ``valet_keys.views.list`` from somewhere
on your site (e.g. from a user profile or settings page). That's where valet
key management starts.

.. LINKS

.. _Pull requests welcome!: https://github.com/lmorchard/django-valet-keys/pulls
.. _South: http://south.aeracode.org/
.. _a basic set of Django templates: https://github.com/lmorchard/django-valet-keys/tree/master/valet_keys/templates/valet_keys

.. vim:set tw=78 ai fo+=n fo-=l ft=rst:
