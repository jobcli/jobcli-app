CREATE OR REPLACE FUNCTION update_lastmodified()
RETURNS TRIGGER AS $$
BEGIN
    NEW.lastmodified = now();
    RETURN NEW;
END;
$$ language 'plpgsql';


