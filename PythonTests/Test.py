'''
@Author: Ariprasath
@Date: 2021-09-14 15:28:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-13
Title: Test the CencusAnalyser module using pytest
'''
import sys
import pytest
sys.path.append("E:\CFP\Python\IndianCensus")
from IndianCensusAnalyser import CensusAnalyser


class TestCensusAnalyser():

    @pytest.fixture()
    def obj(self):
        self.obj1=CensusAnalyser.CsvManipulsation("../data/StateCensusData.csv")
        self.obj2=CensusAnalyser.CsvManipulsation("../data/StateCode.csv")
        return self.obj1,self.obj2

    def test_open_csv(self,obj):
        state_data=[['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm'], ['Uttar Pradesh', '199812341', '240928', '828'], ['Maharashtra', '112372972', '307713', '365'], ['Bihar', '103804637', '94163', '1102'], ['West Bengal', '91347736', '88752', '1029'], ['Madhya Pradesh', '72597565', '308245', '236'], ['Tamil Nadu', '72138958', '130058', '555'], ['Rajasthan', '68621012', '342239', '201'], ['Karnataka', '61130704', '191791', '319'], ['Gujarat', '60383628', '196024', '308'], ['Andhra Pradesh', '49386799','162968', '303'], ['Odisha', '41947358', '155707', '269'], ['Telangana', '35286757', '114840', '307'], ['Kerala', '33387677', '38863', '859'], ['Jharkhand', '32966238', '79714', '414'], ['Assam', '31169272', '78438', '397'], ['Punjab', '27704236', '50362', '550'], ['Chattisgarh', '25540196', '135191', '189'], ['Haryana', '25353081', '44212', '573'], ['Jammu and Kashmir', '12548926', '222236', '57'], ['Uttarakhand', '10116752', '53483', '189'], ['Himachal Pradesh', '6864602', '55673', '123'], ['Tripura', '3671032', '10486', '350'], ['Meghalaya', '2964007', '22429', '132'], ['Manipur', '2721756', '22327', '122'], ['Nagaland', '1980602', '16579', '119'],['Goa', '1457723', '3702', '394'], ['Arunachal Pradesh', '1382611'], ['Mizoram', '1091014', '21081', '52'], ['Sikkim', '607688', '7096', '86']]
        state_code_data=[['SrNo', 'StateName', 'TIN', 'StateCode'], ['1', 'Andaman and Nicobar Islands', '35', 'AN'], ['2', 'Andhra Pradesh', '28', 'AP'], ['3', 'Andhra Pradesh New', '37', 'AD'], ['4', 'Arunachal Pradesh', '12', 'AR'], ['5', 'Assam', '18', 'AS'], ['6', 'Bihar', '10', 'BH'], ['7', 'Chandigarh', '04', 'CH'], ['8', 'Chattisgarh', '22', 'CT'], ['9', 'Dadra and Nagar Haveli', '26', 'DN'], ['10', 'Daman and Diu', '25', 'DD'], ['11', 'Delhi', '07', 'DL'], ['12', 'Goa', '30', 'GA'], ['13', 'Gujarat', '24', 'GJ'], ['14', 'Haryana', '06', 'HR'], ['15', 'Himachal Pradesh', '02', 'HP'], ['16', 'Jammu and Kashmir', '01', 'JK'], ['17', 'Jharkhand', '20', 'JH'], ['18', 'Karnataka', '29', 'KA'], ['19', 'Kerala', '32', 'KL'], ['20', 'Lakshadweep Islands', '31', 'LD'], ['21', 'Madhya Pradesh', '23', 'MP'], ['22', 'Maharashtra', '27', 'MH'], ['23', 'Manipur', '14', 'MN'], ['24', 'Meghalaya', '17', 'ME'], ['25', 'Mizoram', '15', 'MI'], ['26', 'Nagaland', '13', 'NL'], ['27', 'Odisha', '21', 'OR'], ['28', 'Pondicherry', '34', 'PY'], ['29', 'Punjab', '03', 'PB'], ['30', 'Rajasthan', '08', 'RJ'], ['31', 'Sikkim', '11', 'SK'], ['32', 'Tamil Nadu', '33', 'TN'], ['33', 'Telangana', '36', 'TS'], ['34', 'Tripura', '16', 'TR'], ['35', 'Uttar Pradesh', '09', 'UP'], ['36', 'Uttarakhand', '05', 'UT'], ['37', 'West Bengal', '19', 'WB']]
        assert self.obj1.check_read_csv()== state_data
        assert self.obj2.check_read_csv()==state_code_data

    def test_open_csv_errors(self):
        self.obj1=CensusAnalyser.CsvManipulsation(list("../data/StateCensusData.csv"))
        self.obj2=CensusAnalyser.CsvManipulsation("../data/StateCode.txt")
        self.obj3=CensusAnalyser.CsvManipulsation(list("../data/StateCensusData.csv"))
        self.obj4=CensusAnalyser.CsvManipulsation("../data/StateCensusData.txt")
        with pytest.raises(CensusAnalyser.NotStringError):
            self.obj1.check_read_csv()
        with pytest.raises(CensusAnalyser.NotStringError):
            self.obj3.check_read_csv()
        with pytest.raises(CensusAnalyser.NotCsvError):
            self.obj2.check_read_csv()
        with pytest.raises(CensusAnalyser.NotCsvError):
            self.obj4.check_read_csv()

    def test_count(self,obj):
        self.obj1.check_read_csv()
        self.obj2.check_read_csv()
        assert self.obj1.count_rows()==29
        assert self.obj2.count_rows()==37

    def test_header(self,obj):
        self.obj1.check_read_csv()
        self.obj2.check_read_csv()
        assert self.obj1.header_check(['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm'])=="Headers match"
        assert self.obj2.header_check(['SrNo', 'StateName', 'TIN', 'StateCode'])=="Headers match"

    def test_header_errors(self,obj):
        self.obj1.check_read_csv()
        self.obj2.check_read_csv()
        with pytest.raises(CensusAnalyser.HeadersNotListError):
            self.obj1.header_check(('State', 'Population', 'AreaInSqKm', 'DensityPerSqKm'))
        with pytest.raises(CensusAnalyser.HeadersNotListError):
            self.obj2.header_check(('SrNo', 'StateName', 'TIN', 'StateCode'))
        with pytest.raises(CensusAnalyser.HeadersNotStringsError):
            self.obj1.header_check([1, 'Population', 'AreaInSqKm', 'DensityPerSqKm'])
        with pytest.raises(CensusAnalyser.HeadersNotStringsError):
            self.obj2.header_check([1, 'StateName', 'TIN', 'StateCode'])

    def test_dict_convert(self,obj):
        dict_data={'Andaman and Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 'Andhra Pradesh New': 'AD', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BH', 'Chandigarh': 'CH', 'Chattisgarh': 'CT', 'Dadra and Nagar Haveli': 'DN', 'Daman and Diu': 'DD', 'Delhi': 'DL', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP', 'Jammu and Kashmir': 'JK', 'Jharkhand': 'JH', 'Karnataka': 'KA', 'Kerala': 'KL', 'Lakshadweep Islands': 'LD', 'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ME', 'Mizoram': 'MI', 'Nagaland': 'NL', 'Odisha': 'OR', 'Pondicherry': 'PY', 'Punjab': 'PB', 'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TS', 'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UT', 'West Bengal': 'WB'}
        with pytest.raises(CensusAnalyser.FileNotReadedError):
            self.obj2.dict_convert()
        self.obj2.check_read_csv()
        assert self.obj2.dict_convert()==dict_data
    
    def test_new_csv(self,obj):
        census_data=[['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm'],["Sikki", "607688", "7096", "86"]]
        self.obj2.check_read_csv()
        self.obj2.dict_convert()
        assert self.obj2.new_csv(census_data)==[['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm', 'StateCode'], ["Sikki", "607688", "7096", "86", "None"]]