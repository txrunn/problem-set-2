'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_felony_charge_df(arrest_events):
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda x: pd.Series({
            'has_felony_charge': (x['charge_degree'] == 'F').any()
        })
    ).reset_index()
    return felony_charge

def merge_felony_with_universe(felony_charge, pred_universe):
    return pred_universe.merge(felony_charge, on='arrest_id')

def plot_felony_prediction_by_charge(df):
    sns.catplot(data=df, x='has_felony_charge', y='prediction_felony', kind='bar')
    plt.savefig('./data/part4_plots/felony_prediction_by_charge.png', bbox_inches='tight')
    plt.close()

def plot_nonfelony_prediction_by_charge(df):
    sns.catplot(data=df, x='has_felony_charge', y='prediction_nonfelony', kind='bar')
    plt.savefig('./data/part4_plots/nonfelony_prediction_by_charge.png', bbox_inches='tight')
    plt.close()
    print("NOTE: Felony charges are often associated with higher perceived risk, which may drive the model's predictions.")

def plot_felony_prediction_by_charge_and_actual(df):
    sns.catplot(data=df, x='has_felony_charge', y='prediction_felony', hue='felony_six_month', kind='bar')
    plt.savefig('./data/part4_plots/felony_prediction_by_charge_and_actual.png', bbox_inches='tight')
    plt.close()
    print("INTERPRETATION: The model may rely heavily on the presence of current felony charges in making predictions, sometimes overestimating risk for those who don't reoffend and underestimating risk for those who do.")