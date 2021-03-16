#!/bin/env python

# https://www.codewars.com/kata/5202ef17a402dd033c000009

# This was my least favorite so far only because the sample data
# did not accurately match all of test data.

# Also, I overestimated author's usage of the minor_words. I 
# expected them to throw crazy words in to ensure each item
# required specific review .. which they did not. title() 
# would probably have worked just fine. 

# Here is the original submitted function:

def title_case(title, minor_words=''):
    old_title=title.title()

    # Avoid empty data gotcha
    if not old_title:
        return ''
    
    # A minor words list to search
    minor_words=minor_words.lower().split()

    # Capitalize the first item
    new_title=old_title.split()[0].title()

    # Iterate through the remaining items
    for tw in old_title.split()[1:]:
        if tw.lower() in minor_words:
            new_title=new_title + ' ' + tw.lower()
        else:
            new_title=new_title + ' ' + tw
    return new_title.lstrip(' ')

print(title_case('a clash of KINGS', 'a an the of'))