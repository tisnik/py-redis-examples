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

"""Walrus library usage - wait for a new message to be appended."""

from walrus import Database

db = Database()
stream = db.Stream("streamX")

message = stream.read(block=0, last_id="$")
print(message)
