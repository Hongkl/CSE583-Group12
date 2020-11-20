# Components Specification
## Components
### 1. Read and join different data
We need to download the King county’s covid data file and related data files in CSV format. And input those data into the Panda Frame. Since the data files are sorted by different time formats, we need to organize the data to make them synchronous. Then, we will join them and use the matplot package to make several plots about covid data and other data.
### 2. Data Visualization
After processing the data, we will use the Folium package to make some interactive maps.
### 3. Interface
After processing the data, we will use the Folium package to make some interactive maps.
## Interactions to accomplish use cases
Take our use case 2 for an example, users should first click a button on the page or type in their requirements to the input box to express their needs, which means our User Interface component should receive their inputs and transfer these inputs as different queries, and then send them to the Data Manager component. Once the Data Manager component receives these queries, it will return correct data subsets from tables and send them to the Visualization Manager component. After that, Visualization Manager will process these data and show them on the map or plot.
## Preliminary plan
#### 1. Collect Covid-19 data, CPI data, and unemployment rate data of the King county area
#### 2. Organize the data then join them together.
#### 3. Determine which python packages to build the interactive map and Panel to build the user interface.
#### 4. Create mapping visualizations comparing Covid-19 data to unemployment rate data and CPI data in the King county.
#### 5. Create a tool that allows the user to interact with the data.
#### 6. Implement the tool through testing