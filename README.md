# CSE583-Group12
Team Member: Hongkuan Lin, Jinghao Zhang, Jing Cao, Dingyu Zhang
[![Build Status](https://travis-ci.org/Hongkl/CSE583-Group12.svg?branch=main)](https://travis-ci.org/Hongkl/CSE583-Group12)
[![Coverage Status](https://coveralls.io/repos/github/Hongkl/CSE583-Group12/badge.svg)](https://coveralls.io/github/Hongkl/CSE583-Group12)

### COVID-WA
COVID-WA is a python base visuallization tool that built on top of pandas, folium and panel packages. It generates a web interface for users to easily visualize the COVID19 and unemployment data for Washington State. Users can simply click on bottoms to visualize different data for various demands.


### Background:
So far, more than 50 million people have been infected COVID-19 worldwide, but we know: with the joint efforts of people, we will eventually overcome this pandemic. As graduate students in UW, we really care about how COVID-19 affects our community especially in the Washington State area. If in the future we want to look back on those past days and learn how it impacted our daily life, we need a tool to help us better visualize those data.  
For this reason, our project aims to provide a web-based visualization tool. We are going to combine COVID-19 dataset with Unemployment Rate data to show its impact on every counties in Washington State intuitively.
Our project includes an interactive map from which users can check the history data for different counties in Washington State and make a comparison between different areas.  


### Installation
To install COVID-WA perform following steps:

1. Download and install Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
2. Clone the repo: https://github.com/Hongkl/CSE583-Group12.git
3. Create a new conda environment for this tool: conda env create -f environment.yml
4. Activate the new environment: conda activate myenv
5. Open COVID-WA folder and run the code in command line: python CovidWeb.py

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

