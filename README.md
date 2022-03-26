# Elementor Assignment

### General Explanation
Implementation of site data analysis contains several parts
- Read list of sites from provided source (in this case CSV file)
- Perform API call for each site to retrive analysis information
- Perform analysis and create as a result data structure with analysis results for future process
- Output of analysis result (implementation can be different base in needs)

### Code structure

There are several directories and modules:
- configuration - contains configuration file
  - config.py - contains configuration data for a process
- data - files with a list 
  - request1.cvd - contains list file to check
- dataanalysis - contains files that define process of data analysis
  - requestanalysis.py - module that define object to analyze response received from Total Virus API
- totalvirusapi - contains files related to Total Virus API logc
  - apicall.py - module with functionality relevant to call Total Virus API

- appflow.py - this module contains function that orchestrate process flow
- app.py - application starting point

More comments dan be found inside code

###Installation
run pip install -r requirements.txt

### Recommendation to improve process
- To speed up process can be made as parallel execution or by creating data stream application
- Add logger
- Use proper exception handling
- Implement save into database (didn't have enough time to do it). The basic structure is ready. Can be by saving data structure using sqlalchemy




