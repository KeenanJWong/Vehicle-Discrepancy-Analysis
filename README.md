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
* First Dataset: 
  * Data from the Machine performance log
  * This data provides timestamps where certain condition are met within the vehicle indicating 'Issue 1' occurred.
  
* Second Dataset:
  * Data from the Vehicle System log
  * Data to show all the errors that have been recorded.

Using Python, the timestamps from the second dataset were intersected with the timestamps from the first dataset. <br/>
* This is to match the records from the Vehicle system log to the timestamps of 'Issue 1' occurrences from the Machine performance log. <br/>
* Python Script Link: [Vehicle Discrepancy Py](https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/VehicleIssueDiscrepancyAnalysis.py)

Analysis was done to see what proportion of records in the Vehicle system log were registered as 'Issue 2' rather than 'Issue 1'.
<br/>
<br/>
#### Analysis and Insights ####

[IMage] (https://github.com/KeenanJWong/Vehicle-Discrepancy-Analysis/blob/main/PieChart_ProportionOfSystemLoggedIssues.png)

** From the chart generated using Python, it can be seen that 39% of 'Issue 1' occurences from the Machine performance log were recorded as 'Issue 2' in the Vehicle System log. 
** Therefore, two problems are identified:
*** 1) The significance of 'Issue 1' and 'Issue 2' are reduced and inflated, respectively
*** 2) Unnecessary downtime caused as Maintenance would be trying to solve for 'Issue 2' when 'Issue 1' is the actual problem

** If this discrepancy can be fixed, unnecessary downtime can be avoided and improvement initiatives will be more effective as accurate data will be used.
