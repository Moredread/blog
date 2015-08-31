---
layout: post
title: Python pitfall with mutable default parameters
date: 2012-10-14 20:00:00
comments: true
tags: english, python, programming
---

We stumbled upon an unexpected way default parameters work while writing python code for our current game project.

In Python you can specify a default value for a function parameter, which is
used when the function is called with less parameters than the function needs.

``` python

>>> def printHello(text="Hello World!"):
...  print text
>>>
>>> printHello()
Hello World!
```

In python strings are immutable, that means you can't change it after creation. When
you for example concatenate two strings a new one is created, so there is no way
to change the default parameter string.

But what happens if you use an empty list as the default parameter? I
expected to always get an empty list.

So the following function should always print the same.

``` python
>>> def append_one(values=[]):
...   values.append("One")
...   print values
>>> append_one()
['One']
>>> append_one()
['One', 'One']
```

What happens here?

A list is mutable, that means you can add or change elements in the list. And
you get passed the _same_ list instance each time on a call to _append_one_, as
variables are passed by reference in python. So this behaviour is actually not
that surprising. The same is the case for each other mutable class you pass as a
default argument.

But how can you use a mutable object?

There are several ways, but I like the following.

Instead of passing the object directly, we pass _None_ and check for it in the
function.

```
>>> def append_one(values=None):
...     values = values or []
...     values.append("One")
...     print values
...
>>> append_one()
['One']
>>> append_one()
['One']
>>> append_one(['Zero'])
['Zero', 'One']
```

We also used the compact _or_ notation, see the [Python documentation][] for how
that works.

*Edit:* There is also a good [post](http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument) on stackoverflow answering why it was done this way.

[Python documentation]: http://docs.python.org/reference/expressions.html#or "Python documentation"
