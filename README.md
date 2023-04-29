# Vehicle_Discr
Repository for Vehicle Issue Discrepancy project <br />
<br />


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





By looking into the Vehicle machine log we are able to map out all the indications of 'Issue 1' and the time stamps
** We then compare the time stamps of the 'Issue 1' indications to what is recorded in the Vehicle System log.
***From there we can see which records in the Vehicle system log were recorded as an incorrect issue and not 'Issue 1'.

*Tools used: Python, Excel
