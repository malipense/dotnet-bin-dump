 #!/usr/bin/env python3

from logging import basicConfig, DEBUG, WARNING, getLogger
from argparse import ArgumentParser #library to easily parse command line arguments
from re import search, DOTALL
from definitions import DOS_HEADER_MAP, FILE_HEADER
from file_header import FileHeader
from util import bytes_to_int

logger = getLogger(__name__)

class Parser:
    class ParserException(Exception):
        pass

    PATTERN_HEADER_START = b'(\x72.{9}){9}'

    def __init__(self, file_path):
        self.file_path = file_path;
        self.data = self.get_file_data()

    def get_file_data(self):
        logger.debug(f'Reading contents of {self.file_path}')
        try:
            with open(self.file_path, 'rb') as fp:
                data = fp.read()
        except Exception as e:
            raise self.ParserException(f'Error reading file {self.file_path}') from e
        logger.debug(f'Success')
        return data

    def get_dos_header(self):
        logger.debug('Reading DOS_HEADER from PE ...')
        start_offset = 0x0
        dos_headers_map = DOS_HEADER_MAP.copy()
        try: 
            print('***********************DOS_HEADER***********************')
            for table in dos_headers_map:
                print(f'{table} --- HEX: {hex(bytes_to_int(self, self.data[start_offset: start_offset + dos_headers_map[table]['length']]))} --- DEC: {bytes_to_int(self, self.data[start_offset: start_offset + dos_headers_map[table]['length']])} --- {dos_headers_map[table]['desc']}' )
                start_offset += dos_headers_map[table]['length'] 
        except Exception as e:
            raise self.ParserException('as') from e 
        logger.debug('RETURN')

    def get_file_header(self):
        file_header_map = FILE_HEADER.copy()
        file_header = FileHeader(self.data, file_header_map)
        print('\n\n')
        print('***********************FILE_HEADER***********************')
        print(f'MACHINE: {file_header._machine}\nNUMBER OF SECTIONS: {file_header._number_of_sections}\nTIMESTAMP: {file_header._timestamp}\nCHARACTERISTICS: {file_header._characteristics}')

    def get_sections(self):
        return 'called get sections'

if __name__ == '__main__': #if is running as a script or if is imported as a module
    ap = ArgumentParser()
    ap.add_argument('file_paths', nargs = '+', help = 'Path location of the payload')
    ap.add_argument('-d', '--debug', action = 'store_true', help = 'Enable debugging logging')
    ap.add_argument('--headers', action = 'store_true', help = 'Dump bin headers')
    ap.add_argument('--sections', action = 'store_true', help = 'Dump bin sections')

    args = ap.parse_args()

    if args.debug:
        basicConfig(level = DEBUG)
    else:
        basicConfig(level = WARNING)

    for fp in args.file_paths:
        try:
            if args.headers:
                Parser(fp).get_dos_header()
                Parser(fp).get_file_header()
            if args.sections:
                print(Parser(fp).get_sections())
        except:
            logger.exception(f'Exception occurred for {fp}', exec_info = True)
            continue