import pandas as pd
from pprint import pprint
from ipwhois import IPWhois
from datetime import datetime
import socket 
import csv
import re
import ipwhois
import whois
from pprint import pprint
from datetime import datetime
import socket
from time import sleep


print("-" * 50)
print("GoPhish Reporting : "+str(datetime.now()))
print("-" * 50)

file_name =input("Please enter the name of the csv file with the GoPhish Results:")

print("-" * 50)
print("Time started : "+str(datetime.now()))
print("-" * 50)


df =pd.read_csv(file_name)
#print(df[['status','ip','email','id']])

for (status), group in df.groupby(["status"]):
     group.to_csv(f'{status}.csv',index=False) 
                                 
print(pd.read_csv("Email Opened.csv"))
print(pd.read_csv("Clicked Link.csv")) 

###################################################################################################

print("-" * 50)
print("next extract ips from Email Opened.csv: "+str(datetime.now()))
print("-" * 50)

def extract_ip_addresses(input_file1, output_file1):
     ip_set = set()
     
     # Extract IP addresses from the first CSV file
     with open(input_file1, "r") as file1:
          reader = csv.reader(file1)
          for row in reader:
               for item in row:
                    ips = re.findall(r'\'?(?:\d{1,3}\.){3}\d{1,3}\'?', item)
                    ip_set.update(ips)

  #Write the IP addresses to the output CSV file
     with open(output_file1, 'w', newline='') as outfile1:
        writer = csv.writer(outfile1)
        for ip in ip_set:
            writer.writerow([ip])



def extract_ip_address( input_file2, output_file2):
     ip_set = set()
     

      # Extract IP addresses from the second CSV file
     with open(input_file2, 'r') as file2:
        reader = csv.reader(file2)
        for row in reader:
            for item in row:
                ips = re.findall(r'\'?(?:\d{1,3}\.){3}\d{1,3}\'?', item)
                ip_set.update(ips)

  
    #Write the IP addresses to the output CSV file
     with open(output_file2, 'w', newline='') as outfile1:
        writer = csv.writer(outfile1)
        for ip in ip_set:
            writer.writerow([ip])


# Example usage
input_file1 = 'Email Opened.csv'
input_file2 = 'Clicked Link.csv'
output_file1 = 'ip_list_Open.csv'
output_file2 ='ip_list_Click.csv'

extract_ip_addresses(input_file1, output_file1)
extract_ip_address(input_file2, output_file2)

#######################################################################################################






print(pd.read_csv("ip_list_Open.csv")) 


print("-" * 50)
print("Time next step: "+str(datetime.now()))
print("-" * 50)
sleep(60)
print('starting isp provider lookup from ip_list_open.csv')
print("-" * 50)

def ip_whois_lookup(ip):
    if ip.startswith('10.'):
        print(f'skipping private ip {ip} in the 10.*  range')
        return None
    if ip.startswith('172.'):
        print(f'skipping private ip {ip} in the 172.* range')
        return None
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        if 'asn_description' in result:
            return result['asn_description']
    except Exception as e:
        print(f" {ip} {str(e)}")
    return None
    

input_file ='ip_list_Open.csv'
output_file = 'ip_result_Open.csv'

with open(input_file, 'r') as file:
    ip_list = file.read().splitlines()

with open(output_file, 'w') as file:
    for ip in ip_list:
        result = ip_whois_lookup(ip)
        if result:
            file.write(f'{ip},')
            file.write( str(result) )
            file.write('\n\n')
         
        else:
            file.write(f' {ip}\n\n')

print(f'WHOIS results saved to {output_file}')
print("-" * 50)
print("next extract ips from Clicked Link.csv: "+str(datetime.now()))
print("-" * 50)



def add_header_rows(input_file, output_file, header_rows):


    with open(input_file, 'r') as file:
        rows = list(csv.reader(file))

    rows = header_rows + rows 

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


input_file ='ip_result_Open.csv'
output_file ='open_provider.csv'
header_rows =[['ip', 'asn_description', 'country', 'blank']]


add_header_rows(input_file, output_file, header_rows)



################################################################################################################

print(pd.read_csv("ip_list_Click.csv")) 


print("-" * 50)
print("Time next step: "+str(datetime.now()))
print("-" * 50)
sleep(60)
print('starting isp provider lookup of clicked links')
print("-" * 50)

def ip_whois_lookup(ip):
    if ip.startswith('10.'):
        print(f'skipping private ip {ip} in the 10.*  range')
        return None
    if ip.startswith('172.'):
        print(f'skipping private ip {ip} in the 172.* range')
        return None
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)
        if 'asn_description' in result:
            return result['asn_description']
    except Exception as e:
        print(f"{ip} {str(e)}")
    return None
    

input_file ='ip_list_Click.csv'
output_file = 'ip_result_Click.csv'

with open(input_file, 'r') as file:
    ip_list = file.read().splitlines()

with open(output_file, 'w') as file:
    for ip in ip_list:
        result = ip_whois_lookup(ip)
        if result:
            file.write(f'{ip},')
            file.write( str(result) )
            file.write('\n\n')
         
        else:
            file.write(f' {ip}\n\n')

print(f'WHOIS results saved to {output_file}')

print("-" * 50)
print("Time Finished: "+str(datetime.now()))
print ("\n")
print(" results are nearly ready")
print("-" * 50)



def add_header_rows(input_file, output_file, header_rows):
    with open(input_file, 'r') as file:
        rows = list(csv.reader(file))

    rows = header_rows + rows 

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


input_file ='ip_result_Click.csv'
output_file ='Click_provider.csv'
header_rows =[['ip', 'asn_description', 'country', 'blank']]
add_header_rows(input_file, output_file, header_rows)

##################################################################################################################################

 #Input file paths
file1_path = 'Clicked Link.csv'
file2_path = 'Click_provider.csv'
# Output file path
output_file_path = 'Click_add_provider_to_original.csv'

# Read data from file1
file1_data = {}
with open(file1_path, 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        ip = row['ip']
        if ip not in file1_data:
            file1_data[ip] = row

# Read data from file2 and match based on IP addresses
matched_data = []
with open(file2_path, 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        ip = row['ip']
        if ip not in file1_data:
            file1_data[ip] = {}
        file1_data[ip].update(row)

# Determine the fieldnames by combining the keys from all rows
fieldnames = set().union(*file1_data.values())

# Write matched data to the output file, including all relevant 

with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(file1_data.values())

print(f"Output file '{output_file_path}' created successfully.")


#################################################################################################

 #nput file paths
file1_path = 'Email Opened.csv'
file2_path = 'open_provider.csv'
# Output file path
output_file_path = 'Open_add_provider_to_original.csv'

# Read data from file1
file1_data = {}
with open(file1_path, 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        ip = row['ip']
        if ip not in file1_data:
            file1_data[ip] = row

# Read data from file2 and match based on IP addresses
matched_data = []
with open(file2_path, 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        ip = row['ip']
        if ip not in file1_data:
            file1_data[ip] = {}
        file1_data[ip].update(row)

# Determine the fieldnames by combining the keys from all rows
fieldnames = set().union(*file1_data.values())

# Write matched data to the output file, including all relevant 

with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(file1_data.values())

print(f"Output file '{output_file_path}' created successfully.")


#################################################################################################

import csv

# Input file paths
file1_path = 'Email Sent.csv'
file2_path = 'Open_add_provider_to_original.csv'
file3_path = 'Click_add_provider_to_original.csv'

# Output file path
output_file_path = 'Everything.csv'

# Read data from file1
file1_data = []
with open(file1_path, 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        file1_data.append(row)

# Read data from file2
file2_data = []
with open(file2_path, 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        file2_data.append(row)

# Read data from file3
file3_data = []
with open(file3_path, 'r') as file3:
    reader = csv.DictReader(file3)
    for row in reader:
        file3_data.append(row)

# Combine all data into a single list
all_data = file1_data + file2_data + file3_data

# Determine the fieldnames by combining the keys from all rows
fieldnames = set().union(*all_data)

# Write all data to the output file
with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)

print(f"Output file '{output_file_path}' created successfully.")

##############################################################################################################################################
print("-" * 50)
print('Final step convert to excel:'+str(datetime.now()))
print("-" * 50)

csv_file = 'Everything.csv'
df = pd.read_csv(csv_file)

new_order =['id','status', 'time', 'campaign_id', 'email', 'ip', 'asn_description', 'country', 'blank']
df = df[new_order]

excel_file = 'Report_Results.xlsx'
df.to_excel(excel_file, index=False)

print(f"csv file '{csv_file}' converted to excel '{excel_file}' success")




print("-" * 50)
print("Time Finished: "+str(datetime.now()))
print ("\n")
print("Script finished, results are ready ")
print("-" * 50)
