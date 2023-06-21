GoPhishReportGeneration

This program will input a csv file with GoPhish results then separate the ip addressess and corry out an Ip look up to identify the ISP/provider. Currently the required file must be located in the same file location as .py script, and the outputed files will be located in the same destination. I have created a largee quantity of ourput files this was for review that theprogram was correctly extracting, finding provider information while keeping the data intact. The final file will be converted to an excel format to Report_Results.xlsx file. 

The script is still a work in progress as the final file contain all the original data with the added provider information but it contains a double IP entry on th 10.* ans 172.* range ip addresses. I will need to reviewwhy this is happening but in the interin you can just delete the extra ip's as the complete original information is there, please double check though to be sure before deleting. 
