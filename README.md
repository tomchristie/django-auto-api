# Django Auto API

**Web APIs for Django, with one line of code.**

**Author:** Tom Christie, [Follow me on Twitter][1].

## Overview

Django Auto API is an incredibly simple app that gives you a fully hyperlinked read-only API for all installed models in `html`, `json`, `yaml`, `xml` and `csv`. 
It only requires one line of code to be added to your project.

It is intended to demonstrate how `django-serializers` can easily be used to build web APIs.  In particular, it shows that customizing how model relations are represented allows you to do powerful things such as using hyperlinking to represent relationships, rather than using the default primary key representation.

## Requirements

Requires `django-serializers`, which currently requires Django 1.4.

## Installation

Install using pip:

    pip install django-auto-api

Add the `django-auto-api` urls to your URLConf:

    urlpatterns = patterns('',
        ...
        url(r'^api/', include('autoapi.urls', namespace='autoapi')),
    )

## End result

In `HTML` format:

![HTML API](https://github.com/tomchristie/django-auto-api/raw/master/screenshots/html.png)

In `JSON` format:

![JSON API](https://github.com/tomchristie/django-auto-api/raw/master/screenshots/json.png)

In `XML` format:

![XML API](https://github.com/tomchristie/django-auto-api/raw/master/screenshots/xml.png)

## Running the example project

If you've cloned the project from the git repo, you can run a very simple example project:

    ./manage.py syncdb
    ./manage.py loaddata testfixture.json
    ./manage.py runserver

This runs an example API for a few models of `contrib.contenttypes` and `contrib.auth`. 

Changelog
=========

0.1.0
-----

* Initial release

License
=======

Copyright © Tom Christie.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://twitter.com/_tomchristie
