import pandas
import itertools
from math import inf

class Discretize():

    def __init__(self):
        self.initial_cuts = []
        self.final_cuts = {}
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
        print("Starting transformation")
        self.__generate_cuts()
        self.__transform_df()
        print("Transformation complete")
    
    def __generate_cuts(self):
        """
        This private function/method takes in no parameter.
        The cuts are generated to discretize the table using the discernibilty formulas algorithm.
        """
        print("Generating cuts")
        self.attributes = list(self.df.columns)[:-1]
        self.dec = list(self.df.columns)[-1]

        labels = list(self.df[self.dec].unique())
        indices_to_pair = [ self.df.index[ self.df[self.dec] == label ].tolist() for label in labels ]
        
        pairs = []
        for i in range(len(indices_to_pair)-1):
            for j in range(i+1,len(indices_to_pair)):
                pairs.extend( list( itertools.product( indices_to_pair[i], indices_to_pair[j] ) ) )
        
        cuts = {}
        for index,attri in enumerate(self.attributes):
            val = sorted(list(self.df[attri].unique()))
            for i in range(1,len(val)):
                cut = (val[i-1] + val[i])/2
                self.initial_cuts.append( (index, cut) )
                if index not in cuts:
                    cuts[index] = []
                cuts[index].append(cut)
                
        rows = dict.fromkeys(pairs,set())
        cols = dict.fromkeys(self.initial_cuts,set())

        for pair in pairs:
            x1, x2 = pair
            for index,attri in enumerate(self.attributes):
                for cut in cuts[index]:
                    if self.df.loc[x1, attri] < cut < self.df.loc[x2, attri] or self.df.loc[x2, attri] < cut < self.df.loc[x1, attri] :
                        rows[pair].add( (index, cut) )
                        cols[(index, cut)].add(pair)
        
        while bool(rows):
            counts =[(len(value), key[0], key[1]) for key,value in cols.items()]
            optimal_cut = sorted(counts, key = lambda x: (-x[0],x[1],x[2]))[0][1:]
            discern_rows = cols[optimal_cut]
            for col in cols.keys():
                cols[col].difference_update(discern_rows)
            for row in discern_rows:
                del rows[row]
            if optimal_cut[0] not in self.final_cuts:
                self.final_cuts[ optimal_cut[0] ] = []
            self.final_cuts[ optimal_cut[0] ].append(optimal_cut[1])

    def __transform_df(self):
        """
        This private function/method takes in no parameter.
        The df dataframe is transformed and stored into the trans_df using the final cuts list.
        eg : self.final_cuts = {0: [0.9, 1.5], 1: [0.75, 1.5] } where key is the attribute index and value is list of cuts
        """
        print("Transforming dataframe")

if __name__ == "__main__":
    D = Discretize()
    D.read("data.txt")
    D.transform()
    D.write("discretized_data.csv")