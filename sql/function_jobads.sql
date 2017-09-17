-- function_jobads.sql
CREATE OR REPLACE FUNCTION api.ads
    ( country  TEXT
    , jobtitle TEXT
    , location TEXT
    , skills   TEXT
    , company  TEXT )

RETURNS TABLE ( url      TEXT
              , jobtitle TEXT
              , company  TEXT
              , location TEXT
              , country  TEXT )

AS $$

UPDATE indeed        AS i SET hit_cnt = hit_cnt + 1
FROM   published_ads AS p
WHERE i.id = p.id
    AND (CASE WHEN $1 != '' THEN p.country = upper($1)               ELSE TRUE END)
    AND (CASE WHEN $2 != '' THEN p.jobtitle  @@ sanitize_tsquery($2) ELSE TRUE END)
    AND (CASE WHEN $3 != '' THEN p.location  @@ sanitize_tsquery($3) ELSE TRUE END)
    AND (CASE WHEN $4 != '' THEN p.list_text @@ sanitize_tsquery($4) ELSE TRUE END)
    AND (CASE WHEN $5 != '' THEN p.company   @@ sanitize_tsquery($5) ELSE TRUE END)

RETURNING p.url_short
        , p.jobtitle_short
        , p.company_short
        , p.location_short
        , p.country;

$$ LANGUAGE SQL;


