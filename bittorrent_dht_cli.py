import sys
import asyncio
import secrets
from aiobtdht import DHT
from aioudp import UDPServer
import random


def usage():
    usage_mgs: """ usage: python bittorrent_dht_cli.py [INFO_HASH]"""
    print(uage_msg)

async def main(loop):

    initial_nodes = [
        ("67.215.246.10", 6881),  # router.bittorrent.com
        ("87.98.162.88", 6881),  # dht.transmissionbt.com
        ("82.221.103.244", 6881)  # router.utorrent.com
    ]

    udp = UDPServer()
    udp.run("0.0.0.0", random.randint(1024,65535), loop=loop)

    local_node_identifier = secrets.randbits(16*8)
    dht = DHT(local_node_identifier, server=udp, loop=loop)

    print("bootstrap")
    await dht.bootstrap(initial_nodes)
    print("bootstrap done")


    if len(sys.argv) == 1:
        mint_info_hash = "8df9e68813c4232db0506c897ae4c210daa98250"
        print(f"search peers for Linux Mint torrent ('{mint_info_hash}')")
        peers = await dht[bytes.fromhex("8df9e68813c4232db0506c897ae4c210daa98250")]
        info_hash = mint_info_hash

    else:
        print(f"search peer for Infohash: {sys.argv[1]}")
        info_hash = sys.argv[1]

    peers = await dht[bytes.fromhex(info_hash)]
    print("peers:", peers)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    #loop.run_forever()

