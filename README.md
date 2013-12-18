API Usage
==========
This is the documentation for the v1.0 Forum API. The following Rest API provides an interface for clients to register and authenticate users, create topics, post comments, reply to comments and delete comments for public.redactor.co.za.

METHODS
=======

Below are the API methods. The browsable API that REST framework provides makes it possible for the API to be entirely self describing. The documentation for each API endpoint can be provided simply by visiting the URL in your browser. eg. http://public.redactor.co.za/topics/

Register
=========
/register - register new users with username and password fields.

User
=====
/user - Get all users registered on the site.
/user/{id} - Get users identified by a set of ids.

Topics
======
/topics - Get all topics on the site.
/topics/{id} - Get topics identified by a set of ids.

Comments
=========
/comments - Get all comments on the site.
/comments/{id} - Get comments identified by a set of ids.

Reply
/reply - Get all replies on the site.
/reply/{id} - Get reply identified by a set of ids.
