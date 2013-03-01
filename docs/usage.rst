Usage
=====

Views included
--------------

There are four views provided by django-valet-keys:

``valet_keys.views.list``
    The "home page" for django-valet-keys, listing all of a user's keys
    and offering a link to create a new one. It's handy to offer a link to
    this view from a profile or settings page.

``valet_keys.views.new``
    Accepts a user-authored description and generates a new key.

``valet_keys.views.disable``
    Allows a user to disable a key, linked from the list view. Note that keys
    are never *deleted*, only disabled. This preserves recorded history and
    allows later investigation of robot misbehavior.

``valet_keys.views.history``
    Paginated view of usage history for a key, linked from the list view.

.. note::
    There's no *edit* view. Keys can be created or disabled, but are otherwise
    immutable. The only user-serviceable part is the description of the key;
    user name and password are randomly generated.

The ``@accepts_valet_key`` decorator
------------------------------------

In your views, the ``@accepts_valet_key`` decorator is the primary way to
support valet keys. For example:

.. code-block:: python

    from django.http import HttpResponse
    from valet_keys.decorators import accepts_valet_key

    @accepts_valet_key
    def hello(request):
        
        if request.valet_key:
            msg = 'HELLO ROBOT, I SEE YOU ARE IMPERSONATING %s' % request.user
        elif request.user.is_authenticated():
            msg = 'Why, hello there Mr. User!'
        else:
            msg = 'Welcome, guest.'

        response = HttpResponse(msg)
        response['Content-Type'] = 'text/plain'
        return response

The above demonstrates the features of the ``@accepts_valet_key`` decorator:

- ``request.valet_key`` is set to ``None``, if the request did not present a
  valid key in HTTP Basic Auth.

- ``request.valet_key`` contains an instance of ``valet_keys.models.Key`` if
  there *was* a valid key presented via HTTP Basic Auth.

- Additionally, ``request.user`` is set to the Django ``User`` who owns the
  valet key.

The ``Key`` model and activity logging
--------------------------------------

As mentioned above, views decorated with ``@accepts_valet_key`` will receive
an instance of ``valet_keys.models.Key`` in ``request.valet_key`` if a valid
key was presented via HTTP Basic Auth.

The presence of this instance (ie. not ``None``) is useful for detecting
access by an authorized robot. However, there is also a logging method
presented by the ``Key`` model object which is useful for recording what the
robot did while acting on a user's behalf. It works like so:

.. code-block:: python

    @accepts_valet_key
    def comment(request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)

        if 'POST' == request.method and request.valet_key:
            content = request.POST['comment']
            blog_post.add_comment(content)
            request.valet_key.log('blog.commented', blog_post, content)

As demonstrated in this pseudo-code, the ``Key`` model offers a ``log`` method
that accepts these parameters:

``action``
    Arbitrary string naming an action, handy when prefixed with an app name.
``content_object``
    An optional content object on which the action was performed.
``notes``
    Arbitrary text offering further description of the action.

Calls to ``log`` result in entries visible on the ``valet_keys.views.history``
view, thus offering rudimentary key usage tracking. 

.. NOTE::
    This is a pretty cruddy logging API, so `pull requests welcome!`_ 

.. _Pull requests welcome!: https://github.com/lmorchard/django-valet-keys/pulls

.. vim:set tw=78 ai fo+=n fo-=l ft=rst:
