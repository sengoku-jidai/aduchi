import argparse
import pathlib
import yaml

from azuchi import azuchi_log

def load_connections(file_path):
    with open(file_path) as file_stream:
       return yaml.load(file_stream, Loader=yaml.SafeLoader)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--connection-file', default=str(pathlib.Path(pathlib.Path.home(), '.azuchi', 'connections.yml')))
    parser.add_argument('connection')
    args = parser.parse_args()

    connections = load_connections(args.connection_file)
    connection = connections[args.connection]
    azuchi_log(str(connection))
