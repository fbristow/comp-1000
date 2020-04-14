#!/usr/bin/python3

import panflute as pf

def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.ListItem):
        pf.debug(elem)
    
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
