#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from publisher.publisher import *

class TestPublisherMethods(unittest.TestCase):

    def setUp(self):

        self.linkString = '<a href="../genindex.html" title="General Index" accesskey="I">index</a></li> \
<li class="right"> \
<a href="../py-modindex.html" title="Python Module Index">modules</a> |</li> \
<li class="right"> \
<a href="unittest.mock.html" title="26.5. unittest.mock — mock object library" accesskey="N">next</a> |</li> \
<li class="right"> \
<a href="doctest.html" title="26.3. doctest — Test interactive Python examples" accesskey="P">previous</a> |</li> \
<li><img src="../_static/py.png" alt="" style="vertical-align: middle; margin-top: -1px"></li> \
<li><a href="https://www.python.org/">Python</a> »</li> <li class="nav-item nav-item-1"><a href="index.html">The Python Standard Library</a> »</li> \
<li class="nav-item nav-item-2"><a href="development.html" accesskey="U">26. Development Tools</a> »</li> \
href="https://github.com/python/cpython/tree/3.6/Lib/unittest/__init__.py">Lib/unittest/__init__.py</a></p> \
<hr class="docutils"> \
<p>(If you are already familiar with the basic concepts of testing, you might want \
<p>The <a class="reference internal" href="#module-unittest" title="unittest: Unit testing framework for Python."> '

        self.retUrls = ['../genindex.html',
                        '../py-modindex.html',
                        'unittest.mock.html',
                        'doctest.html',
                        'https://www.python.org/',
                        'index.html',
                        'development.html',
                        'https://github.com/python/cpython/tree/3.6/Lib/unittest/__init__.py',
                        '#module-unittest']

    def test_urlparser(self):
        urls = findAllHref(self.linkString)
        for i, url in enumerate(urls):
            self.assertEqual(self.retUrls[i], url)

if __name__ == '__main__':
    unittest.main()
