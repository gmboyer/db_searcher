# db_searcher

This is a tool to take a large csv and filter it down based on the user's criteria. Filtered data can be exported, joined with another csv, or plotted.

### Prerequisites

You will need Python 3.6 or higher installed on your machine. You will also need the following Python libraries:

- jupyter
- ipywidgets
- dfply
- pandas

### Installing

Click on the green button 'clone or download' and select 'download as ZIP'. When the download is finished, unzip the zipped 'db_searcher-master' folder somewhere.

Check to make sure Python 3.6 or higher is installed on your machine. Next, check the list of prerequisites in the "Prerequisites" section, above. If you know these libraries are already installed, skip ahead to the "Tutorial" section. If not, open your computer's command line and install them using conda if you are using Anaconda:

```
conda install ipywidgets
```

or pip if you are not using Anaconda:

```
pip install ipywidgets
```

Repeat this process until each of the prerequisite libraries is installed.

## How to open and run db_searcher

Open Jupyter notebooks using Anaconda (if it is installed) or by opening your computer's command line interface and entering:

```
jupyter notebook
```

A browser tab should open automatically to display the Jupyter interface. Use this interface to navigate to where you put db_searcher.ipynb and then open the notebook. Select 'Restart & Run All' from the 'Kernel' dropdown menu to run the notebook. The db_searcher interface should appear as output in the first cell.

## Tutorial with a test dataset

**Reading Data** Type ```data``` into the 'csv:' text box, then click the Search button. This should read the sample dataset included with db_searcher called data.csv and then display the first and last 30 entries of data.csv, a sample dataset included in the download. You should see all five columns included in data.csv; Sample, Year, Loc, Temperature, and pH. The csv you choose to read in db_searcher needs to be in the same directory as db_searcher.ipynb.

**Selecting** Choose Select from the 'condition' dropdown menu, then click the Add button. This will add a Select line. You can remove a line you just added by clicking the Remove button next to the line. While you have a Select line added, type ```Year, Sample, pH, Temperature``` into the Select text box and then click Search. This will select only the Year, Sample, pH, and Temperature columns and display them in that order. Be aware that db_searcher is case-sensitive, so check that you have the correct uppercase and lowercase letters if something goes wrong.

**Sorting** Choose Sort from the list of conditions and click Add. Type ```Year, pH``` in the resulting text box, then click Search. This will sort the data by year, then by pH.

**Filtering** Create a Filter line in the same way that you made Select and Sort lines. There will be two resulting text boxes. In the left box, type ```Temperature``` and in the right box enter ```<= 40```, then click Search. This will filter the data down to samples where the value for Temperature is less than or equal to 40. Try adding a second Filter line and then filtering pH values <2. Valid filtering criteria are ```<```, ```>```, ```<=```, ```>=```, and ```==``` (exact matches) for columns containing numeric data. For columns containing non-numeric data, db_searcher only recognizes ```==``` for filtering.

Try adding another Filter line and then selecting only entries with the value 2008 in the Year column. Note that there are no matches if you type ```== 2008``` as the filtering criteria. This is because some of the entries in the Year column are non-numeric (e.g. "2000 June"). Instead you will need to type ```== "2008"``` (with 2008 in quotes) to filter the Year column on the value 2008. This principle carries over to filtering any other non-numeric column.

**Plotting** Create a Plot line. Type ```pH, Temperature``` and click Search. This should display an xy-plot and a table of the filtered data.

**Joining** Create a Join line. In the first box, type ```data2```, which is the name of the second sample csv dataset included with db_searcher. Leave the join type as 'Inner', and type ```Sample``` as the column used to perform the join. Click Search. This will display the result of the join. In this case, the "Eh" column from data2.csv should now appear as a column in the displayed table. The csv you choose to join must be in the same directory as db_searcher.ipynb.

**Exporting** To export the displayed data table as a csv, first create an Export line and enter the name of the file you would like to export, then click Search. For instance, entering ```MyOutput``` will create MyOutput.csv in the same directory as db_searcher.ipynb.


## Author

* **Grayson Boyer** - [gmboyer](https://github.com/gmboyer)