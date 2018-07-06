import datetime
import psycopg2

DBNAME = "news"


def query_runner(query):
    # All queries can be run through this method
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def fetch_popular_articles():
    query = "select title, count from popularity limit 3;"
    result = query_runner(query)

    print("\nMost popular three articles of all time: ")

    for article in result:
        print("\""+article[0]+"\""+" - "+str(article[1])+" views")


def fetch_popular_authors():
    query = """
    select authors.name, sum(count)
    from popularity
    join authors on authors.id=popularity.author
    group by authors.name
    order by sum desc;
    """
    result = query_runner(query)

    print("\nMost popular authors of all time: ")

    for author in result:
        print(author[0]+" - "+str(author[1])+" views")


def fetch_error_days():
    query = """
    select total.date,
    (cast(error_req as float)*100/total_req)
    as error_percent from
    (select date_trunc('day',time) as date,
    count(*) as total_req
    from log
    group by date
    ) as total join (
    select date_trunc('day',time) as date,
    count(*) as error_req
    from log
    where status='404 NOT FOUND'
    group by date) as errors
    on total.date=errors.date
    where (cast(error_req as float)*100/total_req)>1;
    """
    result = query_runner(query)
    print("\nDays when more than 1% of requests lead to errors: ")
    for day in result:
        print(str(day[0].strftime('%B %d, %Y'))+" - " +
              str(round(day[1], 2))+"%")

fetch_popular_articles()
fetch_popular_authors()
fetch_error_days()
