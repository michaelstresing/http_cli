import unittest
from pprint import pprint
from http_cli.http_cli import *

class TestUriObjects(unittest.TestCase):

    def test_building_uri(self):

        test = Uri.new() \
            .with_scheme("https") \
            .with_host("facebook.com") \
            .with_path("a/b")

        uri = test.to_uri().to_string()

        self.assertEqual("https://facebook.com/a/b",
                         uri,
                         "Your uri ain't building")

    def test_building_uri_with_param_and_frag(self):

        test = Uri.new() \
            .with_scheme("https") \
            .with_host("facebook.com") \
            .with_path("a/b") \
            .with_param("user", "michael") \
            .with_param("age", "23") \
            .with_frags("f1", "yes") \
            .with_frags("f2", "yesyes")

        uri = test.to_uri().to_string()

        self.assertEqual("https://facebook.com/a/b?user=michael&age=23#f1=yes&f2=yesyes",
                         uri,
                         "Your uri ain't building")

    def test_building_uri_with_port(self):


        test = Uri.new() \
            .with_scheme("https") \
            .with_host("facebook.com") \
            .with_path("a/b") \
            .with_port("8080")

        uri = test.to_uri().to_string()

        self.assertEqual("https://facebook.com:8080/a/b",
                         uri,
                         "Your uri ain't building")

    def test_get(self):

        test = Uri.new() \
            .with_scheme("http") \
            .with_host("demo.codingnomads.co") \
            .with_port("8080") \
            .with_path("tasks_api/users") \

        testjson = test.to_uri().get()

        pprint(testjson)

        self.assertIsNot("blah", testjson, "Unlikely")


class TestHttpCli(unittest.TestCase):

    def test_can_parse_kv(self):
        test

