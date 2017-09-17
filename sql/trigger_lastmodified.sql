CREATE TRIGGER update_indeed_lastmodified BEFORE UPDATE ON indeed FOR EACH ROW EXECUTE PROCEDURE update_lastmodified();
