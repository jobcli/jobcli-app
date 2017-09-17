EXPLAIN
SELECT  'https://www.jobcli.com/ad/' || id                                                    AS url
      , (CASE WHEN length(jobtitle) <= 33 THEN jobtitle ELSE left(jobtitle, 30) || '...' END) AS title
      , (CASE WHEN length(company)  <= 33 THEN company  ELSE left(company , 30) || '...' END) AS company
      , regexp_replace(location, '\(.*\)|\d', '', 'g')                                        AS location
      , upper(conf_country)                                                                   AS country
FROM indeed
WHERE url_indeed IN
    ( SELECT url_indeed
      FROM indeed
      WHERE
          lower(conf_country) = lower('DE')
      AND jobtitle  @@ 'engineer'
      AND location  @@ 'berlin'
      AND list_text @@ 'angular'
      AND company   @@ 'sumup'
    );

