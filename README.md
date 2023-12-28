# dotnet-bin-dump
Dumping data out of PE 

Extract: 
  DOS HEADER
  FILE HEADER
  OPTIONAL HEADER
  SECTIONS:
    *.TEXT
    *.DATA
    *.RDATA

TARGET FRAMEWORK: .NET
  TABLES STREAM:
    *FIELD
    *METHOD
  STRINGS
  US

USAGE:

positional arguments:
  file_paths   Path location of the payload

options:
  -h, --help   show this help message and exit
  -d, --debug  Enable debugging logging
  --headers    Dump bin headers
