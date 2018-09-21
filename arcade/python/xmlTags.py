import xml.etree.ElementTree as ET
from collections import OrderedDict

def dedup_order(dic):
    new_dic = {}
    for n in dic:
        new_dic[n] = sorted(list(set(dic[n])))
    return new_dic
    
def get_depth(node, tag=None, depth=0):
    tag = tag if tag is not None else OrderedDict()
    tag.setdefault(node.tag, depth)
    for child in node:
        tag.update(get_depth(child, tag, depth+1))
    return tag

def get_params(xml):
    root = ET.fromstring(xml)
    arr = []
    stack = [root]
    dic =  {}
    if root.attrib:
        dic[root.tag] = [k for k in root.attrib.keys()]
    result_stack = []
    tree = {}
    while stack:
        tmp = {}
        root = stack.pop()
        #print("root.ta", root.tag)
        #print("root attrib:", root.attrib)
        if root.tag not in tree:
            tree[root.tag] = {}
        else:
            tree = tree[root.tag]
        for child in root:
            for k in child.attrib.keys():
                #print("rootKKK:", k)
                if child.tag not in dic:
                    dic[child.tag] = [k]
                else:
                    dic[child.tag].append(k)
            stack.insert(0,child)
    dic = dedup_order(dic)
    return dic

def xmlTags(xml):
    dic = get_params(xml)
    t = ET.fromstring(xml)
    orders =get_depth(t) 
    res = []
    #print("orderes", orders)
    #print("d",dic)
    for o in orders:
        #print("o:", orders[o])
        if o in dic:
            res.append('--' * orders[o] + o + '(' + ', '.join(dic[o]) +')')
        else:
            res.append('--' * orders[o] + o + '()')
    return res
