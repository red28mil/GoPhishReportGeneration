
GoPhishReportGeneration

This program will input a csv file with GoPhish results then separate the ip addressess and carry out an Ip look up to identify the ISP/provider. Currently the required file must be located in the same file location as .py script, and the output files will be located in the same destination. I have created a large quantity of output files this was for review; that the program was correctly extracting, finding provider information while keeping the data intact. The final file which contains all the relevant information will be converted to an excel format to Report_Results.xlsx file, or in everything.csv.

The script is still a work in progress as the final file contains all the original data with the added provider information but it also contains a double IP entry on the 10.* ans 172.16.* - 172.31.255.255 and 192.* range ip addresses. I will need to review why this is happening but in the interim you can just delete the extra ip's as the complete original information is there, please double check though to be sure before deleting. 

I am running this in vs code, using python libraries version 3.11.2 I currently have it saved in my github account if anyone would like to download it from there just let me know.

NB.You must open the gophish download in excel first and extract the details header, to columns are required to run the script; ip and id. To do this you select the column named details and then click on the text to column button along the top row of the home tab. once open select delimit other and enter " then click next this will extract the information required. Name the ip addresses column header as ip (lowercase) and the the id column as id(lowercase), the other extracted columns can be deleted. 

Also the header and column that contains email sent, semail opened and clicked link must have its header named status(lowercase) as this info is hardcoded into the script.

Save this file and capy it into the gophishreportgeneration folder where the script is contained.

Open the script on VSCode(or your chosen ide). run the script enter the name of the file including the <nameoffile>.csv. the script will run and the output can be found in the gophishreportgeneration folder.




From the initial file there will be 3 output files:
1. Email Sent.csv 
2. Email Opened.csv
3. Clicked Link.csv

Then the next step is to extract the list of IP's from Email Opened and Clicked link:   
1.ip_list_Open.csv  
2.ip_list_Click.csv
                                                                                                                                             
Then isp whois lookup: 

1.ip_result_Open.csv  
2.ip_result_click.csv


This lookup is completed without headers so we need to add them back so we can parse back to the relevant files: 
1. open_provider.csv
2. click_provider.csv

                                                                                                                                        
                                                                                                                                      

Finally we need to add this information back to email opened and clicked link files: 

1.open_add_provider_to_original.csv

2.click_add_provider_to_original.csv

Next put all 3 original files back to one file like it was at the start:

Everything.csv


Last step convert to an excel file named: 


Report_Results.xlsx                                                                                   


note: again final report still has an issue with ignored ip's, i will work on rectifying this.

