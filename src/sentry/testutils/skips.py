"""
sentry.testutils.skips
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

import socket
import pytest


def riak_is_available():
    try:
        socket.create_connection(('127.0.0.1', 8098), 1.0)
    except socket.error:
        return False
    else:
        return True


requires_riak = pytest.mark.skipif(
    not riak_is_available(),
    reason="requires riak server running")


def cassandra_is_available():
    try:
        socket.create_connection(('127.0.0.1', 9042), 1.0)
    except socket.error:
        return False
    else:
        return True


requires_cassandra = pytest.mark.skipif(
    not cassandra_is_available(),
    reason="requires cassandra server running")


def libsourcemap_is_available():
    try:
        import libsourcemap
        del libsourcemap
        return True
    except ImportError:
        return False

requires_no_libsourcemap = pytest.mark.skipif(
    libsourcemap_is_available(),
    reason=''
)
