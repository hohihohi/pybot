# pybot: python slack bot template

* use [slackbot](https://github.com/lins05/slackbot) library

## How to set up

* Requirements
    - docker

    ```shell
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    ```

* Install 
    1. Please `git colne` this repository
    2. Move project root path
    3. Create env file
        - `export API_TOKEN=*** > .env`
    4. Build docker file
        - `docker-compose build`
    5. Start application by docker
        - `docker-compose up -d`
    6. Try to run some commands
