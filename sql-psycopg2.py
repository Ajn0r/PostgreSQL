import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 -Select only name column from artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only Queen from the artist table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Test"])

# Query 4 - select only by artistid #51 from the artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [115])

# Query 5 - Select only the albums with artistid #51 on the album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [115])

# Query 6 - select all tracks where the composer is "Queen"
#  from the track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connections
connection.close()

# print result
for result in results:
    print(result)
