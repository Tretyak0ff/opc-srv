#!/usr/bin/env python3.10
import os
from dotenv import load_dotenv

load_dotenv()

IP_ADDR = os.getenv('IP_ADDR')
IP_PORT = os.getenv('IP_PORT')
URL = f'opc.tcp://{IP_ADDR}:{IP_PORT}/UA/Server'
