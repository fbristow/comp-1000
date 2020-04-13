#!/usr/bin/python3

import panflute as pf

def prepare(doc):
    pass

def action(elem, doc):
    if hasattr(elem, 'attributes') and 'tag' in elem.attributes:
        pf.debug(elem)
        
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
