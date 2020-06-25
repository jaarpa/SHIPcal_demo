# SHIPcal_demo

This is a functional django front-end demo to be used with the simulation engine [SHIPcal](https://github.com/mfrasquet/SHIPcal). This front-end will allow you to visually perform simulations of solar heat for industrial processes and see the results in matter of seconds.

## Installation

You want to have a enviroment manager. Using conda will make the instalation easier; get conda with python 3 from [anaconda](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). You could another enviroment manager as pipenv or venv. You may also find useful to use get [Git](https://git-scm.com/downloads). Nevertheless the only true requirement is to have python 3 and pip installed.

### Get the project
First, move to your working directory and clone this repository. Download the *.zip file or clone it using git
```
git clone https://github.com/jaarpa/SHIPcal_demo.git
```
The previous command will create a folder called `SHIPcal_demo` move inside of it and clone the `SHIPcal` repository
```
cd SHIPcal_demo
git clone https://github.com/mfrasquet/SHIPcal
cd ..
```
now you have a full copy of the project in your local machine.

### Insall the dependencies.

The SHIPcal_demo project ships a `requirements.txt` and a `enviroment.yml` which will assist you to configure all the required packages.
#### Conda installation

If you have conda installed it is only matter to run from the terminal

```
conda env create -f environment.yml
conda activate SHIPcal_demo
```
and you are ready to go!. Just run 
```
python manage.py runserver
```
and type `localhost:8000` in your preferred web browser.

#### Otherwise

If you are using a different enviroment manager different to conda or no enviroment manager at all you can similarly run in the virtual enviroment (if you have any) in your terminal
```
pip3 install -r requirements.txt
```
and you would be ready to go!. Just run 
```
python manage.py runserver
```
and type `localhost:8000` in your preferred web browser.

Nevertheless this method is more likely to fail and you would have to try to install each package manually (don't worry there are not that many).

## Usage tutorial
There are a few things that are region/user dependent in the simulations (e.g. the locations, fuels, collectors) you can feed SHIPcal with the information to simulate any of these (and you have to in order to perform any simulation).

### Add a new location

Go to the navigation menu, under Add>New location to open the new location form.

Yo must fill out the form with the correct data and upload a typical meteorological year (TMY) file of the location in order to get an accurate simulation. `SHIPcal_demo` already has a TMY example that you can use to feed the database, this file is located in `SHIPcal_demo/Celaya.dat` . You can add it as follows:

Finally click the save button and the location will be loaded to the database (it might take a couple of seconds).

### Add a new fuel

Go to the navigation menu, under Add>New fuel to open the new fuel form.

Add the name of the fuel, say Gas LP. SHIPcal works internally using kWh, that's why you should provide the conversion factors from any other fuel unit into kWh, for example 1 kWh is equivalent to 0.08 kg of GLP then you fill in 0.08 kg/kWh and click the add button. Add as many conversion factors as you know. 

You should add the equivalence of CO2 ton per unit too, the available units are the same that you have added before. This wil be useful to calculate how much CO2 is saved.

Click the Create button to make this fuel available for simulation.

### Add a collector

Coming soon, currently only a default collector is supported. Make a pull request!

### Simulate

Once you have added a location, fuels, and collectors, you are ready to simulate!
Go to Simulate in the navigation menu and fill up the form with the data for the simulation and click the simulate button. In a few seconds you would be redirected to the results.

## TODO
- [ ] Functionality to add new collectors
- [ ] Translations
- [ ] Update/Delete fuels view
- [ ] Update/Delete locations view
- [ ] Update/Delete simulation view
- [ ] Results view to get previous simulation results.
- [ ] PDF generation report
