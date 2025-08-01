'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_barplot(pred_universe):
    sns.countplot(data=pred_universe, 
              x='fta')
    plt.title('FTA Counts')
    plt.savefig('./data/part3_plots/fta.png', bbox_inches='tight')
    plt.clf()



# 2. Hue the previous barplot by sex
def fta_barplot_sex(pred_universe):
    sns.countplot(data=pred_universe, 
              x='fta',
              hue='sex')
    plt.title('FTA Counts by sex')
    plt.savefig('./data/part3_plots/fta_by_sex.png', bbox_inches='tight')
    plt.clf()


# 3. Plot a histogram of age_at_arrest
def hist_age_arrest(pred_universe):
    sns.histplot(data=pred_universe, x = 'age_at_arrest')
    plt.title('histogram of age of arrest')
    plt.savefig('./data/part3_plots/hist_age_arrest.png', bbox_inches='tight')
    plt.clf()



# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def hist_age_arrest_with_bins(pred_universe):
    sns.histplot(data=pred_universe, x = 'age_at_arrest', bins=[18, 21, 30, 40, 100])
    plt.title('Age of arrest with bins')
    plt.savefig('./data/part3_plots/hist_age_arrest_with_bins.png', bbox_inches='tight')
    plt.clf()