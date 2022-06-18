# myrepo
    
    This repo is filled with all kinds of test projects. My own and from courses.
    
# restapi
    
### configuration

    install flask

### set virtual envirionment variables

    export FLASK_APP=player
    export FLASK_ENV=development

### run the application

    flask run


    Application will be running on:
        http://127.0.0.1:5000/

## implemented samples:

### Find single player:

        http://127.0.0.1:5000/player/?name=<name of player>

        Example:
        http://127.0.0.1:5000/player/?name=Cole Bardreau

        If you see this in the browser, this could apear as:
            http://127.0.0.1:5000/player/?name=Cole%20Bardreau

        Notice the name Cole%20Bardreau is url encoded because of the space

### joukkueet

        http://127.0.0.1:5000/player/joukkueet

### maat

        http://127.0.0.1:5000/player/maat
