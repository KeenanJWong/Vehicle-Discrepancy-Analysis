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

** From the pie chart generated using Python, it can be seen that 39% of the records in the Vehicle System log were recorded as 'Issue 2' rather than 'Issue 1'. 
** A significant portion of the records are recorded incorrectly.
** This could pose problems in a maintenance and a business improvement point of view.
** As the amount of Issue 1 is alot lower that it should be whilst the amount of Issue 2 is alot higher than it should be.
** Therefore the urgency of Issue 1 is would not be as significant as it should be while Issue 2 is more significant than it actually is. 








