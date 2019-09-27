# pandas_flexible_multiParameter


This is good excercise for the question code design and patterns:

We start with a mixed dataframe consisting of very different parameters. 
We want to discriminate the data in different ways:

° sort the dataframe for unnamed columns

° skip some of the columns 

° keep a lot of the other columns 

° generally filter for one parameter (like 'in' or 'out'), called the 'black and white' selection

° generally filter for one parameter as a bandpass (>/< threshold), 'bandpass' selection

° filter for ranges (from ... to) in one of the parameters, while watching the results of a second parameter
(similar for x in range bla to bla, select y)

° we want to have the parameters and ranges to be accessed dynamic (sorting vice versa, or for different ones)

° we want to keep some the filters as an object, in order to apply different further filterings or calculations on it, without
changing it (count,  ratio for x in range bla ), 

° we want to plot different ranges of one parameter with different colors
in x,y plot wehere x,y are then next parameters. This would be than a 3 parameter-range-filtering-plot.


for the flexible approach: pandas_subdataframes.py

Now the ULM would look pretty bad I guess, the dataframe is splitted into subframes, which then applies range sortings for 
external named parameter and ranges, which in real partly splits the splitted subframe again in many sub_sub_frames. 
At the moment in version 'pandas_subdataframes.py', the last step of sub_splitting is only executed locally, since it then is folded together
with the last step of an calculation, like 'count', 'calc_ratio'. 
This approach, would maybe make it easy to access different two parmeter range filterings with a batchlist, that 
just calls the different parameters and ranges. 
BUT. Could we do this simpler with a decorator function?
BUT. isnt it better if the class is keeping all the sub_sub_frames, or is splitting in different ranges into 
more than one subframe at the same time? (this would imply a generator of sub_dataframes in a class, to keep the
number of splittings dynamic...)


########### so far an open question, what is the best choice ######### happy for any advice ! ;) #########

In contrast to the approach above, the fixed appraoch:
'Search_mean_sorted_flexible2.py'  is the class-orientated design. Which puts everything into one class and 
executes particular defined sortings and functions inside the class. 
This works quite well for some purpose, but remains highly undynamic and unflexible. 
Although, already some of the functions (calc_mean_of_something) are coded for dynamic variables, but others
especially the range filtering separation is not.

