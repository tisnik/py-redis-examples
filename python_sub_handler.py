#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající systém Redis

#
#  (C) Copyright 2018, 2019, 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#


"""Operace typu SUB - čtení zpráv z Redisu."""

import redis
import time


CHANNEL_NAME = "kanal1"


def connect(host, port):
    """Připojení k Redisu na specifikované adrese a portu."""
    return redis.Redis(host=host, port=port)


def handler(message):
    """Callback funkce (handler) zavolaná při přijetí zprávy."""
    print("type {type}  message '{message}'".format(type=message["type"],
                                                    message=message["data"]))


def sub(host, port, channel):
    """Operace typu SUB - čtení zpráv z Redisu."""
    r = connect(host, port)
    pubsub = r.pubsub()
    pubsub.subscribe(**{channel: handler})
    while True:
        message = pubsub.get_message()
        if message:
            print(message)
        else:
            time.sleep(1)


sub("127.0.0.1", 6379, CHANNEL_NAME)
