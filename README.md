# CSE583-Group12
Team Member: Hongkuan Lin, Jinghao Chen, Jing Cao, Dingyu Zhang
[![Build Status](https://travis-ci.org/Hongkl/CSE583-Group12.svg?branch=main)](https://travis-ci.org/Hongkl/CSE583-Group12)
[![Coverage Status](https://coveralls.io/repos/github/Hongkl/CSE583-Group12/badge.svg)](https://coveralls.io/github/Hongkl/CSE583-Group12)

### COVID-WA
COVID-WA is a python base visuallization tool that built on top of pandas, folium and panel packages. It generates a web interface for users to easily visualize the COVID19 and unemployment data for Washington State. Users can simply click on bottoms to visualize different data for various demands.


### Background:
The (COVID-19) pandemic has created both a public health crisis and an economic crisis in the United States. The pandemic has disrupted lives and created a global economic slowdown. As of December, 2020, there have been more than 15 million confirmed COVID19 cases in the United State, and more than 195 thousand cases in Washington State.  
On the other hand. The labor market devastation caused by this pandemic has been the quickest and most severe in recent U.S. history. Many firms reacted to the COVID-19 pandemic by reducing their operations. So many people have lost their jobs during the COVID19 pandemic. The unemployment rate has fallen sharply from a record high of 14.7% in April. but is still 3.2 percentage higher than it was in February, which is before the covid19 struck the US.  
As graduate students in UW, we really care about how COVID-19 affects our community. There are many datasets online but most of them are independent. It is hard to connect one data with the other. For this reason, the goal of out project is to provide a web-based visualization tool for users to better visaualize those data. We are going to combine COVID-19 dataset with Unemployment Rate data to show how infection ratio impacted on every county in Washington State.
 


### Installation
To install COVID-WA perform following steps:

1. Download and install Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
2. Clone the repo: https://github.com/Hongkl/CSE583-Group12.git
3. Create a new conda environment for this tool: conda env create -f environment.yml
4. Activate the new environment: conda activate myenv
5. Open COVID-WA folder and run the code in command line: python CovidWeb.py  

After running the CovidWeb.py, the web will pop up automaticaly showed as below:


![](demo/dashboard.png?raw=true)

### Project Directory Structure
```
CSE583-Group12/
  |- COVID-WA/
  |- data/
     |- COVID19/
        |- COVID19-Rate.csv
        |- COVID19-Month with geo data.csv
        |- ...
     |- Unemployed/
        |- Unemployment.csv
        |- laucntycur14.xlsx
     |- WA_County_json/
        |- Adams.json
        |- Asotin.json
        |- ...
     |- WA_County_Boundaries.geojson
  |- doc/
     |- component_spec.md
     |- functional_spec.md
  |- example/
     |- Unemployment_popup.ipynb
     |- Untitled.ipynb
     |- kingCounty.csv
     |- kingCounty.json
     |- matplot.ipynb
     |- mergeFile.ipynb
     |- test.html
  |- tests/
     |- __init__.py
     |- test_covid.py
  |- .coveragerc
  |- .travis.yml
  |- LICENSE
  |- README.md
  |- environment.yml
  |- setup.py
```
### Project Data
Datasets from wa.gov and bls.gov.  
* Unemployment data: https://www.bls.gov/lau/#data
* COVID data: https://www.doh.wa.gov/Emergencies/COVID19/DataDashboard

