SELECT word,
       count(*) AS cnt
FROM
  (SELECT lower(unnest(string_to_array(string_agg(trim(regexp_replace(jobtitle, '[-,]', ' ', 'g')), ' '), ' '))) AS word
   FROM indeed) AS sub
WHERE length(word) > 3
GROUP BY 1
ORDER BY 2 DESC LIMIT 100;

