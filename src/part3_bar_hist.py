'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def barplot_fta(pred_universe):
    sns.countplot(data=pred_universe, x='fta')
    plt.title('FTA Count')
    plt.savefig('./data/part3_plots/barplot_fta.png', bbox_inches='tight')
    plt.close()

def barplot_fta_by_sex(pred_universe):
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.title('FTA Count by Sex')
    plt.savefig('./data/part3_plots/barplot_fta_by_sex.png', bbox_inches='tight')
    plt.close()

def histogram_age(pred_universe):
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.title('Age at Arrest Histogram')
    plt.savefig('./data/part3_plots/histogram_age.png', bbox_inches='tight')
    plt.close()

def histogram_age_binned(pred_universe):
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.title('Binned Age at Arrest Histogram')
    plt.savefig('./data/part3_plots/histogram_age_binned.png', bbox_inches='tight')
    plt.close()