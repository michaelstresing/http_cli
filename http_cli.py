from typing import Dict
import requests
import argparse

parser = argparse.ArgumentParser(description='Interface to access an API.')

parser.add_argument('--getall', dest='', action='',
                    const=sum, default=max,
                    help='GET all data from API')

parser.add_argument('--post', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='POST to API')

parser.add_argument('--put', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='PUT to API')

args = parser.parse_args()
print(args.accumulate(args.integers))


class Uri:
    """
    Uri class
    """

    __create_key = object()

    @classmethod
    def new(cls):
        """
        Creates a new Uri object, using the BuildUri class (__create_key) used to prevent creation via init.
        """
        return BuildUri(Uri.__create_key)

    def __init__(self, create_key, scheme: str, host: str, port: str, path: str, param: dict, frags: dict):

        assert (create_key == Uri.__create_key), \
            "URI objects must be created using BuildURI, please use the .new() method"

        self._scheme = scheme
        self._host = host
        self._port = port
        self._path = path
        self._param = param
        self._frags = frags

    def format_params(self):
        """
        Formats the dictionary created in BuildUri into a string for the Uri object.
        """

        paramstr = ''
        paramstr = '&'.join([f"{key}={value}" for key, value in self._param.items()])
        if len(paramstr) > 0:
            paramstr = '?' + paramstr

        return paramstr

    def format_frags(self):
        """
        Formats the dictionary created in BuildUri into a string for the Uri object.
        """

        fragstr = ''
        fragstr = '&'.join([f"{key}={value}" for key, value in self._frags.items()])
        if len(fragstr) > 0:
            fragstr = '#' + fragstr

        return fragstr

    def to_string(self):
        """
        Converts the Uri object into a URL string
        """

        paramstring = self.format_params()
        fragmentstring = self.format_frags()

        return f'{self._scheme}://{self._host}:{self._port or ""}/{self._path or ""}{paramstring}{fragmentstring}'

    def get(self):

        source = self.to_string()
        return requests.get(source).json()


class BuildUri:

    def __init__(
            self,
            create_key,
            scheme: str = None,
            host: str = None,
            port: str= None,
            path: str = None,
            param: dict = {},
            frags: dict = {}
    ):

        self._create_key = create_key
        self.scheme = scheme
        self.host = host
        self.port = port
        self.path = path
        self.param = param
        self.frags = frags

    def with_scheme(self, scheme):
        """
        Insert a scheme
        """
        return BuildUri(
            create_key=self._create_key,
            scheme=scheme,
            host=self.host,
            port=self.port,
            path=self.path,
            param=self.param,
            frags=self.frags
        )

    def with_host(self, host):
        """
        Insert a host
        """
        return BuildUri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=host,
            port=self.port,
            path=self.path,
            param=self.param,
            frags=self.frags
        )

    def with_port(self, port):
        """
        Insert a port
        """
        return BuildUri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=self.host,
            port=port,
            path=self.path,
            param=self.param,
            frags=self.frags
        )

    def with_path(self, path):
        """
        Insert a path
        """
        return BuildUri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=self.host,
            port=self.port,
            path=path,
            param=self.param,
            frags=self.frags
        )

    def with_param(self, key, value):
        """
        Insert a parameter
        """

        new_params = self.param.copy()
        new_params[key] = value

        return BuildUri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=self.host,
            port=self.port,
            path=self.path,
            param=new_params,
            frags=self.frags
        )

    def with_frags(self, key, value):
        """
        Insert a fragment
        """

        new_frags = self.frags.copy()
        new_frags[key] = value

        return BuildUri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=self.host,
            port=self.port,
            path=self.path,
            param=self.param,
            frags=new_frags
        )

    def to_uri(self):
        """
        Create a Uri object from the builder
        """
        return Uri(
            create_key=self._create_key,
            scheme=self.scheme,
            host=self.host,
            port=self.port,
            path=self.path,
            param=self.param,
            frags=self.frags
        )
