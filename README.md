# Log Analysis Project

This is the final project for Term 1 of Udacity's Fullstack Nanodegree Course.

## Setup
1. Install VirtualBox
2. Install Vagrant
3. Download or clone this [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
4. Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Unzip this file to extract newsdata.sql
6. Create a new directory inside the vagrant directory that exists in repo cloned in step 3
7. Place newsdata.sql in this newly created directory
8. Clone this repository and place its contents in the same directory.

## Run the project
1. Change directory to `fullstack-nanodegree-vm > vagrant`
2. Run `vagrant up` to start the virtual machine
3. Run `vagrant ssh` to log in
4. Run `cd .. ` twice to go back two steps in the file structure
5. Then run `cd vagrant`
6. By running `ls`, you will now be able to view the shared folders
7. `cd` into the directory that you made in step 6 of Setup
8. You now need to load the data. To do this, run `psql -d news -f newsdata.sql`
9. Once the data is loaded, you need to connect to it by runnning `psql -d news`
10. This project requires the creation of a view. 
    You can create it by running the following SQL statement:
    ```
    create view popularity as
    select articles.title, count(log.path), articles.author
    from log
    join articles on concat('/article/', articles.slug)=log.path
    group by articles.title, articles.author
    order by count desc;
    ```
11. Exit psql by entering `\q`
12. You can now run the queries using `python newsdata.py`

## Code description
The `newsadata.py` file consists of the following functions:
* `query_runner(query)` establishes the connection with the database, executes queries and returns the result. All the following functions call this function.
* `fetch_popular_articles()` constructs the query to answer the question **"What are the most popular three articles of all time?"**
* `fetch_popular_authors()` constructs the query to answer the question **"Who are the most popular article authors of all time?"**
* `fetch_error_days()` constructs the query to answer the question **"On which days did more than 1% of requests lead to errors?"**