#!/usr/bin/env python3
''' challenge on function '''
def main():
    ''' main function '''
    fruits = ['banana','apple','nuts','acorns','fruit_with_lonnnng_name']
    short = len([string.strip() for string in fruits if len(string) < 5])
    medium = len([string.strip() for string in fruits if len(string) >=5 and len(string) <10])
    lng = len([string.strip() for string in fruits if len(string) > 10])
    print("short: {}, medium: {}, long: {}".format(short, medium,lng))
main()

