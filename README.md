# Pyparserai
This is a parser that collects information about a coin from the CoinMarketCap website.
## Installation
To use, you need to install from source
```bash
git clone https://github.com/aishabazylzhanova/pyparserai
cd pyparserai
python3 setup.py install
```
## Usage
```python
from pyparserai import Prai
pars = Prai()
```
## Examples
```python
pars.GetInfo('bitcoin')
```
