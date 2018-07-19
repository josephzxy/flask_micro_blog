# Project Title

flash_micro_blog

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Pipenv is used to manage virtual env and packages.

Pipfile
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "*"
flask-wtf = "*"
pymysql = "*"
flask-migrate = "*"
flask-sqlalchemy = "*"
flask-login = "*"
pytest = "*"

[dev-packages]

[requires]
python_version = "3.6"
```

### Installing

This project can be run by

```
$ export FLASK_APP=myblog.py 
$ flask run
```

`myblog.py` is under `flask_micro_blog/flask/`

After running it, you will see

<img src="https://raw.githubusercontent.com/josephzxy/pic/master/Screen%20Shot%202018-07-19%20at%202.57.49%20PM.png" height=300>

## Running the tests

To be continued

## Deployment

[on Linux](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
[on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)
[on Docker Container](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pipenv](https://docs.pipenv.org/) - Dependency Management


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This project is an outcome of [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
