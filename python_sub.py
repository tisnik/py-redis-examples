#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající systém Redis


import redis
import time


CHANNEL_NAME = "kanal1"


def connect(host, port):
    """Připojení k Redisu na specifikované adrese a portu."""
    return redis.Redis(host=host, port=port)


def sub(host, port, channel):
    """Operace typu SUB - příjem zpráv z Redisu."""
    r = connect(host, port)
    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    while True:
        print("Waiting for message published on " + channel)
        message = pubsub.get_message()
        if message:
            print("type {type}  message '{message}'".format(type=message["type"],
                                                            message=message["data"]))
        else:
            time.sleep(1)


sub("127.0.0.1", 6379, CHANNEL_NAME)
