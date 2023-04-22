import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)


###VI_DF (System Log) Dataframe
VI_DF = pd.read_excel('VehicleIssuesSystemLog.xlsx')
VI_DF['StartDate'] = VI_DF['TimeStart'].dt.date
VI_DF['EndDate'] = VI_DF['TimeEnd'].dt.date

#Creation of Date Join Keys to intersect date points for first dataset
VI_DF['JoinKey1'] = VI_DF['EndDate']
VI_DF['JoinKey2'] = VI_DF['StartDate']


###Identified VIssue1 Dataframe
VIssue1 = pd.read_excel('VehicleIssue1_Identfied.xlsx')
VIssue1['StartDate'] = VIssue1['Issue1Start'].dt.date
VIssue1['EndDate'] = VIssue1['Issue1End'].dt.date

#Creation of Date Join Keys to intersect DATE points for second dataset
VIssue1['JoinKey1'] = VIssue1['StartDate']
VIssue1['JoinKey2'] = VIssue1['EndDate']


###Select columns from first dataset to left join onto second.
VI_DFI = VI_DF[['TimeStart', 'TimeEnd', 'StartDate', 'EndDate', 'JoinKey1', 'JoinKey2']]


###Combined Dataframe 1 (Intersects VIssue1 START dates with VI_DF END dates
VIssue1_m1 = VIssue1.merge(VI_DFI, on = 'JoinKey1', how = 'left')
VIssue1_m1 = VIssue1_m1[['S', 'Issue1Start', 'Issue1End', 'Issue1_mins', 'TimeStart', 'TimeEnd']]


###Combined Dataframe 2 (Intersects VIssue1 END dates with VI_DF START dates
VIssue1_m2 = VIssue1.merge(VI_DFI, on = 'JoinKey2', how = 'left')
VIssue1_m2 = VIssue1_m2[['S', 'Issue1Start', 'Issue1End', 'Issue1_mins',  'TimeStart', 'TimeEnd' ]]


###Append combined DF to show all possible intersecting date events
VIssues_App = pd.concat([VIssue1_m1, VIssue1_m2], ignore_index=True)
VIssues_App.drop_duplicates(inplace = True)


###Function to indicate which DATETIMEs from the appended DF interesect
def datetimeintersect(intersect):
    if (intersect['TimeStart'] <= intersect['Issue1Start']) & (intersect['TimeEnd'] >= intersect['Issue1Start']):
        return 1
    elif (intersect['TimeStart'] >= intersect['Issue1Start']) & (intersect['TimeEnd'] <= intersect['Issue1End']):
        return 2
    elif (intersect['TimeStart'] <= intersect['Issue1End']) & (intersect['TimeEnd'] >= intersect['Issue1End']):
        return 3
    else:
        return 0

#VIssues Appended Dataframe where DATETIME from System log intersects with VIssue1 DATETIME
VIssues_App['conditions'] = VIssues_App.apply(datetimeintersect, axis = 1)
VIssues_AppYes = VIssues_App[VIssues_App['conditions'] != 0] #0 = Datetime of records to not intersect.


###Left join columns from VI_DF (System Log) dataframe to match Comments or intersecting datetimes columns
VIssue1_Yes = VIssues_AppYes.merge(VI_DF, on = 'TimeStart' , how = 'left')
VIssue1_Yes = VIssue1_Yes[['S_x', 'Issue1Start', 'Issue1End', 'Issue1_mins', 'TimeStart', 'TimeEnd_x', 'Issue', 'Comment', 'conditions']]
VIssue1_Yes.drop_duplicates(inplace=True)


###Getting VIssue1 DATETIMES where System Log DATETIMES do not intersect (therefore it is not recorded by the system)
VIssues_AppNo = VIssues_App[VIssues_App['conditions'] == 0]
VIssue1_No = VIssues_AppNo.merge(VI_DF, on = 'TimeStart' , how = 'left')
VIssue1_No = VIssue1_No[['S_x', 'Issue1Start', 'Issue1End', 'Issue1_mins']]
VIssue1_No.drop_duplicates(inplace=True)


###Appending VIssues1 Dataframes with and without intersections.
VIssue_Appended = pd.concat([VIssue1_Yes, VIssue1_No], ignore_index=True)
VIssue_Appended.sort_values(by=['Issue1_mins','Issue1Start'], ascending=False,inplace=True)
VIssue_Appended.reset_index(drop=True,inplace=True)


###Separating and Removing rows that show Null but are duplications from the first Dataframe Merge (With Dates only).
condition = [1]
i = 1

for y in range(len(VIssue_Appended)-1):
    if pd.notnull(VIssue_Appended.iloc[i,4]) and (VIssue_Appended.iloc[i,1] == VIssue_Appended.iloc[i-1,1]):
        j = 1
    elif (pd.isnull(VIssue_Appended.iloc[i,4])) and (VIssue_Appended.iloc[i,1] == VIssue_Appended.iloc[i-1,1]):
        j = 2
    else:
        j = 0
    condition.append(j)
    i = i + 1


VIssue_Appended['con'] = pd.Series(condition)
VIssue_Appended = VIssue_Appended[VIssue_Appended['con'] != 2]


###Filtering out results where Issues from VI_DF dataframe (System Log) have been recorded as 'Issue 2' or not recorded whilst interesecting with timestamps from VIssue1 dataframe.
VIssue_Appended_I2 = VIssue_Appended[VIssue_Appended['Issue'] != 'Issue 1']


###Creating highlighted rows to visually group the same Issue timestamps
Highlight = [1]
k = 1

for z in range(1,len(VIssue_Appended_I2)):
    if VIssue_Appended_I2.iloc[k,1] == VIssue_Appended_I2.iloc[k-1,1]:
        l = Highlight[k-1] #If the current row timestamp = previous row timestamp: l = last variable in list
    else:
        if Highlight[k-1] == 1:
            l = 0 #If last variable in list = 1, assign l as 0
        else:
            l = 1
    Highlight.append(l) #Append current l variable onto list
    k = k + 1

VIssue_Appended_I2['Highlight'] = Highlight #Highlight list becomes column

#Apply colours to group timestamps
def highlightcolour(rows):
    value = rows.loc['Highlight']
    if value == 1:
        color = '#BAE1FF'
    else:
        color = '#BAFFC9'
    return ['background-color: {}'.format(color) for r in rows]


###Cleaning up Final Dataframe and applying grouping colour
VIssue_Appended_I2 = VIssue_Appended_I2.rename(columns={'S_x': 'S', 'TimeEnd_x': 'TimeEnd'})
VIssue_Appended_I2 = VIssue_Appended_I2[['S', 'Issue1Start', 'Issue1End', 'Issue1_mins', 'TimeStart','TimeEnd','Issue','Comment','Highlight']]
VIssue_Appended_I2.reset_index(inplace=True,drop=True)
VIssue_Final = VIssue_Appended_I2.style.apply(highlightcolour, axis=1)


###Exporting Final dataframe to excel
#print(VIssue_Final)
filename = 'VehicleIssueDiscrepancyAnalysis.xlsx'
VIssue_Final.to_excel(filename)


###Pie chart to display the proportion of System-logged issues that are recorded incorrectly as 'Issue 2'/Not recorded
Issue1_Rec = len(VIssue_Appended[VIssue_Appended['Issue'] == 'Issue 1'])
Issue2_Rec = len(VIssue_Appended[VIssue_Appended['Issue'] == 'Issue 2'])
Not_Recorded = len(VIssue_Appended) - (Issue1_Rec + Issue2_Rec)

Issue_Data = [Issue1_Rec, Issue2_Rec, Not_Recorded]
Issue_label =['Issue 1', 'Issue 2', 'Not Recorded']
Colors = sns.color_palette('deep')[0:5]

plt.pie(Issue_Data, labels = Issue_label, autopct='%.0f%%', colors = Colors)
plt.title('% Proportion of System Logged Issues')
plt.show()