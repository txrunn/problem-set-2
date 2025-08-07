'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def scatter_prediction_by_current_charge(df):
    sns.lmplot(data=df, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='has_felony_charge', 
               fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_felony_vs_nonfelony_by_charge.png', bbox_inches='tight')
    plt.close()
    print("NOTE: The group of dots on the right likely represent individuals with very high nonfelony prediction scores. This may signal a subgroup the model considers high risk, regardless of current felony charge status.")

def scatter_prediction_vs_outcome(df):
    sns.stripplot(data=df, x='prediction_felony', y='felony_six_month', jitter=True, alpha=0.3)
    plt.savefig('./data/part5_plots/scatter_prediction_vs_outcome.png', bbox_inches='tight')
    plt.close()
    print("INTERPRETATION: If predicted probabilities are higher for those who were actually rearrested (y=1), then the model is somewhat calibrated. But if predictions are spread across both outcomes, the model may lack calibration.")