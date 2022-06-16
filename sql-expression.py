from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Create varible for "Album" table
artist_table = Table(
    "Artist", meta, 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create varible for "album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Create varible for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String, ForeignKey("artist_table.Name")),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 -Select only name column from artist table
    # select_query = artist_table.select().with_only_columns(
    #    [artist_table.c.Name])

    # Query 3 - select only Queen from the artist table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")
    # Query 4 - select only by artistid #51 from the artist table

    # Query 5 - Select only the albums with artistid #51 on the album table

    # Query 6 - select all tracks where the composer is "Queen"
    #  from the track table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
