from util import bytes_to_int
from datetime import datetime
from enum import Enum

class FileHeader:
    PATTERN_IMG_HEADER_START = b'(\x50\x45\x00\x00.{16}){16}'
    header_start_offset = 0x000000 #find start of header in the file

    class CHARAC_ENUM(Enum):
        RELOCS_STRIPED = 0x0001
        EXECUTABLE_IMAGE = 0x0002
        LINE_NUMS_STRIPPED = 0x0004
        LOCAL_SYMS_STRIPPED = 0x0008
        AGRESSIVE_WS_TRIM = 0x0010
        LARGE_ADDRESS_AWARE = 0x00020
        BYTES_REVERSED_LO = 0x0080
        MACHINE_32BIT = 0x0100
        DEBUG_STRIPPED = 0x0200
        REMOVABLE_RUN_FROM_SWAP = 0x0400
        NET_RUN_FROM_SWAP = 0x0800
        FILE_SYSTEM = 0x1000
        FILE_DLL = 0x2000
        UP_SYSTEM_ONLY = 0x4000
        BYTES_REVERSED_HI = 0x8000

    def __init__(self, bin, definition):
        self.bin = bin
        self.definition = definition
        self._machine = self.get_machine_target()
        self._number_of_sections = self.get_sections_number()
        self._timestamp = self.get_time_stamp()
        self._characteristics = self.get_characteristics()

    def get_sections_number(self):
        start_offset = self.header_start_offset + 0x2
        return bytes_to_int(self, self.bin[start_offset: start_offset + self.definition['NUMBER_OF_SECTIONS']['length']])
    
    def get_time_stamp(self):
        start_offset = self.header_start_offset + 0x4
        unix_timestamp = bytes_to_int(self, self.bin[start_offset: start_offset + self.definition['TIME_DATE_STAMP']['length']])
        return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    def get_pointer_to_sym_table(self):
        start_offset = self.header_start_offset + 0x8

    def get_num_of_symbols(self):
        start_offset = self.header_start_offset + 0xC
    
    def get_size_of_optional_header(self):
        start_offset = self.header_start_offset + 0x10
    
    def get_characteristics(self):
        start_offset = self.header_start_offset + 0x12
        result = []
        characteristics = bytes_to_int(self, self.bin[start_offset: start_offset + self.definition['CHARACTERISTICS']['length']])
        
        for item in self.CHARAC_ENUM:
            if characteristics & item.value:
                result.append(item.name)
        
        return result

    def get_machine_target(self):
        start_offset = self.header_start_offset 
        machine_hex = hex(bytes_to_int(self, self.bin[start_offset: start_offset + self.definition['MACHINE']['length']]))

        if machine_hex == '0x184':      return 'Alpha AXP 32'
        elif machine_hex == '0x284':    return 'Alpha 64'
        elif machine_hex == '0x1d3':    return 'Matsushita AM33'
        elif machine_hex == '0x8664':   return 'AMD64'
        elif machine_hex == '0x1c0':    return 'ARM little endian'
        elif machine_hex == '0xaa64':   return 'ARM64 little endian'
        elif machine_hex == '0x1c4':    return 'ARM Thumb-2 little endian'
        elif machine_hex == '0x284':    return 'AXP 64'
        elif machine_hex == '0xebc':    return 'EFI byte code'
        elif machine_hex == '0x14c':    return 'Intel 386 compatible'
        elif machine_hex == '0x200':    return 'IA64'
        elif machine_hex == '0x6232':   return 'LoongArch 32'
        elif machine_hex == '0x6264':   return 'LoongArch 64'
        elif machine_hex == '0x9041':   return 'Mitsubish M32R'
        elif machine_hex == '0x266':    return 'MIPS16'
        elif machine_hex == '0x366':    return 'MIPS FPU'
        elif machine_hex == '0x466':    return 'MIPS16 FPU'
        elif machine_hex == '0x1f0':    return 'Power PC'
        elif machine_hex == '0x1f1':    return 'Power PC FP'
        elif machine_hex == '0x166':    return 'MIPS little endian'
        elif machine_hex == '0x5032':   return 'RISC-V 32'
        elif machine_hex == '0x5064':   return 'RISC-V 64'
        elif machine_hex == '0x5128':   return 'RISC-V 128'
        elif machine_hex == '0x1a2':    return 'Hitachi SH3'
        elif machine_hex == '0x1a3':    return 'Hitachi SH3 DSP'
        elif machine_hex == '0x1a6':    return 'Hitachi SH4'
        elif machine_hex == '0x1a8':    return 'Hitachi SH5'
        elif machine_hex == '0x1c2':    return 'Thumb'
        elif machine_hex == '0x169':    return 'MIPS little-endian WCE v2'
        else:                           return 'Unknow'