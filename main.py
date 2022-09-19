import pandas as pd
df = pd.read_excel('Analytics Template for Exercise.xlsx', sheet_name=0)
# to check if all data have the same length
def test_len(list_dict):
    lis = []
    for i in list_dict:
        lis.append(len(list_dict[i]))
    assert lis.count(max(lis)) == len(list_dict.keys()), "Missing data"
# Empty dictionary to store each occurrence
lst_dict = {'Date':[],'Site ID':[],'Page Views':[], 'Unique Visitors':[], 'Total Time Spent':[], 'Visits':[], 'Average Time Spent on Site':[]}
"""
- range from 2 to length of all data
- start from 2 because it contains the details of each column i need in it and step 3 to get the next details and skip useless indexes
- In for loop
    - convert to list to concat all values with the new values without lossing previus data
    - In site ID multiply by 31 to cover 31 days and make all length values equles
"""
for i in range(2, len(df), 3):
    lst_dict['Date'] = lst_dict['Date']+list(df.iloc[1][1:32])
    lst_dict['Site ID'] = lst_dict['Site ID']+[df.iloc[i][0]]*31
    lst_dict['Page Views'] = lst_dict['Page Views']+list(df.iloc[i][1:32].values)
    lst_dict['Unique Visitors'] = lst_dict['Unique Visitors']+list(df.iloc[i][32:63].values)
    lst_dict['Total Time Spent'] = lst_dict['Total Time Spent']+list(df.iloc[i][63:94].values)
    lst_dict['Visits'] = lst_dict['Visits']+list(df.iloc[i][94:125].values)
    lst_dict['Average Time Spent on Site'] = lst_dict['Average Time Spent on Site']+list(df.iloc[i][125:].values)
    # to check length of data
    test_len(lst_dict)
    
# create dataframe
data = pd.DataFrame(lst_dict)
# insert Day of month column 
data.insert(loc=0, column='Day of Month', value=data['Date'].dt.day)
# save data in new file
data.to_csv('vistors.csv',index=False, date_format='%Y-%m-%d')