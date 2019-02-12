#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající systém Redis

#
#  (C) Copyright 2018, 2019  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#



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
    for i in range(0, 21):
        print("Publishing message to " + channel)
        message = "zprava #{}".format(i)
        r.publish(channel, message)

        time.sleep(0.001)


pub("127.0.0.1", 6379, CHANNEL_NAME)
