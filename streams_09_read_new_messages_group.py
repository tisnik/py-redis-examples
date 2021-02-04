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

"""Reading messages by a consumer that is part of message consumer group."""

from walrus import Database

db = Database()

cg = db.consumer_group("a-group", ["streamX"])
cg.create()
cg.set_id('$')

while True:
    messages = cg.read(block=0, count=1)
    print(messages[0])
