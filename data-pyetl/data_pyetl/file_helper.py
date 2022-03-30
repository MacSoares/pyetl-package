from datetime import datetime
import numpy as np
import pandas as pd


class FileHelper:

    def __init__(self, filepath, filetype):
        if type(filepath) is not str:
            raise Exception("Filepath must be a string")
        else:
            self.filepath = filepath
        if type(filetype) is not str:
            raise Exception("Filetype must be a string")
        else:
            self.filetype = filetype

    def read_xls_to_dataframe(self):
        """
        Read xls type spreadsheet file
        """
        try:
            read_types = {
                "xls": pd.read_excel(self.filepath),
                "xlsx": pd.read_excel(self.filepath),
                "ods": pd.read_excel(self.filepath),
            }
            df = read_types.get(self.filetype, Exception())
            return df
        except Exception as e:
            return e

    def read_csv_to_dataframe(self, separators=","):
        """
        Read csv spreadsheet file
        """
        try:
            df = pd.read_csv(self.filepath, sep=separators)
            return df
        except Exception as e:
            return e

    def read_json_to_dataframe(self):
        """
        Read json file
        """
        try:
            df = pd.read_json(self.filepath)
            return df
        except Exception as e:
            return e

    def read_xml_to_dataframe(self):
        """
        Read xml file
        """
        try:
            df = pd.read_xml(self.filepath)
            return df
        except Exception as e:
            return e
