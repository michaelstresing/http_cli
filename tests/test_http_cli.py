import unittest

from http_cli import Uri


class TestHttpCli(unittest.TestCase):

    def test_building_uri(self):

        test = Uri.new() \
            .with_scheme("https") \
            .with_host("facebook.com") \
            .with_path("a/b") \
            .with_param("user", "michael") \
            .with_param("age", "23")
        uri = test.to_uri()
        print(uri.to_string())
