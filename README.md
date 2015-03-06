# useless
Useless is useless. Oh yeah, and parses bit and pieces of ELF and PE
dynamic libraries

## usage

```
$ usls.py --help
usage: useless [-h] [-H] [-s] [-S] library

Useless is useless. Oh yeah, and parses bit and piecesof ELF and PE dynamic
libraries

positional arguments:
  library         library to parse

optional arguments:
  -h, --help      show this help message and exit
  -H, --header    print the Header
  -s, --sections  print sections list
  -S, --symbols   print content of dynamic symbol table
```


##installation

```
python setup.py build
python setup.py install
```

##TODO
* add support for ELF32 and PE32+
* add a better support for magic number and format/type/capabilities detection
* add error checking more or less everywhere. now the system with probably
  crash with a python stacktrace if anything goes wrong
* better support for true Unicode strings in PE
* better support for weird 8 bytes names/address_to_name_in_string_form for PE
* add support for all the neglected structures
* add writing support (yeah, sure)
