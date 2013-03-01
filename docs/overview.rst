Overview
========

What is django-valet-keys?
--------------------------

There are many ways to allow a robot to authenticate to a web service and
perform actions on your behalf. For example:

- HTTP Basic authentication using your user name and password
- OAuth to grant permission from within a browser interaction

Well, HTTP auth using your real credentials is stupid. Don't do that. 

OAuth is nice, because you generate a new set of credentials during the course
of granting permission, and you can revoke permission by destroying the
credentials. But, OAuth can be difficult to implement. It's also overkill if
all you want to do is to build a small robot or cronjob, rather than connect
two web services together.

So, enter django-valet-keys. This is a way to manage credentials for robots
that...

- consist of a randomized user name and password;
- can be used with HTTP Basic Auth, presumably over SSL;
- can be disabled by the human in charge at any time;
- can record and track usage.

If you *do* want to connect two web services together, this app is probably not
for you. But, if you'd like something simpler for robots, this might be your
thing.
