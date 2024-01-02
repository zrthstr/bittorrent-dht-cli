# bittorrent-dht-cli

Simple CLI tool to query the [BitTorrent Mainline](https://en.wikipedia.org/wiki/Mainline_DHT) [DHT network](https://en.wikipedia.org/wiki/Distributed_hash_table), written in Python.

The code is closely based on [aiobtdht](https://github.com/bashkirtsevich-llc/aiobtdht)'s README.md.

## Install

Activate the Python virtual environment and install dependencies:

```bash
% git clone git@github.com:zrthstr/bittorrent-dht-cli.git
% cd bittorrent-dht-cli
% python -m venv venv
% source venv/bin/activate    # Activate the virtual environment
% pip install -r requirements.txt  # Install required Python packages
```

## Usage:
```bash
% source bin/activate ## only if not done before inside in this shell
% python bittorrent_dht_cli.py 8df9e68813c4232db0506c897ae4c210daa98250

# Expected example output:
bootstrap
bootstrap done
search peer for Infohash: 8df9e68813c4232db0506c897ae4c210daa98250
peers: {('83.xxx.227.166', 16881), ('95.xxx.216.143', 51984), [...]}
```
