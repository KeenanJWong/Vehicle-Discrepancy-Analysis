# Vehicle_Discr
Repository for Vehicle Issue Discrepancy project <br />
<br />

* Tools used: Python, Excel

* Problem statement: 
** The Vehicle System Log, which records all errors that the vehicle encounters, has been stated to inaccurately record 'Issue 1' as 'Issue 2'. 
Analysis to highlight the scale of inaccuracy is required to justify the business case in order for the Maintenance team to allocate resources. 


* Methodology: 
** Datasets from a sample period (1/1/2022 to 1/1/2023) were extracted for comparison:
*** First Dataset: 
****  Data from the Machine performance log. 
****  This data provides timestamps where certain condition are met within the vehicle indicating 'Issue 1' occurred.

*** Second Dataset:
**** Data from the Vehicle System log. 
**** Data to show all the errors that have been recorded.

** Using Python, the timestamps from the second dataset were intersected with the timestamps from the first dataset 
This is to match the records from the Vehicle system log to the timestamps of 'Issue 1' occurrences from the Machine performance log.
*** Python script found in repository: 

** Analysis was done to see what the proportion of records in the Vehicle system log were recorded as 'Issue 2' rather than 'Issue 1'.


* Analysis and Insights

**Insert picture

** From the pie chart generated using Python, it can be seen that 39% of 'Issue 1' occurences from the Machine performance log were recorded
recorded as 'Issue 2' rather than 'Issue 1' in the Vehicle System log. 
** Therefore the seriousness of 'Issue 1' is diluted whilst the seriousness of Issue 2 is inflated.
** Therefore when Issue 1 occurs, maintenance would be trying to solve for Issue 2 when Issue 1 is actually the problem - leading to unnecessary downtime.
** If this can be fixed this can be avoided as maintenance would know what to do.








