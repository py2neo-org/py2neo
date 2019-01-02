#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2019, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from py2neo import Node, Relationship


def test_can_delete_relationship(graph):
    a = Node()
    b = Node()
    r = Relationship(a, "TO", b)
    graph.create(r)
    assert graph.exists(r)
    with graph.begin() as tx:
        tx.delete(r)
    assert not graph.exists(r)
    assert not graph.exists(a)
    assert not graph.exists(b)
