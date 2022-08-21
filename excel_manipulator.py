import pandas as pd


class ExcelManipulator:
    def __init__(self, filelocation, column_to_insert_to):
        self._file = pd.read_excel(filelocation)
        self._data = pd.DataFrame(self._file)
        self._data.at[0, column_to_insert_to] = " "
        self._adresses = []
        self._estimates = []
        self.column_to_insert_to = column_to_insert_to

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def adresses(self):
        return self._adresses

    @adresses.setter
    def adresses(self, adresses):
        self._adresses = adresses

    @property
    def estimates(self):
        return self._estimates

    @estimates.setter
    def estimates(self, estimates):
        self._estimates = estimates

    def get_list_of_adresses(self):
        adresses = (self.data["PROPERTY ADDRESS"].to_numpy(str) +
                    self.data[self.column_to_insert_to].to_numpy(na_value=" ") +
                    self.data["PROPERTY CITY"].to_numpy(str) +
                    self.data[self.column_to_insert_to].to_numpy(na_value=" ") +
                    self.data["PROPERTY STATE"].to_numpy(str) +
                    self.data[self.column_to_insert_to].to_numpy(na_value=" ") +
                    self.data["PROPERTY ZIP CODE"].to_numpy(str)
                    ).tolist()
        return adresses

    def export_to_xlsx_file(self):
        self.data[self.column_to_insert_to] = self.estimates
        self.data.to_excel("xlsx_files/output.xlsx")
