# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:07:20 2021

@author: sherin
"""

import datetime 


def countSundays(start_date,end_date):    
    
    delta = datetime.timedelta(days=1)
    sundays = 0
    
    while start_date <= end_date:
        if start_date.weekday()==6 and start_date.day==1:
            sundays+=1
        start_date += delta

    print(sundays)
    return sundays



fromDate = datetime.date(1901, 1,1)
toDate = datetime.date(2000, 12,31)
countSundays(fromDate,toDate)

