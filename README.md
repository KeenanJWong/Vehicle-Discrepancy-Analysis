# Vehicle Discrepancy Analysis #

#### Problem Statement ####
The Vehicle System Log, which records all errors that the vehicle encounters, has been stated to inaccurately record 'Issue 1' as 'Issue 2'. <br/>
Analysis to highlight the scale of inaccuracy is required to justify the business case in order for the IT team to allocate resources. 
<br/>
<br/>
#### Methodology  ####
Software used:
* Python
* Excel <br/>

Datasets from a sample period (1/1/2022 to 1/1/2023) were extracted for comparison. 
* First Dataset: [VehicleIssue1_Identfied.xlsx](https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/VehicleIssue1_Identfied.xlsx)
  * Data from the Machine performance log
  * This data provides timestamps where certain condition are met within the vehicle indicating 'Issue 1' occurred.
  
* Second Dataset: [VehicleIssuesSystemLog.xlsx](https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/VehicleIssuesSystemLog.xlsx)
  - Data from the Vehicle System log
  - Data to show all the errors that have been recorded.

Using Python, the timestamps from the second dataset were intersected with the timestamps from the first dataset. <br/>
* This is to match the records from the Vehicle system log to the timestamps of 'Issue 1' occurrences from the Machine performance log. <br/>
* By doing so, we can identify when the Vehicle system log has recorded 'Issue 2' when it should have recorded 'Issue 1' according to the Machine performance log
* Python Script Link: [VehicleIssueDiscrepancyAnalysis.py ](https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/VehicleIssueDiscrepancyAnalysis.py)
* Resulting dataset with intersected timestamps displayed as an excel file: [VehicleIssueDiscrepancyAnalysis.xlsx](https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/VehicleIssueDiscrepancyAnalysis.xlsx)

Analysis was done to see what proportion of records in the Vehicle system log were registered as 'Issue 2' rather than 'Issue 1'.
<br/>
<br/>
#### Analysis and Insights ####

![Image](/Vehicle-Discrepancy-Analysis/assets/Images/PieChart_ProportionOfSystemLoggedIssues.png)

From the chart generated using Python, it can be seen that 39% of 'Issue 1' occurences from the Machine performance log were recorded as 'Issue 2' in the Vehicle System log.  

Therefore, two problems are identified:
 1.  The significance of 'Issue 1' and 'Issue 2' are reduced and inflated, respectively
 2.  Unnecessary downtime caused as Maintenance would be trying to solve for 'Issue 2' when 'Issue 1' is the actual problem

If this discrepancy can be fixed, unnecessary downtime can be avoided and improvement initiatives will be more effective as more accurate data will be used.
