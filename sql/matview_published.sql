drop materialized view if exists published_ads;
create materialized view published_ads as
    select
          to_tsvector('english', jobtitle)   as jobtitle
        , to_tsvector('english', location)   as location
        , to_tsvector('english', list_text)  as list_text
        , to_tsvector('english', company)    as company
        , id                                 as id
        ----------------------------------------------------------------------------------------------------------
        , upper(conf_country)                                                                    as country
        , (CASE WHEN length(jobtitle) <= 33 THEN jobtitle ELSE left(jobtitle, 30) || '...' END)  as jobtitle_short
        , (CASE WHEN length(company)  <= 33 THEN company  ELSE left(company , 30) || '...' END)  as company_short
        , regexp_replace(location, '\(.*\)|\d', '', 'g')                                         as location_short
        , 'https://www.jobcli.com/ad/' || id                                                     as url_short

    from indeed
    where is_published;

create index published_search_idx on published_ads using GIN (jobtitle, location, list_text, company);
create index published_country_idx on published_ads (country);
create index published_id_idx on published_ads (country);
