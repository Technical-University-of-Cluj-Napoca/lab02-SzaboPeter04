from urllib.request import Request,urlopen

class Node:
    def __init__(self,word:str)->None:
        self.word:str=word
        self.left:Node=None
        self.right:Node=None

class BST:
    def __init__(self,source:str,**kwargs)->None:
        url=bool(kwargs.get("url",False))
        file=bool(kwargs.get("file",False))
        if not (url or file):
            raise ValueError("Url or file must be true")
        if url and file:
            raise ValueError("Only one out of url or file can be true")
        if url:
            content=urlopen(source)
            word_list=content.read().decode("utf-8")
        elif file:
            file=open(source,"r",encoding="utf-8")
            word_list=file.read()
        words=[w.strip().lower() for w in word_list.splitlines() if w.strip()]
        def construct(left:int,right:int)->Node:
            if left>right:
                return None
            node=Node(words[(left+right)//2])
            node.left=construct(left,(left+right)//2-1)
            node.right=construct((left+right)//2+1,right)
            return node

        self.root=construct(0,len(words)-1)

    def autocomplete(self,prefix:str)->list[str]:
        self.results=[]
        self._collect(self.root,prefix)
        return self.results

    def _collect(self,node:Node,prefix:str)->None:
        if node==None:
            return
        if node.word>=prefix:
            self._collect(node.left,prefix)
        if node.word.startswith(prefix):
            self.results.append(node.word)
        if node.word<=prefix:
            self._collect(node.right,prefix)