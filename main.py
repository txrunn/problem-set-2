'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    part3.barplot_fta(pred_universe)
    part3.barplot_fta_by_sex(pred_universe)
    part3.histogram_age(pred_universe)
    part3.histogram_age_binned(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    felony_charge = part4.generate_felony_charge_df(arrest_events)
    merged_df = part4.merge_felony_with_universe(felony_charge, pred_universe)
    part4.plot_felony_prediction_by_charge(merged_df)
    part4.plot_nonfelony_prediction_by_charge(merged_df)
    part4.plot_felony_prediction_by_charge_and_actual(merged_df)

    ##  PART 5: SCATTERPLOTS  ##
    part5.scatter_prediction_by_current_charge(merged_df)
    part5.scatter_prediction_vs_outcome(merged_df)


if __name__ == "__main__":
    main()
