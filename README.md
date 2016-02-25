# Query Collections
### A set of classes that makes managing JSON objects easier within Python (and more?)

## Why?

When wanting to access an index of a JSON object (or a Python dictionary/map), we need to use ['member'] syntax. 
This is ok for simple JSON objects, but let's say you had a complex object andyou wanted a deeply nested element,
such as:
```
    dict_instance['member'][0]['items'][0]['id']
```

This is where query collections come in. Right now the supported structures are maps (python dictionaries) and 
lists. Here is how we can access the members in each:

Given a k:v map:
```json
{
    "population": {
        "faculty": [
            {
                "id": "103902",
                "name": "Cory",
                "field": "CS"
            },
            {
                "id": "6789",
                "name": "Ted",
            },
            {
                "id": "67874",
                "name": "Mike",
                "field": "CS"
            }
        ],
        "count": 3,
        "access_codes": [
            1, 2, 3
        ]
    }
}
```

This specific instance would be rather difficult to obtain information from,
and would require a lot of generators and other unnecessary bloat to achieve
a task as simple as "if there are any users who are faculty, return those with a 'field'
specified

Here is the naive solution with regular builtin Python functionality:
```python
    json_obj = ...
    if json_obj.get('population').get('faculty') is not None:
        matches = [f_member for f_member in json_obj['population']['faculty'] if 'field' in f_member]
        return matches
    return None_
```

Here is how we can perform the same operation with a query_dict:
```python
    json_obj = query_dict(...)
    matches = json_obj.query("population:faculty:*:field!")
```

In this example, `*` denotes "any member of the list faculty", and `!` means 'return true if field exist`. 
The wildcard operator, by default, returns any member who returns a value.

## Syntax

The syntax for queries is very easy to understand! To access a nested member of a parent, simply do:
parent:child. This can be chained over any amount of nesting. Of course this is in itself useful,
but with the addition of operators, the use case is much, much more clear!

Acceptable operators:
    - `*`: Wildcard operator. Returns the list of elements at the given index.
    - `!`: Exists operator. Returns true if the member exists.
    
Combination of rules is also acceptable:
    - The wildcard by default stops error reporting and returns all matching elements following itself in the
    query string. For example: .query("*:id!") returns all members of the first level where id exists
    
## Examples:

You may find a list of query examples in the /test directory. This includes all current combinations of operators
and basic error checking.

## query_dict and query_list

Currently this is all implemented through classes that inherit the dict and list class. 
The only additional functionality of these classes are dot access of dictionary members and
a 'length'/'len' property of lists.

#### query_dict
Members of the dictionary can be accessed from the dot operator:
```
>>> obj = query_dict({_
        "name": "Cory",
        "stats": {
            "coolness": "over9000"
        }
    })
>>> obj.name
"Cory"
>>> obj.stats.coolness
"over9000"
```

#### query len/length
```
>>> mlist = query_list([1,2,3])
>>> mlist.len
3
>>> mlist.length
3
```

## Roadmap

 - Equality operator for basic comparisons
 - Equality comparator
 
## License
    Query Collections

    The MIT License (MIT)

    Copyright (c) 2016 Cory Forward

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.