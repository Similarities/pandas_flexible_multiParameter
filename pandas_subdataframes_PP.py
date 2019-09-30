__author__ = 'similarities'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


original_df = pd.read_excel('fundamentalshifts10_selection.xlsx')

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






    def switch_param_and_condition(self, name, condition_new):

        self.param_1 = name
        self.condition_1 = condition_new

        return self.param_1, self.condition_1


    def return_df(self):
        return self.selection



    def black_white_discrimination(self):

        self.selection = self.selection[self.selection[self.param_1] == -1]

        self.test_empty()


    def black_white_discrimination_exclusion(self):


        #print(self.selection)


        self.selection = self.selection[self.selection[self.param_1] != self.condition_1]

        return self.selection





    def test_empty(self):

        if self.selection is []:

            raise ValueError("No match for the condition")


        else:

            #print(self.selection[[self.param_1]])
            self.selection= drop_columns(self.selection, self.param_1)




    def high_pass(self):


        self.selection = self.selection[self.selection[self.param_1] >= self.condition_1]

        #print(self.selection[[self.param_1]], "into HP")




    def low_pass(self):


        self.selection = self.selection[self.selection[self.param_1] < self.condition_1]

        #print(self.selection[[self.param_1]], "low pass <", self.condition_1)






    def no_entry(self):

        self.drop_nan()

        self.selection[self.param_1].replace("out", 0)
        #does only find the last entry ... check for leerstellen, oder ob str ersetzt werden kann.
        pd.to_numeric(self.selection[self.param_1], errors='coerce')
        print("after clenaning...")
        print( self.selection[self.param_1], len(self.selection))
        return self.selection


    def drop_nan(self):

        print("before", len(self.selection))

        self.selection.dropna( subset = [self.param_1], inplace=True)
        print("after:", len(self.selection))




    def fill_nan_with_zero(self):

        self.selection = self.selection[[self.param_1]].fillna(0)
        print("replace in column", self.param_1, "all nan with 0 ", self.selection[self.param_1])
        return self.selection



#self.copy = self.copy.replace(np.nan, True, regex=True)



class bandpass_selection:

    def __init__(self, dataframe, param_1,condition1, condition2):

        self.dataframe = dataframe
        self.param1 = param_1
        self.name = str(param_1)
        self.name_subselection = self.name
        self.condition1 = condition1
        self.condition2 = condition2
        print( self.name, "column to be sorted")
        self.selection = self.dataframe.copy()
        self.sub_selection = []


        testfunction_columnname(self.selection, self.param1)




    def switch_parameter_and_conditions(self, parameter_new, condition_1_new, condition_2_new):
        self.param1 = parameter_new
        self.condition1 = condition_1_new
        self.condition2 = condition_2_new


        return self.param1, self.condition2, self.condition1, self.selection




    def band_pass_1(self):


        #print(self.selection[[self.param1]])

        self.selection = self.selection[self.selection[self.param1] >= self.condition1]
        self.selection = self.selection[self.selection[self.param1] < self.condition2]


        #print(self.selection[[self.param1]], 'please check', self.name)
        #print(len(self.selection))

        return self.selection



    def keep_this_selection(self, bool):

        if bool is True:

            self.sub_selection = []

            self.sub_selection = self.selection

            self.name_subselection = self.name +str(self.param1)+"_"+str(self.condition1)+"_"+str(self.condition2)
            print(self.name_subselection)

            return self.sub_selection


        else:

            None



    def re_use_selection(self):

        print(self.name_subselection, "conditions of reused subselection")

        self.selection = []
        self.selection = self.sub_selection

        return self.selection

    
    
    def reset_subselection(self):
        
        self.sub_selection = []

        return self.sub_selection



    def reset_dataframe(self):
        self.selection = []

        self.selection = self.dataframe.copy()

        self.name = "initial_"

        print("selection is reset to input frame")

        return self.selection




    def return_this_selection(self):

        return self.selection
        
        
        



def testfunction_columnname(dataframe, columname):

    labelset = get_label_names(dataframe)


    if columname in labelset:
        #print("name passed")

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
    
    
    
    
    

class test_overall_numbers:
    
    def __init__(self, add ):

        self.add = add

        
        
    def add_2(self, number):

        var = True
    
        if self.add != 0 and var==True : 
            self.add = self.add - number
            print('test says remains:', self.add)
            
            if self.add == 0:
                print('! no more entrys left!')
        else: 
            
            print('no more entrys left')
        
        
        return self.add







    
def zero_to_none( auswahl, x_label):

        auswahl = auswahl.replace({x_label: 0.}, np.nan)[[x_label]]

        return auswahl



    
# external function  that asks for a particular purpose
def calc_ratio(dataframe, parameter, condition):
    

    print('xxxxx', parameter, '>', condition)
    
    dataframe = zero_to_none(dataframe, parameter)
    
    
    number_All = dataframe.count()[parameter]
    
    if number_All != 0:

        dataframe = dataframe[dataframe[parameter] > condition][[parameter]]
        
        #print(dataframe[[parameter]])
        part = dataframe.count()[parameter]
    
        ratio = part/ number_All
    
        return ratio, number_All
    
    else:
        return 0



# specific defined batch list that  uses object form bandpass_selected class
# with recycling subframing and resets
def batch_one_paremeter_range_for_object(liste):

    for i in range(len(liste)-1):

        bandpass.switch_parameter_and_conditions('z um', liste[i], liste[i+1])
        x = bandpass.band_pass_1()
        print("-----------", "z in um from:", liste[i], 'to  <', liste[i+1])
        print(calc_ratio(x, 'Nmax', 21))
        print(calc_ratio(x, 'Nmax', 27))

        # skips the last selection in order to see the other values again.
        bandpass.re_use_selection()




list_GVD = [-1000, -300, 400, 900, 1500]
list_z = [-2000, -400, 400, 1500, 3500]



my_sorted_data = discriminate_parameters(RESULT, "PP in out", 7.9)



#my_sorted_data.black_white_discrimination_exclusion()

my_sorted_data.high_pass()
my_sorted_data.switch_param_and_condition("PP in out", 35)
my_sorted_data.low_pass()
my_sorted_data.switch_param_and_condition("EL on target", 1.2)
my_sorted_data.high_pass()

PP_in = my_sorted_data.return_df()

print(PP_in[ ["EL on target", "PP in out"]])
print(len(PP_in), " selected of:", len(RESULT))






bandpass = bandpass_selection(PP_in, 'GVD in fs^2', -1000, -200)
bandpass.band_pass_1()
bandpass.keep_this_selection(True)
batch_one_paremeter_range_for_object(list_z)
bandpass.reset_dataframe()

bandpass.switch_parameter_and_conditions('GVD in fs^2', -200, 400)
bandpass.band_pass_1()
bandpass.keep_this_selection(True)
batch_one_paremeter_range_for_object(list_z)

bandpass.reset_dataframe()
bandpass.switch_parameter_and_conditions('GVD in fs^2', 400, 900)
bandpass.band_pass_1()
bandpass.keep_this_selection(True)
batch_one_paremeter_range_for_object(list_z)


bandpass.reset_dataframe()
bandpass.switch_parameter_and_conditions('GVD in fs^2', 900, 1500)
bandpass.band_pass_1()
x=bandpass.keep_this_selection(True)
batch_one_paremeter_range_for_object(list_z)

print(x[["Nmax", "day", "GVD in fs^2"]])




