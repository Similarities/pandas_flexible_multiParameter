__author__ = 'julia'

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

    def band_pass(self):

        #& self.selection[self.param1] > self.condition2 & self.selection[self.param1] > self.condition2


        self.selection = self.selection[self.selection[self.param1] >= self.condition1]
        self.selection = self.selection[self.selection[self.param1] < self.condition2]

        self.name = self.name + ' >=' + str(self.condition1) + ' <' + str(self.condition2)
        self.name_subselection = self.name
        #print(self.selection[[self.param1]], 'please check', self.name)
        print(len(self.selection))
        return self.selection
    
    
    
    def reset_subselection(self):
        
        self.sub_selection = []
        print(self.sub_selection)
        self.name_subselection = self.name
        return self.sub_selection
        
        
        
    def bandpass_split_for_second_parameter(self, param2,p2_condition1, p2_condition2, param_sort): 
        
        self.reset_subselection()
        
        self.sub_selection = self.selection.copy()
        
        print(param2, p2_condition1,p2_condition2)
        
       # if self.sub_selection[self.sub_selection[param2]].isnull:
            
            

        
        self.sub_selection = self.sub_selection[self.sub_selection[param2] >= p2_condition1]
        self.sub_selection = self.sub_selection[self.sub_selection[param2] < p2_condition2]
        self.name_subselection = self.name_subselection +' + '+ str(param2) + '>=' + str(p2_condition1) + '<' + str(p2_condition2)
        #print(self.name_subselection)
        
        #print(self.sub_selection[[self.param1, param2, param_sort]])
        
        return self.sub_selection, len(self.sub_selection)
    
    



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
    



my_sorted_data = discriminate_parameters(RESULT, "PP in out", "out")
my_sorted_data.black_white_discrimination()
PP_out = my_sorted_data.return_df()

#El via decorator...

my_sorted_data2 = discriminate_parameters(PP_out, "EL on target", 1.1)
my_sorted_data2.high_pass()
high_EL = my_sorted_data2.return_df()
#print(high_EL)


# first parameter >= , second parameter <

GVD_neg = bandpass_selection(high_EL, "GVD in fs^2", -2000, -200)
GVDneg = GVD_neg.band_pass()
GVDneg_zneg, len1 = GVD_neg.bandpass_split_for_second_parameter('z um', -2000,-400, 'Nmax')

test_number_GVDneg = test_overall_numbers(len(GVDneg))


GVDneg_z0, len2 = GVD_neg.bandpass_split_for_second_parameter('z um', -400, 400, 'Nmax')


GVDneg_z1500, len3 = GVD_neg.bandpass_split_for_second_parameter('z um', 400, 1500, 'Nmax')

GVDneg_z2500, len3 = GVD_neg.bandpass_split_for_second_parameter('z um', 1500, 3500, 'Nmax')


print(calc_ratio(GVDneg_zneg, 'Nmax', 21), 'GVDneg_zneg')
print(calc_ratio(GVDneg_z0, 'Nmax', 21), 'GVDneg_z0')
print(calc_ratio(GVDneg_z1500, 'Nmax', 21), 'GVDneg_z1500')
print(calc_ratio(GVDneg_z2500, 'Nmax', 21), 'GVDneg_z2500')

print(calc_ratio(GVD0_zneg, 'Nmax', 24), 'GVD0_zneg')
print(calc_ratio(GVD0_z0, 'Nmax', 24), 'GVD0_z0')
print(calc_ratio(GVD0_z1500, 'Nmax', 24), 'GVD0_z1500')
print(calc_ratio(GVD0_z2500, 'Nmax', 24), 'GVD0_z2500')


GVD_0 = bandpass_selection(high_EL, "GVD in fs^2", -200, 400)
GVD0 = GVD_0.band_pass()
GVD0_zneg, len1 = GVD_0.bandpass_split_for_second_parameter('z um', -2000, -400, 'Nmax')
GVD0_z0, len2 = GVD_0.bandpass_split_for_second_parameter('z um', -400, 400, 'Nmax')
GVD0_z1500, len3 = GVD_0.bandpass_split_for_second_parameter('z um', 400, 1500, 'Nmax')
GVD0_z2500, len4 = GVD_0.bandpass_split_for_second_parameter('z um', 1500, 3500, 'Nmax')

print(calc_ratio(GVD0_zneg, 'Nmax', 21), 'GVD0_zneg')
print(calc_ratio(GVD0_z0, 'Nmax', 21), 'GVD0_z0')
print(calc_ratio(GVD0_z1500, 'Nmax', 21), 'GVD0_z1500')
print(calc_ratio(GVD0_z2500, 'Nmax', 21), 'GVD0_z2500')

print(calc_ratio(GVD0_zneg, 'Nmax', 24), 'GVD0_zneg')
print(calc_ratio(GVD0_z0, 'Nmax', 24), 'GVD0_z0')
print(calc_ratio(GVD0_z1500, 'Nmax', 24), 'GVD0_z1500')
print(calc_ratio(GVD0_z2500, 'Nmax', 24), 'GVD0_z2500')


GVD_600 = bandpass_selection(high_EL, 'GVD in fs^2', 400, 700)
GVD600 = GVD_600.band_pass()
GVD60O_zneg, len1 = GVD_600.bandpass_split_for_second_parameter('z um', -2000, -400, 'Nmax')
GVD600_z0, len2 = GVD_600.bandpass_split_for_second_parameter('z um', -400, 1500, 'Nmax')
GVD600_z1500, len2 = GVD_600.bandpass_split_for_second_parameter('z um', 1500, 2500, 'Nmax')
GVD600_z2500, len2 = GVD_600.bandpass_split_for_second_parameter('z um', 2500, 3500, 'Nmax')


print(calc_ratio(GVD60O_zneg, 'Nmax', 21), 'GVD600_zneg')
print(calc_ratio(GVD600_z0, 'Nmax', 21), 'GVD600_z0')
print(calc_ratio(GVD600_z1500, 'Nmax', 21), 'GVD600_z1500')
print(calc_ratio(GVD600_z2500, 'Nmax', 21), 'GVD600_z2500')

print(calc_ratio(GVD60O_zneg, 'Nmax', 24), 'GVD600_zneg')
print(calc_ratio(GVD600_z0, 'Nmax', 24), 'GVD600_z0')
print(calc_ratio(GVD600_z1500, 'Nmax', 24), 'GVD600_z1500')
print(calc_ratio(GVD600_z2500, 'Nmax', 24), 'GVD600_z2500')


GVD_900 = bandpass_selection(high_EL, 'GVD in fs^2', 700, 1200)
GVD900 = GVD_900.band_pass()
GVD90O_zneg, len1 = GVD_900.bandpass_split_for_second_parameter('z um', -2000, -400, 'Nmax')
GVD900_z0, len2 = GVD_900.bandpass_split_for_second_parameter('z um', -400, 1500, 'Nmax')
GVD900_z1500, len2 = GVD_900.bandpass_split_for_second_parameter('z um', 1500, 2500, 'Nmax')
GVD900_z2500, len2 = GVD_900.bandpass_split_for_second_parameter('z um', 2500, 3500, 'Nmax')

print(calc_ratio(GVD90O_zneg, 'Nmax', 21), 'GVD900_zneg')
print(calc_ratio(GVD900_z0, 'Nmax', 21), 'GVD900_z0')
print(calc_ratio(GVD900_z1500, 'Nmax', 21), 'GVD900_z1500')
print(calc_ratio(GVD900_z2500, 'Nmax', 21), 'GVD900_z2500')
print(calc_ratio(GVD90O_zneg, 'Nmax', 24), 'GVD900_zneg')
print(calc_ratio(GVD900_z0, 'Nmax', 24), 'GVD900_z0')
print(calc_ratio(GVD900_z1500, 'Nmax', 24), 'GVD900_z1500')
print(calc_ratio(GVD900_z2500, 'Nmax', 24), 'GVD900_z2500')



#test_number = test_overall_numbers(len(high_EL))
#test_number.add_2(len(GVDneg))
#test_number.add_2(len(GVD0))
#test_number.add_2(len(GVD600))
#test_number.add_2(len(GVD900))






