#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    str2date version 0.9 - Proper Parser of ISO 8601 Calendar Date and Time Strings
#    Copyright (c) 2016 Avner Herskovits
#
#    MIT License
#
#    Permission  is  hereby granted, free of charge, to any person  obtaining  a
#    copy of this  software and associated documentation files (the "Software"),
#    to deal in the Software  without  restriction, including without limitation
#    the rights to use, copy, modify, merge,  publish,  distribute,  sublicense,
#    and/or  sell  copies of  the  Software,  and to permit persons to whom  the
#    Software is furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this  permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT  WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE  WARRANTIES  OF  MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR  ANY  CLAIM,  DAMAGES  OR  OTHER
#    LIABILITY, WHETHER IN AN  ACTION  OF  CONTRACT,  TORT OR OTHERWISE, ARISING
#    FROM,  OUT  OF  OR  IN  CONNECTION WITH THE SOFTWARE OR THE  USE  OR  OTHER
#    DEALINGS IN THE SOFTWARE.
#
import datetime
from re import compile

_date_re  = compile( '^([0-9]{4})(?:\-(0[0-9]|1[0-2])(?:\-([0-2][0-9]|3[01])(?:(?:T|\s)([01][0-9]|2[0-4])(?:\:([0-5][0-9])(?:\:([0-5][0-9]|60))?)?(?:[\.,]([0-9]+))?([zZ]|[+-](?:[01][0-9]|2[0-4])\:[0-5][0-9])?)?)?)?$' )

def str2date( string ):

    YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MICROSECOND, TIMEZONE = 0, 1, 2, 3, 4, 5, 6, 7

    parsed = _date_re. match( string )
    if parsed is None: return None

    parsed = parsed. groups()
    if parsed[ TIMEZONE ] is None or parsed[ TIMEZONE ] in 'zZ':
        zone = 0
    else:
        tzh, tzm = list( map( int, parsed[ TIMEZONE ]. split( ':' )))
        if parsed[ TIMEZONE ][ 0 ] is '-':
            zone = tzh * 3600 - tzm * 60
        else:
            zone = tzh * 3600 + tzm * 60
    minute = int( parsed[ MINUTE ]) if parsed[ MINUTE ] is not None else 0
    second = int( parsed[ SECOND ]) if parsed[ SECOND ] is not None else 0
    micros = 0
    if parsed[ MICROSECOND ] is not None:
        fraction = float( '0.' + parsed[ MICROSECOND ])
        if parsed[ MINUTE ] is None:
            comp = 3600 * fraction
            minute = int( comp / 60 )
            second = int( comp - 60 * minute )
            micros = int( 1000000 * ( comp - int( comp )))
        elif parsed[ SECOND ] is None:
            second = int( 60 * fraction )
            micros = int( 60000000 * fraction - 1000000 * second  )
        else:
            micros = int( fraction * 1000000 )

    try:
        result = datetime. datetime(
            year        = int( parsed[ YEAR ]),
            month       = int( parsed[ MONTH ]) if parsed[ MONTH ] is not None else 1,
            day         = int( parsed[ DAY ])   if parsed[ DAY ]   is not None else 1,
            hour        = int( parsed[ HOUR ])  if parsed[ HOUR ]  is not None else 0,
            minute      = minute,
            second      = second,
            microsecond = micros,
            tzinfo      = datetime. timezone( datetime. timedelta( seconds = zone )))
    except:
        result = None

    return result

if __name__ == '__main__':
    from sys import argv
    print( str2date( argv[ 1 ]))

