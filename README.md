# Codegenerator for PLC´s (BETA)


## GUI Interface

![BuR](doc/img/CodeGen_BuR.png)

## Supported PLC´s

* B&R Automation Studio 4.x.x  
  * Structured Text (ST)
  * C++ (CPP) 
* Siemens TIA_V15
  * Structured Text (ST)

### Supported platform
* Linux
  * Ubuntu 16.04
  * Ubuntu 18.04
* Windows 7, 10 

### Install for Development

* Install Python 3 runtime (>= V3.6.6)
  * Windows [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
  * Linux [https://docs.python-guide.org/starting/install3/linux/](https://docs.python-guide.org/starting/install3/linux/)
  
**Install development dependencies**
1. cd to the directory where requirements.txt is located
2. activate your virtualenv
3. run
```bash
$ pip install -r requirements.txt
```

### Build from Source

1. Install pyinstaller [https://www.pyinstaller.org/](https://www.pyinstaller.org/)
2. in your shell run
```bash
$ pyinstaller build.spec
```

## Documentation

German:  
[CodeGenerator German Documentation](http://www.dgrill.at/portfolio/05-CodeGenerator/)



