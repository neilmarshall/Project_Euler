"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1,000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

def number_as_word(n):
    """
    Return count of letters when a number is written as a word

    >>> number_as_word(20)
    'twenty'

    >>> number_as_word(115)
    'one hundred and fifteen'

    >>> number_as_word(342)
    'three hundred and forty two'

    >>> number_as_word(5480)
    'five thousand four hundred and eighty'
    """
    digit_map = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    
    tens_map = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    
    number = ""
    
    # parse 1,000s
    while n >= 1000:
        return digit_map[n // 1000] + " thousand " + number_as_word(n % 1000)
    
    # parse 100s
    while n >= 100:
        return digit_map[n // 100] + " hundred " + ("and " if n % 100 != 0 else "") + number_as_word(n % 100)
    
    # parse tens
    while n >= 20:
        return tens_map[10 * (n // 10)] + (" " + number_as_word(n % 10) if n % 10 != 0 else "")
    
    # parse digits
    return digit_map[n]
    

def PE_17():
    """
    Return count of letters for all numbers between 1 and 1,000 when
    written as words

    >>> PE_17()
    21124
    """
    return sum(len(number_as_word(n).replace(' ', '')) for n in range(1, 1001))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
