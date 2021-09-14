'''
@Author: Ariprasath
@Date: 2021-09-13 09:49:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-14
Title: Open a CSV file, count the number of rows, return the extension of the file and return the header from the CSV file
'''

import csv

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class NotCsvError(Error):
    def __init__(self):
        self.message="The given file is not a csv file"
        super().__init__(self.message)
        super().__str__()
class NotStringError(Error):
    def __init__(self):
        self.message="The given file name is not a string"
        super().__init__(self.message)
class HeadersNotListError(Error):
    def __init__(self):
        self.message="All headers should be contained within a list"
        super().__init__(self.message)
class HeadersNotStringsError(Error):
    def __init__(self):
        self.message="Headers should be strings"
        super().__init__(self.message)


class CsvManipulsation():
    def __init__(self,file_name):
        self.file_name=file_name
        self.csv_data=list()


    def read_csv(self):
        '''
        Description: 
            Reads a CSV file and adds all the data to a list. Data will be in a nested list format.
        Parameter: 
            None
        Return:
            None
        '''   
        with open(self.file_name,"r") as csv_file:
            self.csv_reader=csv.reader(csv_file)
            for element in self.csv_reader:
                self.csv_data.append(element)

    def check_read_csv(self):
        '''
        Description:
            checks the csv file name entered and reads the csv file
        Parameter:
            None
        Return:
            csv.data(list): contains data red from the csv file
        Raises:
            NotStringError: If the file name entered is not a string
            NotCsvError: If the file is not a csv file
        '''
        try:
            if type(self.file_name)!=str:
                raise NotStringError
            elif self.file_name.rsplit(".")[-1]!="csv":
                raise NotCsvError
            else:
                self.read_csv()
        except NotStringError as S:
            raise S
        except NotCsvError as C:
            raise C
        else:
            return self.csv_data

    def count_rows(self):
        '''
        Description:
            Counts the number of rows of data in the csv file. Header row is not counted
        Parameter:
            None
        Return:
            count(int): The nunmber of rows of data in the csv file
        '''
        self.count=0
        for element in self.csv_data[1:]:
            self.count+=1
        return self.count

    def header_check(self,headers):
        '''
        Description:
            Checks whether the given header and the header in the csv file is same or not
        Parameter:
            headers(list): contains strings of all headers
        Return:
            A string "Headers match" if both the headers are same
        Raises:
            HeadersNotListError: If the passed parameter is not a list
            HeadersNotStringError: If the passed parameter contains values other than string data type
        '''
        try:
            if type(headers)!=list:
                raise HeadersNotListError
            elif not(all(isinstance(x,str) for x in headers)):
                raise HeadersNotStringsError
            else:
                if self.csv_data[0]==headers:
                    return "Headers match"
        except HeadersNotListError as L:
            raise L
        except HeadersNotStringsError as S:
            raise S
