import logging
import time
import base64

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from django.test.client import Client
from django.http import HttpRequest

from nose.tools import assert_equal, with_setup, assert_false, eq_, ok_
from nose.plugins.attrib import attr

from ..models import Key
from ..decorators import accepts_valet_key


class KeyDecoratorsTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @attr('current')
    def test_key_auth_decorator(self):

        user = User(username="test23", email="test23@example.com")
        user.save()

        @accepts_valet_key
        def fake_view(request, foo, bar):
            return (foo, bar)

        for is_disabled in (False, True):

            key = Key(user=user)
            secret = key.generate_secret()
            key.save()

            if is_disabled:
                key.disable()

            cases = (
                (key.key, secret, True),
                (key.key, 'FAKE', False),
                ('FAKE',  secret, False),
                ('FAKE',  'FAKE', False),
            )

            for k, s, success in cases:

                request = HttpRequest()
                request.user = AnonymousUser()

                auth = '%s:%s' % (k, s)
                b64_auth = base64.encodestring(auth)
                request.META['HTTP_AUTHORIZATION'] = 'Basic %s' % b64_auth

                foo, bar = fake_view(request, 'foo', 'bar')
                eq_('foo', foo)
                eq_('bar', bar)

                if not success or is_disabled:
                    ok_(not request.user.is_authenticated())
                else:
                    ok_(request.user.is_authenticated())
                    ok_(request.user == user)
                    ok_(request.valet_key)
                    ok_(request.valet_key == key)

            key.delete()
