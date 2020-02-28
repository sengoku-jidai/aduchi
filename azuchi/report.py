import pathlib
import yaml

from azuchi import azuchi_log

def load_connections():
    file_path = pathlib.Path(pathlib.Path.home(), '.azuchi', 'connections.yml')
    with file_path.open() as file_stream:
       return yaml.load(file_stream, Loader=yaml.SafeLoader)


if __name__ == '__main__':
    connections = load_connections()
    azuchi_log('hello,report!')