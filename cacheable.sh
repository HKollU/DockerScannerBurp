#!/bin/bash
curl -i -s -k -X $'GET' \
    -H $'Host: cora-vuetify-dev.herokuapp.com' -H $'Connection: close' -H $'sec-ch-ua: \";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"' -H $'Origin: https://cora-vuetify-dev.herokuapp.com' -H $'sec-ch-ua-mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Accept: */*' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: font' -H $'Referer: https://cora-vuetify-dev.herokuapp.com/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    -b $'XSRF-TOKEN=eyJpdiI6IlQyMmZhSGNmMTNlczU0T1NuT2xRamc9PSIsInZhbHVlIjoiMWZYd0I5TVI4UjZOc0xwRllQKytkaDhpXC9OZDhrMGJkeHlIZHBtSWFyYkpLd3ZsUmlraGdrdDh2Q0xaZnNsQ0QwcnZZVkhOamdacjhUNE1JS0tHT2RGWnhEMGNSYnBhYVlVOEtwTEtRd3pTajRrcE1cL3lTV1ozNmhDak5DWU5BQiIsIm1hYyI6Ijc3ZTFkMjZjODM4MDIyYjI1YTM2NjBhMjBhZTkzNTQ2ZmViZjY5ODg3Y2RiNWRlYjc5ZGU4ZTk2ODM4YzFiZDQifQ%3D%3D; laravel_session=eyJpdiI6Ilg4Q0JmU3JuS0ZWSzFuSXI0QkhYMnc9PSIsInZhbHVlIjoiXC82bTJrWlwvR0c0RWxRQlgzMFlFajVFaWFkMVZaRklwZVZXNnFKaUZkNENXYWRxSUI4WlRxN2NoNHArUXVxWjl0OTk1QmNKc3BlQ0VKaWc4alNqRzJCU2tFTUNxNGJDYmVISXowY0Z0Y2xTcEhZd0Fmc2k5OWtDODJKdVwvR2F4UVUiLCJtYWMiOiI0ZWFmOGQyMWQ5NTRlODg0Mzk5ZjQyY2YxNjdhMWU2YTgwMjRlNWZjMjE5Y2Q1MzVmNDk5Y2JjNjY3MWZmMjVjIn0%3D' \
    $'https://cora-vuetify-dev.herokuapp.com/fonts/vendor/@mdi/materialdesignicons-webfont.woff2?f1997a8aba8a498fe4032e3b56e871ca' >cache.txt && cat cache.txt
