import datetime

from tests.models import Entry, Blog


def test_basic_filtering(my_session, b1, b2):
    bq = my_session.query(Blog)
    eq = my_session.query(Entry)
    assert bq.filter_by(name__exact="blog1").one() is b1
    assert bq.filter_by(name__contains="blog").all() == [b1, b2]
    assert bq.filter_by(entries__headline__exact="b2 headline 2").one() is b2
    assert (
            bq.filter_by(
                entries__pub_date__range=(
                    datetime.date(2010, 1, 1),
                    datetime.date(2010, 3, 1),
                )
            ).one()
            is b1
    )
    assert eq.filter_by(pub_date__year=2011).one() is b2.entries[2]
    assert eq.filter_by(pub_date__year=2011, id=b2.entries[2].id).one() is b2.entries[2]


def test_basic_excluding(my_session, b2):
    eq = my_session.query(Entry)
    assert eq.exclude_by(pub_date__year=2010).one() is b2.entries[2]


def test_basic_ordering(my_session, b1, b2):
    eq = my_session.query(Entry)
    assert eq.order_by("-blog__name", "id").all() == b2.entries + b1.entries
