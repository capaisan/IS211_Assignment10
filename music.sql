CREATE TABLE Artist (
  name TEXT PRIMARY KEY
);

CREATE TABLE Album (
  name TEXT,
  artist TEXT,
  PRIMARY KEY (name, artist),
  FOREIGN KEY (artist) REFERENCES Artist(name)
);

CREATE TABLE Song (
  name TEXT,
  album TEXT,
  artist TEXT,
  track_number INTEGER,
  duration INTEGER,
  PRIMARY KEY (album, artist, track_number),
  FOREIGN KEY (album, artist) REFERENCES Album(name, artist)
);
