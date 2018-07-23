import re

def longest_word(sent):
    """returns the longest word in a sentence string. If there are ties
    for the same length, the first longest word is returned. Punctuation
    is not taken into consideration.
    """
    
    word_list = sent.strip().split(' ')
    word_list = [re.sub('\W', '', word) for word in word_list]
    len_list = [len(word) for word in word_list]
    i = len_list.index(max(len_list)) # returns first item with max length. 
        
    return word_list[i]


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

