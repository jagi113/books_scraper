CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE books (
  	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    slug VARCHAR (400),
    title VARCHAR (400),
	author VARCHAR (2000),
	url VARCHAR (800),
	image VARCHAR (800),
	price NUMERIC(5,2),
    status TEXT,
	description TEXT,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (slug, author)
);

CREATE OR REPLACE FUNCTION set_created_at()
  RETURNS TRIGGER AS $$
  BEGIN
    NEW.created_at = NOW();
    RETURN NEW;
  END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_created_at_trigger
  BEFORE INSERT ON books
  FOR EACH ROW
  EXECUTE FUNCTION set_created_at();