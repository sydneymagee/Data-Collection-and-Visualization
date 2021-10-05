"""
This is the data visualization file for WEC
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# When scraping the horse_name is formatted like "Horse: THENAME     #SOMENUMBERS
# I used str.split to fix this below
# Source: https://www.geeksforgeeks.org/python-pandas-split-strings-into-two-list-columns-using-str-split/
def fix_horse_name(df):
    df['horse_name'] = df['horse_name'].str.replace('Horse: ', '')
    newdf = df['horse_name'].str.split('        ', n=1, expand=True)
    df['Horse Name'] = newdf[0]
    df['Horse Number'] = newdf[1]
    df.drop(columns=['horse_name'], inplace=True)
    return df

#def drop_Outlier(df):
    #drop_data = df.set_index("Section")
    #print(drop_data.head())
    #drop_data.drop(['Open Jumper by Money Won','National Derby by money won'])
    #print(df.head())

def per_horse(df, horse_name):
    df0 = df[df['Horse Name'] == horse_name]
    df1 = df0[['Horse Name','Points','Place','Rider']]
    riders = df1['Rider']
    ax = df1.plot.bar(rot=0, subplots=True, title=['', ''], color={'Points':'c','Place':'m'})
    ax[0].set_title("Results for " + horse_name)
    ax[1].set_xticklabels(riders)
    ax[1].set_xlabel("RIDERS")
    ax[1].set_ylabel("POINTS")
    ax[0].set_ylabel("PLACING")
    plt.xticks(rotation=90)
    return ax

def per_rider(df, rider_name):
    df0 = df[df['Rider'] == rider_name]
    df1 = df0[['Rider','Horse Name','Place','Points']]
    horses = df1['Horse Name']
    ax = df1.plot.bar(rot=0, subplots=True, title=['', ''], color={'Points':'c','Place':'m'})
    ax[0].set_title("Results for " + rider_name)
    ax[1].set_xticklabels(horses)
    ax[1].set_xlabel("HORSES")
    ax[1].set_ylabel("POINTS")
    ax[0].set_ylabel("PLACING")
    plt.xticks(rotation=90)
    return ax

def rider_show(df, show, rider):
    df0 = df[df['Rider'].str.startswith(rider)]
    df0 = df0[df0['Show'] == show]
    df1 = df0.groupby(['Rider'])['Points'].aggregate(['sum'])
    ax = df1.plot.bar(rot=0, color={'sum':'r'})
    ax.set_title("Riders with the initial " + rider + " At " + show)
    ax.set_xlabel("RIDERS")
    ax.set_ylabel("POINTS AT THE SHOW")
    plt.xticks(rotation=90)
    return ax

def avg_sections_per_show(df, show):
    df0 = df[df['Show'] == show]
    df0 = df.groupby('Section')['Points'].mean().reset_index()
    df0.plot(kind='scatter', x='Section', y='Points', color='navy')
    plt.xticks(rotation=90)
    plt.title("The Average of Each " + show + "'s Points")
    
def sum_sections_per_show(df, show):
    df0 = df[df['Show'] == show]
    df0 = df.groupby('Section')['Points'].sum().reset_index()
    df0.plot(kind='scatter', x='Section', y='Points', color='forestgreen')
    plt.xticks(rotation=90)
    plt.title("Each Section of " + show + "'s Results")

def all_shows(df):
    df0 = df.groupby('Show')['Points'].sum().reset_index()
    df0.plot(kind='scatter', x='Show', y='Points', color='steelblue')
    plt.xticks(rotation=90)
    plt.title("Each Horse Show's Cumulative Points")

def main():
    df = pd.read_csv('wec_results.csv')                                 #read in the csv and get df
    fix_horse_name(df)
    df['rider'].fillna("No Name", inplace=True)
    df.rename(columns={'section':'Section','show_class':'Show Class',
        'show':'Show','rider':'Rider','place':'Place','entries':'Entries',
        'points':'Points'}, inplace=True)
    
    print("----------------------------------------------------")
    print("------------World Equestrian Center Data------------")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    #drop_Outlier(df)
    
    horse_name = input('Horse Name: ')
    per_horse(df, horse_name)
    
    rider_name = input('Rider Name: ')
    per_rider(df, rider_name)
    
    show_name = input('Show Name: ')
    rider_initial = input("Rider's first initial: ")
    rider_show(df, show_name, rider_initial)
    
    show00 = input('Show Name: ')
    avg_sections_per_show(df, show00) 
    
    show0 = input('Show Name: ')
    sum_sections_per_show(df, show0)
    
    all_shows(df)
    
    plt.show()
       

if __name__ == '__main__':
    main()    

