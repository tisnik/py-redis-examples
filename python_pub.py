#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající systém Redis


import redis
import time


CHANNEL_NAME = "kanal1"


def connect(host, port):
    """Připojení k Redisu na specifikované adrese a portu."""
    return redis.Redis(host=host, port=port)


def pub(host, port, channel):
    """Operace typu PUB - publikace zpráv do Redisu."""
    r = connect(host, port)

    # budeme publikovat deset zpráv
    for i in range(0, 11):
        print("Publishing message to " + channel)
        message = "zprava #{}".format(i)
        r.publish(channel, message)

        time.sleep(1)


pub("127.0.0.1", 6379, CHANNEL_NAME)
