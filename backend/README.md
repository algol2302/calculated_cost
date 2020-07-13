# calculated cost

## Design

* The file `tarif.json` saves to redis. For big json files it's required 
something like sentinel (see https://redis.io/topics/sentinel)
* All requests logs to PostgreSQL.
* There are `prod.env` and `local.env` (of course it unsafe, but for studying it's ok)

## To run the app just clone the repo and enter:
```
docker-compose up
```

## Openapi schema:

http://localhost/docs

## Register a new user

http://localhost/docs#/auth/register_api_v1_auth_register_post

``` json
{
  "email": "test@test.com",
  "password": "123456"
}
```

and get JWT token like:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNGZkMzQ3N2ItZWNjZi00ZWUzLThmN2QtNjhhZDcyMjYxNDc2IiwiYXVkIjoiZmFzdGFwaS11c2VyczphdXRoIiwiZXhwIjoxNTg3ODE4NDI5fQ.anO3JR8-WYCozZ4_2-PQ2Ov9O38RaLP2RAzQIiZhteM
```

## Request for calculating cost

http://localhost/api/v1/

Request body:
```json
{
  "date": "2020-07-01",
  "cargo_type": "Glass",
  "declared_value": 100
}
```

Authorization: 
``` 
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNGZkMzQ3N2ItZWNjZi00ZWUzLThmN2QtNjhhZDcyMjYxNDc2IiwiYXVkIjoiZmFzdGFwaS11c2VyczphdXRoIiwiZXhwIjoxNTg3ODE4NDI5fQ.anO3JR8-WYCozZ4_2-PQ2Ov9O38RaLP2RAzQIiZhteM
```

Success reponse:
```
{
  "calculated_cost": 3.5
}
```

## TODO

* Update `gunicorn_run.sh` and `gunicorn_conf.py` for prod envs
* Optimize `tarif.json` loading
* Clean up file structure
* Add tests