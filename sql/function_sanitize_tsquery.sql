-- function_sanitize_tsquery.sql
CREATE OR REPLACE FUNCTION sanitize_tsquery(string TEXT)
RETURNS tsquery

AS $$

SELECT
    to_tsquery('english',
        regexp_replace(
            regexp_replace(
                replace(
                    trim(
                        regexp_replace(
                            $1, '[^a-zA-Z0-9, ]', '', 'g'
                        )
                    ),
                ',', ' | '
                ),
            ' +', ' & ', 'g'
            ),
        '\& \| \&', '|', 'g'
        )
    );

$$ LANGUAGE SQL;

