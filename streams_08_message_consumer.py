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

"""Simple microbenchmark - better burst message consumer."""

import time

from walrus import Database

db = Database()
stream = db.Stream("streamY")

start = time.time()

messages = stream.read(last_id=0, count=100000)
counter = len(messages)

end = time.time()
print("Consumer duration for {} messages: {} seconds".format(counter, (end - start)))
