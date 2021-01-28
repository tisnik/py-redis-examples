#!/usr/bin/python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Simple microbenchmark - burst message producer."""

import time

from walrus import Database


db = Database()
stream = db.Stream("streamY")

MESSAGES = 100000

start = time.time()

for i in range(0, MESSAGES):
    message_id = stream.add({"id": i,
                             "last": "y" if i == MESSAGES - 1 else "n"})

end = time.time()
print("Producent duration for {} messages: {} seconds".format(MESSAGES, (end - start)))
