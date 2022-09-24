import csv
import os
import sqlite3

DB_DIR = os.path.join(os.getcwd(), 'db.sqlite3')
CSV_DIR = os.path.join(os.path.join(os.getcwd(), 'static'), 'data')


def import_one_file_csv_to_sqlite():

    con = sqlite3.connect(DB_DIR)
    cur = con.cursor()

    with open(os.path.join(CSV_DIR, 'users.csv'),
              'r',
              encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO users_customuser VALUES'
                + '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'genre.csv'),
              'r',
              encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_genre VALUES (?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'titles.csv'),
              'r',
              encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_title VALUES (?, ?, ?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'category.csv'),
              'r', encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_category VALUES (?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'genre_title.csv'),
              'r', encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_title_genre VALUES (?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'comments.csv'),
              'r', encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_comment VALUES (?, ?, ?, ?, ?)', row
            )

    with open(os.path.join(CSV_DIR, 'review.csv'),
              'r', encoding="utf8") as f_open_csv:
        rows = csv.reader(f_open_csv, delimiter=",")

        for row in rows:
            cur.execute(
                'INSERT INTO reviews_review VALUES (?, ?, ?, ?, ?, ?)', row
            )

    con.commit()
    con.close()


if __name__ == '__main__':
    import_one_file_csv_to_sqlite()
