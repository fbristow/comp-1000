---
title: Testing attributes with pandoc
---

Making lists with labels
------------------------

### Section 1

Here's a list with some labels:

1. First item {#first-item}
2. Second item {:tag#first-item:}
3. Third item {:tag: #third-item}

### Section 2

Here's another list with some labels in section 2:

1. `Fourth item`{#fourth-item}
2. [Fifth item]{tag=this id=that}
    1. Can I do nested example lists? {:nested:}

Making references to labels
---------------------------

The (@first-item) that we looked at had (@second-item) underneath it. Then
came (@third-item). Does HTML render anything? Yes, it does!

What about the (@fourth-item)? Can we see that? How about (@fifth-item) and its
child (@sub-item-five)?
