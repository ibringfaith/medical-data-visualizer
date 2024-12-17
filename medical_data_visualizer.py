import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', sep=',')

# 2
bmi = df['weight']/(df['height']**2)
df['overweight'] = 0 if bmi <=25 else 1

# 3
# Normalize data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.

# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
