# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:42:26 2020

@author: Daisy
"""

## setting working directory
import os
os.chdir(r"C:\Users\Daisy\Downloads\GT Coursework\Spring Semester 2020\ISyE6416 Regression Analysis\Final Project\Data")

## import the file
import pandas as pd
data_2_final = pd.read_csv("us_101_lane2.csv", header = 0)



###--- Step1:Select the vehicle with the highest frequency as the center vehicle in a platoon 
###--- Step1:construct records for veh 472 first (frame range from 1081 to 3183)
  
### select a short data frame with only vehicle id 472 (highest frequency)
## extract all records for vehicle id 472
data_2_472 = data_2_final[data_2_final["Vehicle_ID"] == 472]
# make sure no row is duplicated
notunique_frame_bool_472 = data_2_472["Frame_ID"].duplicated(keep = 'first')
data_2_472_foruse = data_2_472[~notunique_frame_bool_472]

## extract vehicle id 472's vehicle velocity and it's last-frame preceding vehicle params
# extract all vehicle params if the subject's following vehicle is 472 as the input variables
data_following_472 = data_2_final[data_2_final["Following"] == 472]
# make sure no row is duplicated
notunique_frame_bool_following_472 = data_following_472["Frame_ID"].duplicated(keep = 'first')
data_following_472_foruse = data_following_472[~notunique_frame_bool_following_472]

# create input and output dataframes
following_472_input = data_following_472_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_472_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_472_input_indexed = following_472_input.reset_index(drop = True) 
following_472_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])

# extract next_frame vehicle 472 v_Vel as the output variable
for i in range(len(following_472_input)):
    frame_id_current = following_472_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_472_next = data_2_472_foruse[data_2_472_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_472_foruse.loc[index_472_next,"v_Vel"]
    following_472_output = following_472_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True)      
                                                 
# merge input and output variables for vehicle id 472
following_472_total = pd.concat([following_472_input_indexed, following_472_output], axis = 1)
following_472_total["v_ID"] = 472

#---------------------------------------------------------------------------------------------


###--- Step2: Select the vehicle preceding vehicle 472 within the frame range
## deal with three vehicles preceding veh 472 first: veh 456 (frame 1081 to 1416)/ veh 457 (frame 1417 to 1539)/ veh 468 (frame 2092 to 2061)
## veh 456 (frame 1081 to 1416)
data_2_456 = data_2_final[data_2_final["Vehicle_ID"] == 456]
notunique_frame_bool_456 = data_2_456["Frame_ID"].duplicated(keep = 'first')
data_2_456_foruse = data_2_456[~notunique_frame_bool_456] # frame range from 1059 to 2556
data_following_456 = data_2_final[data_2_final["Following"] == 456]
notunique_frame_bool_following_456 = data_following_456["Frame_ID"].duplicated(keep = 'first')
data_following_456_foruse = data_following_456[~notunique_frame_bool_following_456]
# create input and output dataframes
following_456_input = data_following_456_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_456_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_456_input_indexed = following_456_input.reset_index(drop = True) 
following_456_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])
# extract next_frame vehicle 456 v_Vel as the output variable
for i in range(len(following_456_input)):
    frame_id_current = following_456_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_456_next = data_2_456_foruse[data_2_456_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_456_foruse.loc[index_456_next,"v_Vel"]
    following_456_output = following_456_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True) 
# merge input and output variables for vehicle id 472
following_456_total = pd.concat([following_456_input_indexed, following_456_output], axis = 1)
following_456_total["v_ID"] = 456
following_456_foruse = following_456_total[following_456_total["v_Frame_output"].isin(list(range(1081,1417)))]

## veh 457 (frame 1417 to 1539)
data_2_457 = data_2_final[data_2_final["Vehicle_ID"] == 457]
notunique_frame_bool_457 = data_2_457["Frame_ID"].duplicated(keep = 'first')
data_2_457_foruse = data_2_457[~notunique_frame_bool_457] # frame range from 1059 to 2556
data_following_457 = data_2_final[data_2_final["Following"] == 457]
notunique_frame_bool_following_457 = data_following_457["Frame_ID"].duplicated(keep = 'first')
data_following_457_foruse = data_following_457[~notunique_frame_bool_following_457]
# create input and output dataframes
following_457_input = data_following_457_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_457_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_457_input_indexed = following_457_input.reset_index(drop = True) 
following_457_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])
# extract next_frame vehicle 457 v_Vel as the output variable
for i in range(len(following_457_input)):
    frame_id_current = following_457_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_457_next = data_2_457_foruse[data_2_457_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_457_foruse.loc[index_457_next,"v_Vel"]
    following_457_output = following_457_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True) 
# merge input and output variables for vehicle id 472
following_457_total = pd.concat([following_457_input_indexed, following_457_output], axis = 1)
following_457_total["v_ID"] = 457
following_457_foruse = following_457_total[following_457_total["v_Frame_output"].isin(list(range(1417,1540)))]

## veh 468 (frame 2092 to 3061)
data_2_468 = data_2_final[data_2_final["Vehicle_ID"] == 468]
notunique_frame_bool_468 = data_2_468["Frame_ID"].duplicated(keep = 'first')
data_2_468_foruse = data_2_468[~notunique_frame_bool_468] # frame range from 2092 to 3061
data_following_468 = data_2_final[data_2_final["Following"] == 468]
notunique_frame_bool_following_468 = data_following_468["Frame_ID"].duplicated(keep = 'first')
data_following_468_foruse = data_following_468[~notunique_frame_bool_following_468]
# create input and output dataframes
following_468_input = data_following_468_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_468_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_468_input_indexed = following_468_input.reset_index(drop = True) 
following_468_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])
# extract next_frame vehicle 468 v_Vel as the output variable
for i in range(len(following_468_input)):
    frame_id_current = following_468_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_468_next = data_2_468_foruse[data_2_468_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_468_foruse.loc[index_468_next,"v_Vel"]
    following_468_output = following_468_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True) 
# merge input and output variables for vehicle id 472
following_468_total = pd.concat([following_468_input_indexed, following_468_output], axis = 1)
following_468_total["v_ID"] = 468
following_468_foruse = following_468_total[following_468_total["v_Frame_output"].isin(list(range(2092,3062)))]


#-----------------------------------------------------------------------------------------------
###--- Step3: Select the vehicle following vehicle 472 within the frame range
data_preceding_472 = data_2_final[data_2_final["Preceding"] == 472]
notunique_frame_bool_preceding_472 = data_preceding_472["Frame_ID"].duplicated(keep = 'first')
data_preceding_472_foruse = data_preceding_472[~notunique_frame_bool_preceding_472]

## veh 477 (frame 1104 to 1565)
data_2_477 = data_2_final[data_2_final["Vehicle_ID"] == 477]
notunique_frame_bool_477 = data_2_477["Frame_ID"].duplicated(keep = 'first')
data_2_477_foruse = data_2_477[~notunique_frame_bool_477] # frame range from 2092 to 3061
data_following_477 = data_2_final[data_2_final["Following"] == 477]
notunique_frame_bool_following_477 = data_following_477["Frame_ID"].duplicated(keep = 'first')
data_following_477_foruse = data_following_477[~notunique_frame_bool_following_477]
# create input and output dataframes
following_477_input = data_following_477_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_477_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_477_input_indexed = following_477_input.reset_index(drop = True) 
following_477_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])
# extract next_frame vehicle 477 v_Vel as the output variable
for i in range(len(following_477_input)):
    frame_id_current = following_477_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_477_next = data_2_477_foruse[data_2_477_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_477_foruse.loc[index_477_next,"v_Vel"]
    following_477_output = following_477_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True) 
# merge input and output variables for vehicle id 472
following_477_total = pd.concat([following_477_input_indexed, following_477_output], axis = 1)
following_477_total["v_ID"] = 477
following_477_foruse = following_477_total[following_477_total["v_Frame_output"].isin(list(range(1104,1566)))]

## veh 475 (frame 2108 to 3183)
data_2_475 = data_2_final[data_2_final["Vehicle_ID"] == 475]
notunique_frame_bool_475 = data_2_475["Frame_ID"].duplicated(keep = 'first')
data_2_475_foruse = data_2_475[~notunique_frame_bool_475] # frame range from 2092 to 3061
data_following_475 = data_2_final[data_2_final["Following"] == 475]
notunique_frame_bool_following_475 = data_following_475["Frame_ID"].duplicated(keep = 'first')
data_following_475_foruse = data_following_475[~notunique_frame_bool_following_475]
# create input and output dataframes
following_475_input = data_following_475_foruse[["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]]
following_475_input.columns = ["v_Vel","v_Acc","Space_Headway","Time_Headway","Frame_ID"]
following_475_input_indexed = following_475_input.reset_index(drop = True) 
following_475_output = pd.DataFrame(columns = ["v_Vel_output","v_Frame_output"])
# extract next_frame vehicle 475 v_Vel as the output variable
for i in range(len(following_475_input)):
    frame_id_current = following_475_input["Frame_ID"].iloc[i] # get the current frame
    frame_id_next = frame_id_current + 1 # get the next frame
    index_475_next = data_2_475_foruse[data_2_475_foruse["Frame_ID"] == frame_id_next].index   
    v_Vel_following_next = data_2_475_foruse.loc[index_475_next,"v_Vel"]
    following_475_output = following_475_output.append(pd.DataFrame({"v_Vel_output": v_Vel_following_next, 
                                                                     "v_Frame_output": frame_id_next}),
                                                                    ignore_index = True) 
# merge input and output variables for vehicle id 472
following_475_total = pd.concat([following_475_input_indexed, following_475_output], axis = 1)
following_475_total["v_ID"] = 475
following_475_foruse = following_475_total[following_475_total["v_Frame_output"].isin(list(range(2108,3184)))]


#-----------------------------------------------------------------------------------------------
###--- Step4: Merge all the data for loess modeling
data_final = pd.concat([following_456_foruse, following_457_foruse, following_468_foruse,
                        following_472_total, following_477_foruse, following_475_foruse], 
                       ignore_index = True, axis = 0)

data_final = data_final[["v_ID","v_Frame_output","v_Vel_output","Frame_ID","v_Vel","v_Acc","Space_Headway","Time_Headway"]]

data_final_foruse = data_final.sort_values("v_Frame_output")
data_final_foruse = data_final_foruse.reset_index(drop = True)
data_final_foruse.to_csv("us_101_lane2_foruse.csv", index = False)
data_final_test = data_final_foruse.iloc[0:1358]
data_final_train = data_final_foruse.iloc[1358:]

