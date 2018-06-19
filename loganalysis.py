#!/usr/bin/env python3

import psycopg2

articleQues = 'What are the most popular three articles of all time?'

article_query = """
    select articles.title, count(*) as views from articles
    join log on log.path = '/article/' || articles.slug
    group by articles.title,log.path
    order by views desc limit 3;
"""

authorQues = 'Who are the most popular article authors of all time?'

author_query = """
    select authors.name, count(*) as views from articles
    join authors on articles.author = authors.id
    join log on log.path = '/article/' || articles.slug
    group by authors.name order by views desc limit 4;
"""

errorQues = 'On which days did more than 1% of requests lead to errors?'

error_query = """
    select * from(select date(time),
    round(100.0*sum(case when status = '200 OK'
    then 0 else 1 end) / count(log.status),2)
    as e from log group by date(time)order by e desc) a where e > 1;
"""


def get_results(query):
    """Connects the database,executes query and gets result from database ."""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    db.close()
    return results


def print_results_articles(results):
    """Print query results for articles, fetched from the database ."""
    i = 1
    for result in results:
        print('(' + str(i) + ') \"' + result[0] + '\" with ' + str(result[1]) +
              " views")
        i += 1


def print_results_authors(results):
    """Print query results for authors, fetched from the database ."""
    i = 1
    for result in results:
        print('(' + str(i) + ') ' + result[0] + ' with ' + str(result[1]) +
              " views")
        i += 1


def print_results_errors(results):
    """Print error query results fetched from database ."""
    for result in results:
        print(result[0].strftime('%B %d, %Y') + " -- " + str(result[1]) +
              "% errors")


def get_article_query():
    """Gets and prints the top 3 articles ."""
    results = get_results(article_query)
    print('\n' + articleQues)
    print_results_articles(results)


def get_author_query():
    """Gets and prints the top 4 authors ."""
    results = get_results(author_query)
    print('\n' + authorQues)
    print_results_authors(results)


def get_error_query():
    """Gets and prints the days with more than 1% error ."""
    results = get_results(error_query)
    print('\n' + errorQues)
    print_results_errors(results)


if __name__ == '__main__':
    get_article_query()
    get_author_query()
    get_error_query()
