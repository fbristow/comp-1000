#!/usr/bin/python3

import panflute as pf

def prepare(doc):
    pass

def action(elem, doc):
    if hasattr(elem, 'attributes') and 'tag' in elem.attributes:
        pass
    if isinstance(elem, pf.Span) and hasattr(elem, 'identifier'):
        elem.content.append(pf.RawInline(f"\\label{{{elem.identifier}}}", format='tex'))

    return elem
        
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
