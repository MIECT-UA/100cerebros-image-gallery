# encoding=utf-8

# Performs several unitary tests on modules imageEditor, imageMenu, effects,
# filters, memes, etc...
# Usage: python -m pytest -v tests.py.

import pytest


def test_effects_Thumbnails():
    














#IGNORE THESE
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Tests of connection.py
def test_CONNECT():
    import time
    import json
    from connection import CONNECT, CONNECT_LIST
    print 'testing CONNECT with correct message'
    message = json.dumps({
            "type": "PUT",
            "name": "test_CONNECT",
            "timestamp": int(time.time()),
            "content": "test test_CONNECT",
        })+"\r\n"
    assert CONNECT(message) != None


def test_CONNECT_LIST():
    import json
    from connection import CONNECT, CONNECT_LIST
    print 'testing CONNECT_LIST with correct message'
    message = json.dumps({
            "type": "LIST",
         }) + "\r\n"
    assert CONNECT_LIST(message) != None


# -----------------------------------------------------------------------------
# Tests of list.py
def test_LIST():
    from list import LIST
    print 'testing if LIST runs as expected'
    assert LIST() == 'OK'


# -----------------------------------------------------------------------------
# Tests of create.py
def test_CREATEexistingBox():
    import os
    import sys
    from create import CREATE
    print 'testing the creation of two boxes with same name'
    count = 0
    if (os.path.exists("testCount.txt")):
        file = open('testCount.txt', 'r')
        # count allows multiple tests without changing box names manually
        count = int(file.read())
        file.close()
    assert CREATE('testCREATE2boxes_' + str(count), 0) == 'OK'
    assert CREATE('testCREATE2boxes_' + str(count), 0) == ('ERROR', 'Box already exists')
    count = count + 1
    file = open('testCount.txt', 'w')
    file.write(str(count))
    file.close()


def test_CREATEsecureBox():
    import os
    import sys
    from create import CREATE
    print 'testing successful creation of a secure box'
    count = 0
    if (os.path.exists("testCount.txt")):
        file = open('testCount.txt', 'r')
        # count allows multiple tests without changing box names manually
        count = int(file.read())
        file.close()
    assert CREATE('testCREATEsecureBox_' + str(count), 1) == 'OK'
    count = count + 1
    file = open('testCount.txt', 'w')
    file.write(str(count))
    file.close()


def test_CREATEwrongSecure():
    import time
    from create import CREATE
    print 'testing the creation of a secure box with wrong argument'
    assert CREATE('testCREATEsecureBox' + str(int(time.time())), 2) == ('ERROR', 'Invalid user input')


# -----------------------------------------------------------------------------
# Tests of put.py
def test_PUTnoSuchBox():
    from put import PUT
    print 'testing PUT to unexisting box'
    assert PUT('testPUTnoSuchBox', 'message testPUTnoSuchBox') == ('ERROR', 'Box not found')


def test_PUTexistingBox():
    from create import CREATE
    from put import PUT
    print 'testing PUT to exising box'
    CREATE('test_PUTexistingBox', 0)
    assert PUT('test_PUTexistingBox', 'message test_PUTexistingBox') == 'OK'


def test_PUTexistingBoxSec():
    from create import CREATE
    from put import PUT
    print 'testing PUT to existing secure box'
    CREATE('test_PUTexistingBoxSec', 1)
    assert PUT('test_PUTexistingBoxSec', 'message est_PUTexistingBoxSec') == 'OK'


# -----------------------------------------------------------------------------
# Tests of get.py
def test_GETnoSuchBox():
    from get import GET
    print 'testing GET from unexisting box'
    assert GET('testGETnoSuchBox', 0) == ('ERROR', 'Box not found')


def test_GETemptyBox():
    from create import CREATE
    from get import GET
    print 'testing GET from empty box'
    CREATE('test_GETemptybox', 0)
    assert GET('test_GETemptybox', 0) == ('ERROR', 'Box is empty')


def test_GEToneTextBox():
    from create import CREATE
    from put import PUT
    from get import GET
    print 'testing GET from box with messages'
    CREATE('test_GEToneTextBox', 0)
    PUT('test_GEToneTextBox', 'message test_GEToneTextBox')
    assert GET('test_GEToneTextBox', 0) == 'OK'
    assert GET('test_GEToneTextBox', 0) == ('ERROR', 'Box is empty')


def test_GETwrongSecure():
    from create import CREATE
    from get import GET
    print 'testing GET from a secure box with wrong argument'
    CREATE('test_GETwrongSecureBox', 1)
    assert GET('testGETwrongSecureBox', 2) == ('ERROR', 'Invalid user input')


def test_GETsecureEmptyBox():
    from create import CREATE
    from get import GET
    print 'testing GET from a secure empty box with wrong argument'
    CREATE('test_GETsecureEmptyBox', 1)
    assert GET('test_GETsecureEmptyBox', 1) == ('ERROR', 'Box is empty')


def test_GEToneTextSecureBox():
    from create import CREATE
    from put import PUT
    from get import GET
    print 'testing GET from secure box with messages'
    CREATE('test_GEToneTextSecureBox', 0)
    PUT('test_GEToneTextSecureBox', 'message test_GEToneTextSecureBox')
    assert GET('test_GEToneTextSecureBox', 0) == 'OK'
    assert GET('test_GEToneTextSecureBox', 0) == ('ERROR', 'Box is empty')
