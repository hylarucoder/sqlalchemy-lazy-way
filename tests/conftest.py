#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import datetime

import pytest

from tests.models import session, Blog, Entry


@pytest.fixture
def setup_database(request):
    def teardown_database():
        print("teardown_function called")

    request.addfinalizer(teardown_database)


@pytest.fixture(scope='session')
def my_session():
    return session


@pytest.fixture(scope='session')
def b2(my_session):
    b = Blog(
        name="blog2",
        entries=[
            Entry(
                headline="b2 headline 1",
                body="body 1",
                pub_date=datetime.date(2010, 5, 12),
            ),
            Entry(
                headline="b2 headline 2",
                body="body 2",
                pub_date=datetime.date(2010, 7, 18),
            ),
            Entry(
                headline="b2 headline 3",
                body="body 3",
                pub_date=datetime.date(2011, 8, 27),
            ),
        ],
    )
    my_session.add(b)
    my_session.commit()
    return b


@pytest.fixture(scope='session')
def b1(my_session):
    b = Blog(
        name="blog1",
        entries=[
            Entry(
                headline="b1 headline 1",
                body="body 1",
                pub_date=datetime.date(2010, 2, 5),
            ),
            Entry(
                headline="b1 headline 2",
                body="body 2",
                pub_date=datetime.date(2010, 4, 8),
            ),
            Entry(
                headline="b1 headline 3",
                body="body 3",
                pub_date=datetime.date(2010, 9, 14),
            ),
        ],
    )
    my_session.add(b)
    my_session.commit()
    return b
