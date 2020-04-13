---
title: Testing example lists with pandoc
---

Making lists with labels
------------------------

### Section 1

Here's a list with some labels:

(@first-item)  First item
(@second-item) Second item
(@third-item)  Third item

### Section 2

Here's another list with some labels in section 2:

(@fourth-item) Fourth item
(@fifth-item) Fifth item
    (@sub-item-five) Can I do nested example lists?

Making references to labels
---------------------------

The (@first-item) that we looked at had (@second-item) underneath it. Then
came (@third-item). Does HTML render anything? Yes, it does!

What about the (@fourth-item)? Can we see that? How about (@fifth-item) and its
child (@sub-item-five)?
