 #!/usr/bin/env python3

from logging import basicConfig, DEBUG, WARNING, getLogger
from argparse import ArgumentParser #library to easily parse command line arguments
from re import search, DOTALL

logger = getLogger(__name__)

class Parser:
    class ParserException(Exception):
        pass

    PATTERN_HEADER_START = b'(\x72.{9}){9}'
    PATTERN_SECTION_TABLE = b'(\x72.{9}){9}'
    PATTERN_SECTION_STRING = b'(\x72.{9}){9}'
    PATTERN_SECTION_SYMBOLS = b'(\x72.{9}){9}'

    def __init__(self, file_path):
        self.file_path = file_path;
        self.data = self.getFileData()

    def getFileData(self):
        logger.debug(f'Reading contents of {self.file_path}')
        try:
            with open(self.file_path, 'rb') as fp:
                data = fp.read()
        except Exception as e:
            raise self.ParserException(f'Error reading file {self.file_path}') from e
        logger.debug(f'Success')
        return data
    
    def getHeaders(self):
        return 'called get headers';

    def getSections(self):
        return 'called get sections';

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
                print(Parser(fp).getHeaders())
            if args.sections:
                print(Parser(fp).getSections())
        except:
            logger.exception(f'Exception occurred for {fp}', exec_info = True)
            continue