DOS_HEADER_MAP = {
    'E_MAGIC': {
        'offset': 0x2,
        'length': 0x2,
        'desc': 'Magic Number'
    },
    'E_CBLP': {
        'offset': 0x4,
        'length': 0x2,
        'desc': 'Bytes on last page of file'
    },
    'E_CP': {
        'offset': 0x6,
        'length': 0x2,
        'desc': 'Pages in file'
    },
    'E_CRLC': {
        'offset': 0x8,
        'length': 0x2,
        'desc': 'Relocations'
    },
    'E_CPARHDR': {
        'offset': 0xA,
        'length': 0x2,
        'desc': 'Size of header in paragraphs'
    },
    'E_MINALLOC': {
        'offset': 0xC,
        'length': 0x2,
        'desc': 'Minimum extra paragraphs needed'
    },
    'E_MAXALLOC': {
        'offset': 0xE,
        'length': 0x2,
        'desc': 'Maximum extra paragraphs needed'
    },
    'E_SS': {
        'offset': 0x10,
        'length': 0x2,
        'desc': 'Initial (relative) SS value'
    },
    'E_SP': {
        'offset': 0x12,
        'length': 0x2,
        'desc': 'Initial SP value'
    },
    'E_CSUM': {
        'offset': 0x14,
        'length': 0x2,
        'desc': 'Checksum'
    },
    'E_IP': {
        'offset': 0x16,
        'length': 0x2,
        'desc': 'Initial IP value'
    },
    'E_CS': {
        'offset': 0x18,
        'length': 0x2,
        'desc': 'Initial (relative) CS value'
    },
    'E_LFARLC': {
        'offset': 0x1A,
        'length': 0x2,
        'desc': 'File address of relocation table'
    },
    'E_OVNO': {
        'offset': 0x1C,
        'length': 0x2,
        'desc': 'Overlay Number'
    },
    'E_RES[0]': {
        'offset': 0x1E,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES[1]': {
        'offset': 0x20,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES[2]': {
        'offset': 0x22,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES[3]': {
        'offset': 0x24,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_OEMID': {
        'offset': 0x26,
        'length': 0x2,
        'desc': 'OEM identifier'
    },
    'E_OEMINFO': {
        'offset': 0x28,
        'length': 0x2,
        'desc': 'OEM information'
    },
    'E_RES2[0]': {
        'offset': 0x2A,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[1]': {
        'offset': 0x2C,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[3]': {
        'offset': 0x2E,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[4]': {
        'offset': 0x30,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[5]': {
        'offset': 0x32,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[6]': {
        'offset': 0x34,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[7]': {
        'offset': 0x36,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[8]': {
        'offset': 0x38,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_RES2[9]': {
        'offset': 0x3A,
        'length': 0x2,
        'desc': 'Reserved words'
    },
    'E_LFANEW': {
        'offset': 0x3C,
        'length': 0x4,
        'desc': 'File address of new exe header'
    }
}

FILE_HEADER = {
    'MACHINE': {
        'length':0x2,
        'desc': 'PE target architecture'
    },
    'NUMBER_OF_SECTIONS': {
        'length':0x2,
        'desc': 'Number of sections'
    },
    'TIME_DATE_STAMP': {
        'length':0x4
    },
    'POINTER_TO_SYMBOL_TABLE': {
        'length':0x4
    },
    'NUMBER_OF_SYMBOLS': {
        'length':0x4
    },
    'SIZE_OF_OPTIONAL_HEADER': {
        'length':0x2
    },
    'CHARACTERISTICS': { 
        'length':0x2
    }
}