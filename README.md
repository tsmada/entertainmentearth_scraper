# README #


### What is this repository for? ###

This project attempts to acquire the listings provided by entertainmentearth.com ee distributor search with a keyword of "a"

### How do I get set up? ###

#### Setup ####

This project can be easily deployed to OSX or Linux via the following method. We will use a "virtual environment" to hold our Python versions, etc so that we will not need to modify our system libraries/Python version. This project relies on the Scrapy.org framework.

OSX:

* Install brew
** Paste into terminal: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
* Install virtualenv
** Paste into terminal: pip install virtualenv
* Create virtualenv directory/project
** Navigate to top directory to contain virtual environment (I use ~/Projects) with terminal (cd ~/Projects) (mkdir ~/Projects if it doesn't already exist.)
** Paste into terminal: virtualenv entertainmentearth
** Navigate into this virtualenv directory (cd ~/Projects/entertainmentearth)
** Activate the virtualenv by pasting into terminal: source bin/activate
* Install scrapy by pasting into terminal: pip install scrapy
* Download the project to this current directory by pasting the following into terminal: git clone https://smada@bitbucket.org/smada/entertainmentearth.git
** Note: if you don't have git please install it by pasting the following into terminal: brew install git
** You should have a copy of the project now in your current directory.
* Navigate to the project directory by pasting the following into the terminal: cd entertainmentearth


### Running ###

Paste into terminal: scrapy crawl entertainmentearth -t csv -o output.csv

You will have an output file containing all the scraped items in CSV format.

* You will need to make sure you have activated your virtual env by navigating to the directory above in the setup and "sourcing" the activate binary. When done scraping you can simply issue the command "deactivate" to leave the virtualenv.

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact