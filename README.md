# PikabuFacesAggregator
App to store and provide information about [Pikabu website's](https://pikabu.ru/) articles that contain pictures with faces.

## Bringing up

1. Clone this project and go to the directory
```bash
git clone https://github.com/stupina/PikabuFacesAggregator.git && cd PikabuFacesAggregator
```

2. Add file "env_file" to the our root directory. Add to params to file:
```bash
DB_NAME=db_service_name_from_docker_compose_file
DB_PORT=db_external_port_from_docker_compose_file
```

3. Bring up the app
```bash
docker-compose up
```

4. Browse to [link](http://localhost:5000/articles) to see the app in action.

## Services

#### Parser
This service periodically (every 60 minutes) parses the website's articles and store them into the database.

#### API
This service retuns information about website's articles that contain pictures with faces. Too get information use endpoint **/articles**. Example:
```bash
curl -X GET http://localhost:5000/articles
```
