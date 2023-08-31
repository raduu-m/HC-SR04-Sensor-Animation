import numpy as np

def MovingAverage(S1_data_x,S2_data_y,S3_data_x, S4_data_y):

    average_S1=round(np.sum(S1_data_x)/10,1)
    average_S2=round(np.sum(S2_data_y)/10,1)
    average_S3=round(np.sum(S3_data_x)/10,1)
    average_S4=round(np.sum(S4_data_y)/10,1)
      
    x_data = [average_S1, 0,  average_S3,0]
    y_data = [0, average_S1, 0, -1*average_S2]
    
    return x_data,y_data