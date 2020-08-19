# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:57:10 2020

@author: Daisy
"""

## setting working directory
import os
os.chdir(r"C:\Users\Daisy\Downloads\GT Coursework\Spring Semester 2020\ISyE6416 Regression Analysis\Final Project\Data")

## import the file
import pandas as pd
data = pd.read_csv("us-101.csv", header = 0)
## drop unneceessary columns
data = data.drop(["O_Zone","D_Zone","Section_ID","Location"], axis = 1)
data = data.drop(["Movement"], axis = 1)
data = data.drop(["Int_ID"], axis = 1)
data = data.drop(["Total_Frames"], axis = 1)
data = data.drop(["Direction"], axis = 1)
## choose vehicle class is auto
data = data[data["v_Class"] == 2]
## separate by lane id
data_2 = data[data["Lane_ID"] == 2]
data_3 = data[data["Lane_ID"] == 3]
data_4 = data[data["Lane_ID"] == 4]
# use data_2 as the training set
data_2 = data_2.drop(["Global_X","Global_Y","Local_X","Local_Y"], axis = 1)
data_2 = data_2.drop(["v_Width","v_length","v_Class"], axis = 1)
data_2 = data_2.sort_values(by = ["Global_Time"])
## select only records with same time 
### based on global_time
notunique_time_bool = data_2["Global_Time"].duplicated(keep = False)
data_2_timeforuse = data_2[notunique_time_bool]
### based on frame_id
notunique_frame_bool = data_2["Frame_ID"].duplicated(keep = False)
data_2_frameforuse = data_2[notunique_frame_bool]
### verified to be the same
data_2_final = data_2_timeforuse
data_2_final = data_2_final.drop(["Lane_ID"], axis = 1)
data_2_final = data_2_final.drop(["Global_Time"], axis = 1)
## rearrange the dataframe
data_2_final = data_2_final[["Frame_ID","Vehicle_ID","Preceding","Following",
                            "v_Vel","v_Acc","Space_Headway","Time_Headway"]]
data_2_final.to_csv("us_101_lane2.csv", index = False)

###--- Method 1: select the highest frequency to build the model   
### select a short data frame with only vehicle id 472 (highest frequency)
# vehicle id is 472 
data_2_short_1 = data_2_final[data_2_final["Vehicle_ID"] == 472].index
data_21 = data_2_final[data_2_final.index.isin(data_2_short_1)]
# preceding vehicle id is 472 (the following vehicle of vehicle id 472)
data_2_short_2 = data_2_final[data_2_final["Preceding"] == 472].index
data_22 = data_2_final[data_2_final.index.isin(data_2_short_2)]
# following vehicle id is 472 (the preceding vehicle of vehicle id 472)
data_2_short_3 = data_2_final[data_2_final["Following"] == 472].index
data_23 = data_2_final[data_2_final.index.isin(data_2_short_3)]
## a new data set for use
data_2_short = pd.concat([data_21, data_22, data_23], axis = 0)

## extract all records for vehicle id 472
data_2_472 = data_2_short[data_2_short["Vehicle_ID"] == 472]
# make sure no row is duplicated
notunique_frame_bool_472 = data_2_472["Frame_ID"].duplicated(keep = 'first')
data_2_472_foruse = data_2_472[~notunique_frame_bool_472]

## extract vehicle id 472's vehicle velocity and it's last-frame preceding vehicle params
# extract all vehicle params if the subject's following vehicle is 472 as the input variables
data_following_472 = data_2_short[data_2_short["Following"] == 472]
# make sure no row is duplicated
notunique_frame_bool_following_472 = data_following_472["Frame_ID"].duplicated(keep = 'first')
data_following_472_foruse = data_following_472[~notunique_frame_bool_following_472]
# create input and output dataframes
following_472_input = data_following_472_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_472_input_indexed = following_472_input.reset_index(drop = True) 
#input_output_for_472 = data_following_472[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_472_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])

# extract next_frame vehicle 472 v_Vel as the output variable
for i in range(len(following_472_input)):
    frame_id_current = following_472_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_472 = data_2_472_foruse[data_2_472_foruse["Frame_ID"] == frame_id_next].index
    v_Vel_following_next = data_2_472_foruse.loc[index_472,"v_Vel"]
    following_472_output = following_472_output.append(pd.DataFrame({"v_Vel_output":v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True)      
                                                 
# merge input and output variables for vehicle id 472
following_472_total = pd.concat([following_472_input_indexed, following_472_output], axis = 1)
    
    
