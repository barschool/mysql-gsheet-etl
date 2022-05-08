SELECT j.id
, j.date_posted
, v.name
, a.country
, c.city world_city
, co.country world_country
FROM jobsite_job j
lEFT JOIN jobsite_venue v on v.id = j.venue_id
lEFT JOIN jobsite_address a on a.id = v.address_id
lEFT JOIN jobsite_worldcity c on c.id = a.world_city_id
lEFT JOIN jobsite_worldcountry co on co.id = a.world_country_id
LIMIT 10