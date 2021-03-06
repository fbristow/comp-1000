#!/usr/bin/python3

import re
import panflute as pf

# e.g., :outcome#identifier:, :outcome:, or &course&
tag_pattern = re.compile("(?::[a-z#-]+:|&\d+&)")

def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.ListItem) and elem.content and isinstance(elem.content[0], pf.Plain):
        plain = elem.content[0]

        stringy = pf.stringify(elem)
        matches = tag_pattern.findall(stringy)
        identifier = None
        outcome = None

        # strip the tags from the element before we proceed any further
        for tag in matches:
            elem = elem.replace_keyword(tag, pf.Space())

        # strip the trailing whitespace (this is equivalent to a trim operation)
        while type(plain.content[-1]) in (pf.Space, pf.SoftBreak):
            del plain.content[-1]

        # gather all of the tags/IDs on the learning objective into something
        # that we can write out to an attribute on the span.
        outcomes = []
        identifiers = []
        courses = []
        for tag in matches:
            if "&" in tag:
                # this is not a tag, it's a course reference
                courses.append(tag[1:-1])
            elif "#" in tag:
                identifiers.append(tag[tag.index("#")+1:-1])
                outcomes.append(tag[:tag.index("#")] + ":")
            else:
                outcomes.append(tag)
        outcomes = " ".join(outcomes)
        courses = " ".join(courses)

        if len(identifiers) == 1:
            identifier = identifiers[0]
        elif len(identifiers) > 1:
            pf.debug(f"Found multiple IDs: {identifiers}")
            identifier = identifiers[0]
        else:
            identifier = ""

        # Take the existing contents of the `pf.Plain` that's the first child
        # of the `pf.ListItem` and embed that into a `pf.Span`. Then make the
        # `pf.Span` the only child of the `pf.Plain`.
        if matches:
            span = pf.Span(*plain.content, identifier=identifier,
                    attributes={"outcomes": outcomes, "course":
                        pf.stringify(doc.metadata["title"])}) 
            if courses:
                span.attributes["used-in"] = courses
            plain.content.clear()
            plain.content.append(span)

        return elem
    
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
