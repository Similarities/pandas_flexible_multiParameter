__author__ = 'similarities'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


original_df = pd.read_excel('fundamentalshifts12_selection_div_new.xlsx')

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
    
    def len_of_dif(self):
        return len(self.copy)
    
    def new_column(self, liste, name):
        if len(liste) == self.len_of_dif():
            self.copy.insert(1,name,liste,True)
            #self.copy[name] = liste
        else:
            print('does not have same dimension')
        return self.copy

    def export_one_column(self, name):
        liste = self.copy[name].tolist()
        return liste
        


mam = Sort_and_Copy_Dataframe(original_df)
mam.drop_unnamed_columns()
mam.drop_columns(["z steps", 'Comment 1', "EL (corrected)", "comment2", "GVD", "2w center", 'HHG_E in uJ full range'])
mam.get_label_names()
RESULT = mam.get_new_df()


class discriminate_parameters:
    def __init__(self, dataframe, param_1, condition_1):
        self.dataframe = dataframe
        self.param_1 = param_1
        self.condition_1 = condition_1
        self.selection = self.dataframe.copy()
        check_columnname(self.selection, self.param_1)

    def switch_param_and_condition(self, name, condition_new):
        self.param_1 = name
        self.condition_1 = condition_new
        return self.param_1, self.condition_1

    def return_df(self):
        return self.selection

    def black_white_discrimination(self):
        self.selection = self.selection[self.selection[self.param_1] == -1]


    def black_white_discrimination_exclusion(self):
        #print(self.selection)
        self.selection = self.selection[self.selection[self.param_1] != self.condition_1]
        return self.selection

    def empty(self):
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


        check_columnname(self.selection, self.param1)

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


def check_columnname(dataframe, columname):
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

class overall_numbers:
    def __init__(self, add ):
        self.add = add
    def add_2(self, number):
        var = True
        if self.add != 0 and var==True : 
            self.add = self.add - number
            print('remaining:', self.add)
            
            if self.add == 0:
                print('! no more entrys left!')
        else:
            print('no more entrys left')
        return self.add

def stepsize_x_axis( borderL, borderR):
        z_values = list(range(borderL,borderR))
        return  z_values

def mean_of_something_vs_something(auswahl, parameter_x, scale_factor_x, x_label, parameter_sorted, y_label, name):
        #auswahl.sort_values(by=['z um'])
        result_array_z_meanEnergy = np.zeros([1,3])
        #print(result_array_z_meanEnergy)
        #print(auswahl, "reseted")
        for x in range(0, len(parameter_x)):
            criteria = auswahl[x_label] == parameter_x[x]*scale_factor_x

            auswahl2 = auswahl.copy
            auswahl2 = auswahl[criteria][parameter_sorted]
            mean_var = auswahl2.mean(axis = 0, skipna = True)
            std_var = auswahl2.std()
            if np.isnan(mean_var) or mean_var == 0:
                None
            # catches statistics with N<2 and removes
            elif np.isnan(std_var):
               None
            else:
                result_array_z_meanEnergy = np.vstack((result_array_z_meanEnergy, np.array([parameter_x[x]*scale_factor_x, mean_var, std_var])))
                print (result_array_z_meanEnergy)

        #catches empty result array
        if len(result_array_z_meanEnergy) < 1:
            print("nothing to plot for mean in: ", name)
        # returns result array
        else:
            errY = result_array_z_meanEnergy[1::,2]
            return result_array_z_meanEnergy[1::,0],result_array_z_meanEnergy[1::,1], errY




def plot_together_in_one_graph(color, name, x, y, x_label, y_label, errX, errY, marker):
        x1=x
        y1=y
        if len(x1) == 0:
            print("empty dataframe in:", x_label)

        elif len(y1) == 0:
            print("empty dataframe in:", y_label)

        else:
            plt.figure(2)
            plt.errorbar(x1, y,  xerr=errX, yerr=errY, fmt='o', label= name, alpha=0.3, color = color, marker=marker )
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

def zero_to_none(auswahl, x_label):
        auswahl = auswahl.replace({x_label: 0.}, np.nan)[[x_label]]
        return auswahl

    
# calculates rato between all datapoints and a particular selection (>condition)
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
    


def save_picture(picture_name):
        plt.savefig(picture_name+".png",  bbox_inches="tight", dpi = 1000)

list_GVD = [-1000, -300, 400, 900, 1500]
list_z = [-2000, -400, 400, 1500, 3500]


my_sorted_data = discriminate_parameters(RESULT, "PP in out", -1)
my_sorted_data.black_white_discrimination()
#my_sorted_data.switch_param_and_condition('day', 20190117)
#my_sorted_data.black_white_discrimination_exclusion()
E1=1.98
E2=2.52
my_sorted_data.switch_param_and_condition('EL on target', E1)
my_sorted_data.high_pass()
my_sorted_data.switch_param_and_condition('EL on target', E2)
my_sorted_data.low_pass()
# for statistics: here filtered results:
PP_out_energy_range = my_sorted_data.return_df()
print(len(RESULT), "overall shots in campaign")
print(len(PP_out_energy_range), "number of shots with no prepulse and in the selected energy range")

#furter discriminate by cutoff
my_sorted_data.switch_param_and_condition("Nmax", 24)
my_sorted_data.high_pass()
#my_sorted_data.low_pass()

PP_out = my_sorted_data.return_df()
print(len(PP_out), "with N>25 cutoff, PPout and selected Energy range of overall:", len(PP_out_energy_range))

#for checking single entries:
#print(PP_out[ ['div25 gauss', "PP in out", 'Nmax', 'z um', 'day', 'shot']])
#print(len(PP_out), " selected of:", len(RESULT))


bandpass = bandpass_selection(PP_out, 'GVD in fs^2', -300, 400)
bandpass.band_pass_1()
x = bandpass.keep_this_selection(True)

#statistics:
bandpass_all = bandpass_selection(PP_out_energy_range, 'GVD in fs^2', -300, 400)
bandpass_all.band_pass_1()
xprime = bandpass_all.keep_this_selection(True)
print( "number of shots in this range including lower cutoff", len(xprime[["div25 gauss"]]))
print("all shots with Nmax>24", len(x[['div25 gauss']]))
number_to_low_cutoff = len(xprime[["div25 gauss"]])-len(x[['div25 gauss']])

#x-axis for all plots
stepsize_x = stepsize_x_axis( -5000,1000)
errx = 200
erry = 0

# do not count 0 as value
x[['div25 gauss']] = x[['div25 gauss']].replace(0., np.nan)
# correct for driving laser divergence 40mrad
x[['div25 gauss']] = x[['div25 gauss']]/40
#again statistics
print("not evaluable or Nmax<24 in selection:", x[['div25 gauss']].isna().sum())
print("not used shots general ratio:", (x[['div25 gauss']].isna().sum()+ number_to_low_cutoff)/ len(xprime[['div25 gauss']]) )
print("not used shots ratio with Nmax>24:", x[['div25 gauss']].isna().sum()/ len(x[['div25 gauss']]) )



mean_x, mean_y, erry = mean_of_something_vs_something(x, stepsize_x, 1, "z um", "div25 gauss", "[mrad]","GDD -300 - 300 fs^2"  )


plot_together_in_one_graph("c", "GDD -200- 300 fs^2", mean_x, mean_y, "z [um]", 'w25 gauss', errx, erry, "*")

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

bandpass2 = bandpass_selection(PP_out, 'GVD in fs^2', 400, 650)
xx = bandpass2.band_pass_1()

bandpass_all = bandpass_selection(PP_out_energy_range, 'GVD in fs^2', 400, 650)
bandpass_all.band_pass_1()
xprime = bandpass_all.keep_this_selection(True)
print( "number of shots in this range including lower cutoff", len(xprime[["div25 gauss"]]))
print("all shots in this selection, Nmax>24:", len(xx[['div25 gauss']]))
number_to_low_cutoff = len(xprime[["div25 gauss"]])-len(xx[['div25 gauss']])

xx[['div25 gauss']] = xx[['div25 gauss']].replace(0., np.nan)
xx[['div25 gauss']] = xx[['div25 gauss']]/40
print("not evaluable or Nmax<24 in selection:", xx[['div25 gauss']].isna().sum())
print("not used shots general ratio:", (xx[['div25 gauss']].isna().sum()+ number_to_low_cutoff)/ len(xprime[['div25 gauss']]) )
print("not used shots ratio for Nmax>24:", xx[['div25 gauss']].isna().sum()/ len(xx[['div25 gauss']]) )


mean_x, mean_y,  erry = mean_of_something_vs_something(xx, stepsize_x, 1, "z um", "div25 gauss", "[mrad]","GDD 400 - 700 fs^2"  )
plot_together_in_one_graph("r", "GDD 400- 600 fs^2", mean_x, mean_y, "z [um]", 'w25 gauss', errx, erry, "o")

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")


bandpass3 = bandpass_selection(PP_out, 'GVD in fs^2', 700, 1101)
xxx = bandpass3.band_pass_1()
bandpass3.keep_this_selection(True)
bandpass_all = bandpass_selection(PP_out_energy_range, 'GVD in fs^2', 700, 1101)
bandpass_all.band_pass_1()
xprime = bandpass_all.keep_this_selection(True)
print( "number of shots in this range including lower cutoff", len(xprime[["div25 gauss"]]))
print("all shots in this selection, Nmax>24:", len(xxx[['div25 gauss']]))
number_to_low_cutoff = len(xprime[["div25 gauss"]])-len(xxx[['div25 gauss']])

xxx[['div25 gauss']] = xxx[['div25 gauss']].replace(0., np.nan)
xxx[['div25 gauss']] = xxx[['div25 gauss']]/40

print("not evaluable or Nmax<24 in selection:", xxx[['div25 gauss']].isna().sum())
print("all shots in this selection:", len( xxx[['div25 gauss']]))
print("not used shots general ratio:", (xxx[['div25 gauss']].isna().sum()+ number_to_low_cutoff)/ len(xprime[['div25 gauss']]) )
print("not used shots ratio:", xxx[['div25 gauss']].isna().sum()/ len(xxx[['div25 gauss']]) )

mean_x, mean_y, erry = mean_of_something_vs_something(xxx, stepsize_x, 1, "z um", "div25 gauss", "[mrad]","GDD 800 - 1200 fs^2"  )
plot_together_in_one_graph("black", "GDD 700 - 1100 fs^2", mean_x, mean_y, "z [um]", 'w25 gauss/Theta_L [mrad]', errx, erry, "P")






#plt.xscale('log')
plt.xlim(-4200,100)
plt.title(str(np.round(E1*0.7,1))+ "-"+ str(np.round(E2*0.7,1))+" J on target")
#plt.ylim(0.5, 20)
save_picture('div25_gauss_EL2-2.5_marker')
plt.show()









