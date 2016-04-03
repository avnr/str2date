# str2date

### Proper Parser of ISO 8601 Calendar Date and Time Strings

`str2date` accepts a string argument and returns a `datetime` object. If the string is not a proper ISO 8601 Calendar Date with an optional time then `str2date` returns None.

Some points to note:

- The delimiter between the date portion and time portion can be either T per the standard or a space character.

- In absence of a timezone UTC is assumed - `str2date` won't ever return a naive date.

- In line with the standard, time can be represented partially as hh, hh:mm, or as a full hh:mm:ss, in all cases followed by an optional fraction that will be properly computed.

- Time fraction separator can be either a period (.) or a comma (,). No limit to the number of fraction digits, although the result will be rounded to the nearest microsecond.

Examples:

    >>> from str2date import str2date
    >>> print( str2date( '1998-07-06T05:04:03-02:00' ))
    1998-07-06 05:04:03-02:00
    >>> print( str2date( '1998-07-06T05:04:03.555-02:00' ))
    1998-07-06 05:04:03.555000-02:00
    >>> print( str2date( '1998-07-06 05:04:03,555-02:00' ))
    1998-07-06 05:04:03.555000-02:00
    >>> print( str2date( '1998' ))
    1998-01-01 00:00:00+00:00

Install with `pip install str2date` or copy `str2date.py` to your project.

MIT License.
