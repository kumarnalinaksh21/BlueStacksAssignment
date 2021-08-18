# BlueStacksAssignment
This repository contains the assignments for BlueStacks DevOps vacancy
***
## Assignment 1 : 
This assignment is to create an Amazon CloudFront(CDN) for your static content website which you have to host on S3 bucket (https://xxxxxxxxx.cloudfront.net/)

Case A. If the user opens (https://xxxxxxxxx.cloudfront.net/) it should be seen "Hello, CDN origin is working fine"

      A.1 This behavior object content stays in an Edge Cache at for at least 48 hours 

Case B. If user opens (https://xxxxxxxxx.cloudfront.net/devops-folder/) it should fetch from other S3 bucket and user should see "Hello, CDN 2 origin is working fine"

      B.1 This behavior header should base caching on HOST and CloudFront-Viewer-Country

### NOTE: Please create only one CloudFront Distribution without the Alternate Domain Names (CNAMEs) and share the CDN domain name to validate the assignment.

### NOTE: Both the URL's should not include index.html `

## Soultion 1:
*Case A*. https://dq4ek4i824wn5.cloudfront.net

![image](https://user-images.githubusercontent.com/32825207/129965173-12f78d0c-039d-41b5-af11-a6e729aa1c32.png)




*Case B*. https://dq4ek4i824wn5.cloudfront.net/devops-folder/

![image](https://user-images.githubusercontent.com/32825207/129965232-8506378e-d2f8-448b-9859-c9579b60021b.png)




***

## Assignment 2

We want to gather some basic statistics for our security team. They want to know the top 8 IP addresses that hit our web servers.

Your task will be the following:
Implement a script (use any language you want) to get the top 8 IP addresses out of an existing log file
Save your script with no file extension
It has to be an executable file
there is no need for using arguments
The output format will be the following:(8 lines - top saw IP addresses by the number of hits):

<ip_address><space><number_of_hits>

A real example output would look like this:

$ count

92.6.41.236 22

186.248.72.9 19

81.243.137.36 18

217.118.78.16 15

213.118.39.51 15

93.146.139.64 14

80.116.15.0 14

186.213.159.176 11

Logfile: [Click here](https://github.com/bluestacks/dev-ops-challenge/blob/master/logfile)

### NOTE: Use AWS free tier for hosting.

## Soultion 2:
I used Python for this.
The python script and executable files are both shared in the repository.
Here is the snippet of the execution.


![image](https://user-images.githubusercontent.com/32825207/129964192-485d75a2-1e06-4326-a17c-4f74a890648d.png)
***
