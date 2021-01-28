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

"""Walrus library usage - adding (appending) a message to stream."""

from walrus import Database

db = Database()
stream = db.Stream("streamX")

message_id = stream.add({"foo": 10,
                         "bar": 20})
print(message_id)
