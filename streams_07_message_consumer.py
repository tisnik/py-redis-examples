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

"""Simple microbenchmark - burst message consumer."""

import time

from walrus import Database

db = Database()
stream = db.Stream("streamY")

counter = 0

start = time.time()

last_id = "0"

while True:
    messages = stream.read(block=0, last_id=last_id, count=1)
    message = messages[0]
    last_id = message[0]
    content = message[1]
    counter += 1
    if b"last" in content and content[b"last"] == b"y":
        break

end = time.time()
print("Consumer duration for {} messages: {} seconds".format(counter, (end - start)))
