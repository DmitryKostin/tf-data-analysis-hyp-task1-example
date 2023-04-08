import pandas as pd
import numpy as np
from scipy import stats as st
import math as mth

chat_id = 944932368

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    alpha = 0.04

    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    p_combined = (x_success + y_success) / (x_cnt + y_cnt)

    difference = p1 - p2

    z_value = difference / mth.sqrt(p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt))

    distr = st.norm(0, 1)

    p_value = (1 - distr.cdf(abs(z_value))) * 2

    if p_value < alpha:
        return True
    else:
        return False
