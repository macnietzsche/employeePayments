# ACME - Salary calculation
ACME has decided to develop an application to calculate the amount in USD to pay an employee, based on the quantity of hours and the time they worked. Therefore, the hour fee is calculated based in the table below:

| Time segments \ Day (Acronym)         | Monday (MO) | Tuesday (TU)  | Wednesday (WE)  | Thursday (TH) | Friday (FR) | Saturday (SA) | Sunday (SU) |
| :----:                | :----:      | :----:        | :----:          | :----:        | :----:      | :----:        | :----:      |
|00:01 - 09:00          |25           |25             |25               |25             |25           |30             |30           |
|09:01 - 18:00          |15           |15             |15               |15             |15           |20             |20           |
|18:01 - 00:00          |20           |20             |20               |20             |20           |25             |25           |

### Requirements
In order to run this application ```Python 3.7``` is required. No third-party libraries are needed. 

### Running the application
Before you run the aplication, you may want to register some data about your employees in ```employees_input.txt```. Make sure that the format of your entries is correct.

Input sample format: ```ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00```

Make sure you:
- Include a name
- Separate name and body with ```=```
- Include at least one day in the body. Use ```,``` to separate each day
- Take day acronyms from the table above.
- Separate start and end time values with ```-```
- Insert valid time values: ```from 00:01 to 24:00```

To run the aplication, execute this in your terminal: ```$ python src/app.py```

## For administrators
At the moment, payment fees are calculated based in the table at the top. If these rules are changed, please refer to ```config/payment_settings.json``` and update the JSON file according to the new rules.

Make sure that time segments:
- Do not overlap.
- Fill all day without leaving time gaps. Must fill ```from 00:01 to 24:00```
- Have valid time values

## Structure Overview
The following chart shows the basic the behavior of the application.
<p align="center">
<img src="employeePaymentsFlow.png" width='700'>
</p>

### Payment Handler

### TIme Interval Handler

### Input handler



## Testing
### Run the tests
```console
$ python -m pytest
```
Eleven tests have been written in order to test domains, subdomains (units), services, and integrations.
