
# HTML Message Splitter

### Script `msg_split.py`


## The project structure

```
./
    ├── examples/           1. folder with html file
    │   └── source.html     2. html file
    ├── scripts             3. additional classes and scripts
    │   │── exceptions.py   4. custom exception
    │   │── splitter.py     5. class Splitter with main logic
    │   └── tag.py          6. class Tag
    ├── tests               7. Unit tests
    │   │── test-2.html     ----//----
    │   └── test-3.html     ----//----
    ├── msg_split.py        8. main script
    ├── requirements.txt    9. dependencies  
    └── README.md
```

## The libraries used
* Python 3.12
* unit tests: pytest
* argparse (standard library)


## Getting start

#### Clone the repository and go to the repository folder
```shell
git clone
```

#### Set up a Virtual Environment and activate it

```shell
python -m venv venv
```
```shell
source venv/bin/activate
```

#### Install dependencies
```shell
pip install -r requirements.txt
```

### Launch tests
```shell
pytest -v
```

### Scripts to test `msg_split.py` based on the provided file

```shell
python msg_split.py --max-len=4096 "./examples/source.html"
```

```shell
python msg_split.py --max-len=4396 "./examples/source.html"
```

```shell
python msg_split.py --max-len=4296 "./examples/source.html"
```









python msg_split.py --max-len=4096 "./examples/source.html"
