#! /usr/bin/env python

import unittest
from http_server import build_response


class testHTTPserver(unittest.TestCase):

    # def test(self):
    #     self.failUnless(True)

    # def test_rcv_request():
    #     pass

    # def test_dir_response(self):

    #     response = build_response('/images/')
    #     print response

    # def test_file_response(self):

    #     response = build_response('sample.txt')
    #     print response

    # def test_file_not_found_response(self):

    #     response = build_response('notafile.txt')
    #     print response
    # def test_build_response(self):

    #     response = build_response('/index.html')
    #     print response

if __name__ == '__main__':
    unittest.main()