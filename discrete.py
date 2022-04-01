import pandas
import itertools
from math import inf

class Discretize():

    def __init__(self):
        self.initial_cuts = []
        self.final_cuts = []
        self.df = None
        self.attributes = []
        self.dec = None
        self.trans_df = None
        print("Discretize object instantiated")
    
    def read(self, path):
        """
        This function/method takes in the path of the input data file.
        The input data file must be in CSV format.
        The input data is stored into the "df" member variable as a pandas dataframe object.
        All other member variables are set back to empty list or None value
        """
        print("Reading data from ",path)
    
    def write(self, path):
        """
        This function/method takes in the path of the output data file.
        The transformed dataframe is stored at the given path in CSV format.
        """
        print("Writing data at ",path)

    def transform(self):
        print("Sarting transformation")
        self.__generate_cuts()
        self.__transform_df()
        print("Transformation complete")
    
    def __generate_cuts(self):
        """
        This private function/method takes in no parameter.
        The cuts are generated to discretize the table using the discernibilty formulas algorithm.
        """
        print("Generating cuts")

    
    def __transform_df(self):
        """
        This private function/method takes in no parameter.
        The df dataframe is transformed and stored into the trans_df using the final cuts list.
        """
        print("Transforming dataframe")

if __name__ == "__main__":
    D = Discretize()
    D.read("data.txt")
    D.transform()
    D.write("discretized_data.csv")