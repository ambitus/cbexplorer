# cbexplorer

The control block explorer project

## Goal

This project intends to make z/OS data structures available to Python developers.
To achieve this, the Assembler / C header /other source code used in z/OS are converted to [zml](https://github.com/ambitus/zml) which contains then all necessary information on the structure and organization of the described data structures.
The zml files are then converted by the CB Explorer to Python classes which allow access to the fields in the data structures in a pythonic way.

![Build Process](/resorces/CB_Explorer-build.png?raw=true)

## Access to data

It is necessary to distinguish between two way of accessing data.

![Data Extraction](/resorces/CB_Explorer-access.png?raw=true)

One is access to system memory to read (and potentially write) data from/to the system in an immediate way. This is especially relevant if there is a need to have interact with z/OS internal data that has not yet been written to SMF records. By using the python module [cytpes](https://docs.python.org/3/library/ctypes.html) it is possible to access the system memory by simply providing an address (see AddressDescriptor in LocatorDescriptor)

The second one is access to data structures that have been dumped to a binary file. These data structures can be navigated in the same way. This can be achieved by using standard Python modules for file handling (see FileDescriptor in LocatorDescriptor).



## Usage
Clone the repository via `git clone --recursive` to get the submodules or perform `git submodule update --init --recursive`.

Use pip to install the requirements `pip install -r requirements.txt --user`.

Currently the `test.sh` will generate the control block mappings below the `tests/` folder. To use them simply include them in Python via

```python
from tests.controlblocks import *
from zospy.locate import LocatorFactory

mem_locator = LocatorFactory.create('address', 0)

psa = PSA(mem_locator)
ascb = ASCB(mem_locator.new_from(psa.PSAANEW))
...
```

