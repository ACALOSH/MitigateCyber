# MitigateCyber
coding test for mitigate

----VIRTUAL ENVIRONMENT---- This program can be run through a virtual conda environment. conda can be installed here : https://docs.anaconda.com/anaconda/install/ Once installed open terminal and type `conda --version` to confirm its been properly downloaded

To create a new virtual environment type "conda create -n testenv python=3.9 sqlite" this will create a new enviornment called testenv to activate this enviornment type ` conda activate testenv `
When done with this program, type `conda deactivate testenv`

----PROGRAM---- Now that your virtual environment has been activated, navigate to the downloaded folder with the files from the github page using terminal command "cd" from this folder, you can activate the program using the prompt `$ python main.py FUNCTION`

-Methods-

```$python main.py list```
  -shows a list of current tasks in database. tasks consists of (message, status, start time, end time).

```$python main.py create "task message"```
  -creates a task in database with the message "task message" and adds it to database, these tasks will be running until the stop method is called

```$python main.py update ID# "updated message"```
  -updates a task with id = ID# in database to have the new message "updated message"

```$python main.py delete ID# ```
  -deletes task with id = ID# from the database

```$python main.py stop ID#```
  -stops task with id = ID#, sets status to "stopped" if task was running and updates end time to current time.

---Test--- Note: Tests should be done with the database clear of entries

To run the tests, run "$ python test.py"
