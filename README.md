# A ICD-10-CM Lookup Software

ICD-10 (International Classification of Diseases, Version 10) is a standardized coding system used in most of the world
to describe morbidity (disease) and mortality (death) for electronic health records and public health reporting. It has
been used for mortality reporting in the United States since 1999, and on October 1, 2015, an extended version of ICD-
10 called ICD-10-CM (“Clinical Modification”) became the standard morbidity coding system for electronic health
records in the US as well.


### Step 1. Developing an ICD-10-CM Lookup Program

Based upon the following user requirements: 

* A user should be able to input an ICD-10-CM code (for example, “B05.9”) and have the program print a text description of the code (in this case, “Measles without complication”)

* If a user has an ICD-10-CM description (for example “Ebola virus disease”), the user can enter it and the program will print all possible related code values (here, it’s A98.4)

* Users that have only a partial ICD-10-CM code number or description should be able to enter it and the program will print a list of all potential descriptions or codes. This is useful when a common disease term, such as “diabetes”, can match many different codes. (In this instance, “diabetes” appears 478 times in the 2018 ICD-10-CM code list)

### Step 2. Building a GUI for the ICD-10-CM Lookup Application

The purpose of Step 2 is to create an actual graphic user interface (GUI) in Python for the ICD-10-CM query software which was created in Step 1.

The interface consists of a single window which contains some relevant widgets:

* A text entry area for the user to type in codes or descriptions

* A larger text area to place the results

* A button to run the query

* A button to clear what is in the widgets

* A button to quit the program
