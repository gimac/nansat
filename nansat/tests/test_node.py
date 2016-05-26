#------------------------------------------------------------------------------
# Name:         test_node.py
# Purpose:      Test the Node class
#
# Author:       Aleksander Vines
#
# Created:      2016-02-26
# Last modified:2016-02-26T16:00
# Copyright:    (c) NERSC
# Licence:      This file is part of NANSAT. You can redistribute it or modify
#               under the terms of GNU General Public License, v.3
#               http://www.gnu.org/licenses/gpl-3.0.html
#------------------------------------------------------------------------------
import unittest
from nansat.node import Node


class NodeTest(unittest.TestCase):
    def test_creation(self):
        tag = 'Root'
        value = '   Value   '
        anAttr = 'elValue'
        node = Node(tag, value=value, anAttr=anAttr)
        self.assertEqual(node.tag, tag)
        self.assertDictEqual(node.attributes, {'anAttr': anAttr})
        self.assertEqual(node.value, value.strip())

    def test_delete_attribute(self):
        tag = 'Root'
        value = '   Value   '
        anAttr = 'elValue'
        node = Node(tag, value=value, anAttr=anAttr)
        self.assertIn('anAttr', node.attributes)
        node.delAttribute('anAttr')
        self.assertNotIn('anAttr', node.attributes)

    def test_add_node(self):
        rootTag = 'Root'
        root = Node(rootTag)
        firstLevelTag = 'FirstLevel'
        firstLevel = Node(firstLevelTag)
        root += firstLevel
        self.assertIn(firstLevel, root.children)

    def test_add_nodes(self):
        rootTag = 'Root'
        root = Node(rootTag)
        firstLevelTag = 'FirstLevel'
        firstLevel = Node(firstLevelTag)
        root += firstLevel
        firstLevel2 = Node(firstLevelTag)
        root += firstLevel2
        firstLevel2ndTag = 'FirstLevel2ndTag'
        firstLevel3 = Node(firstLevel2ndTag)
        root += firstLevel3
        self.assertIn(firstLevel, root.children)
        self.assertIn(firstLevel2, root.children)
        self.assertIn(firstLevel3, root.children)

    def test_xml(self):
        rootTag = 'Root'
        root = Node(rootTag)
        firstLevelTag = 'FirstLevel'
        firstLevel = Node(firstLevelTag)
        root += firstLevel
        firstLevel2 = Node(firstLevelTag)
        root += firstLevel2
        firstLevel2ndTag = 'FirstLevel2ndTag'
        firstLevel3 = Node(firstLevel2ndTag)
        root += firstLevel3
        self.assertEqual(root.xml(),
                         ('<Root>\n'
                          '  <FirstLevel/>\n'
                          '  <FirstLevel/>\n'
                          '  <FirstLevel2ndTag/>\n'
                          '</Root>\n'),)

    def test_replace_node(self):
        rootTag = 'Root'
        root = Node(rootTag)
        firstLevelTag = 'FirstLevel'
        firstLevel = Node(firstLevelTag)
        root += firstLevel
        firstLevel2 = Node(firstLevelTag)
        root += firstLevel2
        firstLevel2ndTag = 'FirstLevel2ndTag'
        firstLevel3 = Node(firstLevel2ndTag)
        root.replaceNode(firstLevelTag, 1, firstLevel3)
        self.assertIn(firstLevel, root.children)
        self.assertNotIn(firstLevel2, root.children)
        self.assertIn(firstLevel3, root.children)
        self.assertEqual(len(root.children), 2)