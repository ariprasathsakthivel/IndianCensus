'''
@Author: Ariprasath
@Date: 2021-09-14 09:49:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-14
Title: Open a CSV file, count the number of rows, return the extension of the file and return the header from the CSV file. Also filters data from a file, create a new file and add all the data including the filtered data
'''

import csv
import json
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
class FileNotReadedError(Error):
    def __init__(self):
        self.message="No file is readed. Please read the file before filtering the data"
        super().__init__(self.message)



class CsvManipulsation():
    def __init__(self,file_name):
        self.file_name=file_name
        self.csv_data=list()
        self.csv_data_dict=dict()


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

    def dict_convert(self):
        '''
        Description:
            Generates a dictionary containing first index element as key and third index element as value.
        Parameter:
            None
        Returns:
            None
        '''
        try:
            if self.csv_data==[]:
                raise FileNotReadedError
            else:
                for element in self.csv_data[1:]:
                    self.csv_data_dict[element[1]]=element[3]
        except FileNotReadedError as F:
            raise F
        else:
            return self.csv_data_dict
            
    def new_csv(self,census_data):
        '''
        Description:
            Opens a csv file if exists or create a new csv file as a writer. adds a column of values dictionary into the csv file passed.
        Parameter:
            census_data(list): contains multiple lists containing data
        Returns:
            None
        '''
        with open("../data/StateCensusDataupdated.csv",'w', newline="") as new_file:
            csv_writer=csv.writer(new_file)
            census_data[0].append("StateCode")
            for element in census_data[1:]:
                if list(self.csv_data_dict.keys()).count(element[0])>0:
                    element.append(self.csv_data_dict[element[0]])
                else:
                    element.append("None")
                    
            csv_writer.writerows(census_data)
            return census_data
            


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

    def csv_json(self,json_file_path):
        '''
        Description:
            Converts a csv file into a json file
        Parameters:
            json_file_path(string): The complete path of the file
        Returns:
            None
        Raises:
            NotStringError: Thrown if the entered json_file_path is not a string
        '''
        try:
            if type(json_file_path)!=str:
                raise NotStringError
            else:
                data_dict=dict()
                with open(self.file_name,'r') as csv_file:
                    csv_reader=csv.DictReader(csv_file)
                    with open(json_file_path,'w') as json_file:
                        for rows in csv_reader:
                            json.dump(rows,json_file)
                            json_file.write("\n")
        except NotStringError as S:
            raise S

if __name__=="__main__":
    census=CsvManipulsation("../data/StateCensusData.csv")
    census.csv_json("../data/StateCensusData.json")