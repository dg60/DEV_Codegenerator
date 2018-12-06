"""
Base Class for the generators
Author: dgrill
Date: 26 Nov 2018
"""


class BaseGen(object):

    # read values from the pandas dataframe
    def _readValues(self,dataframe_):
        values = dataframe_.values
        lst_values = []

        for value in values:
            lst_values.append(value)

        return lst_values


