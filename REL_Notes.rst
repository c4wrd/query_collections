Query Collections Release Notes
===============================

This document will serve as purpose for documenting any changes with each release.

Releases are grouped by major, minor, version and listed by build:: MAJOR.MINOR.VERSION.BUILD

0.0.1 ALPHA
===========
3a(4)
____
 - Fixed small issue with stream.skip

3a(3)
_____
 - Fixed 'mapToInt' method name
 - Added additional Optional getAs return types
 - Small bug fixes

3a(1-2)
_____
 - Fixed issue with the Stream min, max, and forEach methods

3a(0)!
______
 - Streams are here! This is a 1 to 1 copy of the Java 8 Stream API and works wonderously! Very useful when combined
 with lambda expressions! Most functionality exists, please feel free to open up tickets for issues that have been missed. As
 for the default single threaded nature of Python, there is no parallel capabilities (as such, if you demand speed Python wouldn't
 be the favored choice regardless)

2a(10)
______
 - Fixed issue where instance variables are not returned correctly

2a(9)
_____
 - Fixed query_dict setattr and delattr methods, previously non-working.

2a(8)
_____
 - Added basic implementation of list filtering, which allows us to query lists or items that match specific criteria.
 View the readme for updated tutorial on how to filter.

2a(7)
-----
 - We can now query an item with the index operators! When accesing elements of a query_dict or query_list
    with the index operators (braces), you can prefix the index value (a string!) with '?' and it will
    perform a query instead of accessing that element.

2a(5)
-----
 - Fixed issue where wildcard returns list instead of a query_list, preventing further query chains.

2a(4)
-----
 - Addition of this release notes file!

2a(3)
-----
 - Fixed issue where a tuple was not properly queried with a wildcard

2a(2)
-----
 - Build version increment, addition of 2a(1)

2a(1)
-----
 - Welcome to 0.0.1.2a! There was a lot of internal refactoring removing circular dependencies, and overall cleaner.
 - Now you can query any dict or list object, it does not need to be a query_dict or query_list
        - use the 'query' method in the package