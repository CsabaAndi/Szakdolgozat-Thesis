import pandas as pd
from datetime import datetime


def read_and_concat_updated_df():

    old = r"old.json"
    new = r"new.json"
    base = r"output\data\match-history\england\chelsea-football-club.json"


    # convert false azért kell mert vmiért automatic convertálja a dateket szarul
    old_df = pd.read_json(old, convert_dates=False)
    new_df = pd.read_json(new, convert_dates=False)  
    all_df = pd.read_json(base, convert_dates=False)  


    only_new_diff_df = old_df.merge(new_df, how='outer', indicator=True).loc[lambda x: x.pop('_merge') == 'right_only']
    out_df = pd.concat([old_df, only_new_diff_df.drop_duplicates()])

   
    out_df_clean = out_df.loc[(~out_df["Score"].isin(["-", "CANC", "SUSP"])) & (~out_df["Score"].str.match("\d\d:\d\d", na=False))] # valamiért van nan??
    all_df_clean = all_df.loc[(~all_df["Score"].isin(["-", "CANC", "SUSP"])) & (~all_df["Score"].str.match("\d\d:\d\d", na=False))] # valamiért van nan??


    pd.options.mode.chained_assignment = None  # default='warn'

    out_df_clean['Date'] = pd.to_datetime(out_df_clean['Date'], format=r'%d/%m/%y').dt.date
    all_df_clean['Date'] = pd.to_datetime(all_df_clean['Date'], format=r'%d/%m/%y').dt.date

    out = out_df_clean.loc[out_df_clean['Date'].between(datetime.strptime("01/01/0001", r'%d/%m/%Y').date(), datetime.strptime("01/01/2022", r'%d/%m/%Y').date())].sort_values(by='Date', ascending=True)
    all = all_df_clean.loc[all_df_clean['Date'].between(datetime.strptime("01/01/0001", r'%d/%m/%Y').date(), datetime.strptime("01/01/2022", r'%d/%m/%Y').date())].sort_values(by='Date', ascending=True)
    

    print(out.shape)
    print(all.shape)
    
    out.set_index('Date', inplace=True)
    all.set_index('Date', inplace=True)

    print(out.to_string())
    print(all.to_string())
    print(out.equals(all))
    




    return 0


if __name__ == "__main__":
    read_and_concat_updated_df()