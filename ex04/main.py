import sys
import search_engine
from BST import BST

def parse_kwargs(args):
    arguments={}
    for item in args:
        key,value=item.split("=",1)
        if value=="True":
            value=True
        else:
            value=False
        arguments[key]=value
    return arguments

if __name__=="__main__":
    source=sys.argv[1]
    kwargs=parse_kwargs(sys.argv[2:])
    bst=BST(source,**kwargs)
    search_engine.search_loop(bst)