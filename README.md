*(line ...) refers to specific line(s) in the 20210325T1530Z_1D_NL_EQ_001.xml file.


## Task 1:

4. On 2024-08-04 between 06.00 and 12.00 there are some inconsistencies, where imbalance was not decreasing after the activation action. Might be because there was not enough activation.
   
 	Something similar can be seen on 2024-08-10 between 09.00 and 17.00, and on 2024-08-11 , between 09.00 and 15.00, but this time there was almost no activation at all. It activated too late.
	
   Overall The upwards activation has been quite precise.

## Task 2:

### 1. 	
      1.generator - 225kW (line 582)
	  2.generator - 990kW (line 625)
	  3.generator - 225kW (line 667)
	  adding up nominal powers in the generators, then total is 1440 kW
### 2. 
    nominal 15.75 kV (lines 1625-1628)
  
### 3.
    Permanently allowed limit is 1876, temporarily allowed 500. (lines 198-237)
    Permanent allowed limit should be used in normal conditions, temporarily limit is for emergencies or other unusual conditions
   
### 4.
    NL-G1 is set as slack in the model as it's the largest and most flexible generator. (lines 585 - 627)
    It also has some kind of regulating control, which might be related to the slack node. (lines 1913-1918)
    lines 585-627. Slack node is needed to maintain balance in the power system

### 5.
    _1dc9afba-23b5-41a0-8540-b479ed8baf4b is missing rated voltage. 
    Typo in the xml code, line 16 was missing closing tag. 

## Task 3:

### 1.
    UTC time should be used when systems, that are connected to each other, are used in different countries/timezones or systems that are controlled from different timezones. 
	  This could be applied in software development as well, if team members work from different timezones. 
	  UTC time should be used when logging information or when timestamps are used in databases.
### 2.
    Local time can be used in applications that are user-centric. Like Calendars, meeting scheduling apps etc - It's more user-friendly and no need to calculate time into local timezone.
### 3.
    It depends on the context. For users it can lead to confusion if not clearly defined. Some can say that left closed, right closed can be more user-friendly as both start and end times are included in the interval.
	For calculations I would use left closed, right open.
