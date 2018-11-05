#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import datetime

import pytest

from tests.models import engine, Base, session


@pytest.fixture
def setup_database(request):
    def teardown_database():
        print("teardown_function called")

    request.addfinalizer(teardown_database)


@pytest.fixture
def my_session():
    return session
