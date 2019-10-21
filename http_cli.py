import argparse
from uri_objects import Uri
from pprint import pprint


def parse_input():
    """
    Uses argparse to gather args from the original command line input.
    """

    parser = argparse.ArgumentParser(description='Interface to access an API.')

    parser.add_argument('action',
                        help='Action type to access the API',
                        choices=['GET', 'PUT', 'POST']
                        )

    parser.add_argument('--item',
                        metavar="KEY=VALUE",
                        nargs='+',
                        help="Set a number of key-value pairs, which will comprise the values to put/post"
                        )

    parser.add_argument('--s', '--scheme',
                        help='Set the scheme (http or https)',
                        default="https"
                        )

    parser.add_argument('--h', '--host',
                        help="Set the host (main domain)",
                        required=True
                        )

    parser.add_argument('--port',
                        help='Set the port (for example 8080)'
                        )

    parser.add_argument('--p', '--path',
                        help='Set the path (for example /search)'
                        )

    parser.add_argument('--param',
                        metavar="KEY=VALUE",
                        nargs='+',
                        help='Set the parameters as key value pairs'
                        )

    parser.add_argument('--frags',
                        metavar="KEY=VALUE",
                        nargs='+',
                        help='set the fragments as key value pairs'
                        )

    parser.add_argument('--id',
                        metavar="KEY=VALUE",
                        nargs='+',
                        help='set the requested parameter for a GET request of a specific item'
                        )

    args = parser.parse_args()

    return args


def parse_key_values(itemstr):
    """
    Used in parse_vars to parse each input for a key value pair, by items separated by '='
    """
    items = itemstr.split('=')
    key = items[0].strip()

    if len(items) > 1:
        value = '='.join(items[1:])
        return key, value


def parse_vars(items):
    """
    Parse a series of key-value pairs and return a dictionary
    """
    dictionary = {}

    if items:
        for i in items:
            key, value = parse_key_values(i)
            dictionary[key] = value
    return dictionary


def contruct_uri(args):
    """
    Constructs the URI object from the parsed inputs.
    TODO: The get specific returns all, not a specific item, test post and put.
    """

    useruri = Uri.new() \
        .with_scheme(args.s) \
        .with_host(args.h) \
        .with_path(args.p) \
        .with_port(args.port)

    if args.param is not None:
        paramdic = parse_vars(args.param)

        for key, value in paramdic:
            useruri.with_param(key, value)

    if args.frags is not None:
        fragdic = parse_vars(args.frag)

        for key, value in fragdic:
            useruri.with_frags(key, value)

    useruri = useruri.to_uri()

    return useruri


def evaluate_action(useruri, args):
    """
    Exectues the desired action on the constructed URI Object.
    """

    if args.action == 'GET' and args.id is not None:
        getparam = parse_vars(args.id)
        return useruri.get_specific(getparam)

    elif args.action == 'GET' and args.id is None:
        return useruri.get()

    elif args.action == 'POST':
        postitem = parse_vars(args.item)
        return useruri.post(item_to_post=postitem)

    elif args.action == 'PUT':
        putitem = parse_vars(args.item)
        return useruri.put(item_to_post=putitem)


if __name__ == "__main__":

    targs = parse_input()
    tuseruri = contruct_uri(targs)
    do = evaluate_action(tuseruri, targs)
    pprint(do)