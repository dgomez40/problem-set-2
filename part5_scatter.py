'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 

def scatter_prediction_felony_vs_nonfelony(pred_universe):
    sns.lmpplot(
        data=pred_universe,
        x='prediction_felony',
        y='prediction_nonfelony',
        hue='has_felony_charge',
        fit_reg=False
    )
    plt.savefig('./data/part5_plots/scatter_prediction_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.clf()


# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

def oberservation():
    print("What can you say about the group of dots on the right side of the plot?")
    print('these are individuals with high felony predictions')


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
def scatter_prediction_felony_vs_nonfelony(pred_universe):
    sns.lmplot(
        data=pred_universe,
        x='prediction_felony',
        y='y_felony',
        fit_reg=False
    )
    plt.savefig('./data/part5_plots/scatter_calibration_prediction_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.clf()


# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

def observation2():
    print('if the model is calibrated or not?')
    print('Due to the scatter plots being polar-opposites, I dont think the model is calibrated properly.')



