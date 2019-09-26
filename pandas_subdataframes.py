__author__ = 'julia'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab


original_df = pd.read_excel("fundamentalshifts9_selection.xlsx")

class Sort_and_Copy_Dataframe:

    def __init__(self,  database):
        self.orginal = database
        self.copy = self.orginal.copy()
        #self.copy = self.copy.replace(np.nan, True, regex=True)
        self.tricks = []
        self.auswahl = []
        self.label_set = []




    def drop_unnamed_columns(self):

        self.auswahl = self.copy.columns.str.match('Unnamed')
        empty_column_index = [i for i, x in enumerate(self.auswahl) if x]

        for i in range(len(empty_column_index)):

            number = empty_column_index[i]

            delete_column = "Unnamed: " + str(number)

            self.copy.drop(labels = [delete_column], axis = 1, inplace = True)

        return self.copy


    def get_label_names(self):

        self.label_set = set(self.copy.columns)

        #print(label_set, "labels in dfs..")

        #print("number in sort class:", len(self.label_set))

        print("columns in sort class:", self.label_set)

        #return label_set



    #enables external delete column_name access
    def drop_columns(self, trick):

        self.tricks = trick

        self.copy.drop(labels=self.tricks, axis=1, inplace = True)

        self.label_set = set(self.copy.columns)






    def get_new_df(self):

        return self.copy



mam = Sort_and_Copy_Dataframe(original_df)
mam.drop_unnamed_columns()
mam.get_label_names()
mam.drop_columns(["z steps", 'Comment 1', "side peaks", "EL (corrected)", "comment2", "GVD", "CWE central", "2w center", "central2", "divergence", 'category, x,y,z', 'HHG_E in uJ full range', "central"])
mam.get_label_names()
RESULT = mam.get_new_df()



class discriminate_parameters:

    def __init__(self, dataframe, param_1, condition_1):

        self.dataframe = dataframe
        self.param_1 = param_1
        self.condition_1 = condition_1
        self.selection = self.dataframe.copy()


        testfunction_columnname(self.selection, self.param_1)

    def return_df(self):
        return self.selection



    def black_white_discrimination(self):


        #print(self.selection)





        self.selection = self.selection[self.selection[self.param_1] == self.condition_1]

        self.test_empty()



    def test_empty(self):



        if self.selection is []:

            raise ValueError("No match for the condition")





        else:

            #print(self.selection[[self.param_1]])


            self.selection= drop_columns(self.selection, self.param_1)








    def high_pass(self):

        self.selection = self.selection[self.selection[self.param_1] >= self.condition_1]

        self.test_empty()


    def low_pass(self):


        self.selection = self.selection[self.selection[self.param_1] < self.condition_1]

        self.test_empty()






class bandpass_selection:

    def __init__(self, dataframe, param_1, condition_1, condition_2):

        self.dataframe = dataframe

        self.param1 = param_1

        print( self.param1, "column")
        self.condition1 = condition_1
        self.condition2 = condition_2

        self.selection = self.dataframe.copy()


        testfunction_columnname(self.selection, self.param1)

    def band_pass(self):

        #& self.selection[self.param1] > self.condition2 & self.selection[self.param1] > self.condition2


        self.selection = self.selection[self.selection[self.param1] <= self.condition1 ]
        self.selection = self.selection[self.selection[self.param1] >self.condition2]
        print(self.selection[[self.param1]])

        return self.selection
























def testfunction_columnname(dataframe, columname):

    labelset = get_label_names(dataframe)


    if columname in labelset:
        print("name passed")

        return True



    else:
        raise NameError("no match for columnname of the dataframe")




    # acts permanently on input dataframe!
def drop_columns(dataframe, columnname):


    dataframe.drop(labels=columnname, axis=1, inplace = True)

    return dataframe



def get_label_names(dataframe):

        label_set = tuple(set(dataframe.columns))


        #print("number at label def:", len(label_set))

        #print("columns at label def:", label_set)

        return label_set





my_sorted_data = discriminate_parameters(RESULT, "PP in out", "out")
my_sorted_data.black_white_discrimination()
PP_out = my_sorted_data.return_df()

#El via decorator...

my_sorted_data2 = discriminate_parameters(PP_out, "EL on target", 1.7)
my_sorted_data2.high_pass()
high_EL = my_sorted_data2.return_df()
#print(high_EL)




GVD_neg = bandpass_selection(high_EL, "GVD in fs^2", 400, -400)



