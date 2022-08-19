#!/usr/bin/env python3.10
import logging
import asyncio
from server import server


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(server())
