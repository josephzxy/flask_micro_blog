# flask_micro_blog

<img src="https://raw.githubusercontent.com/josephzxy/pic/master/Screen%20Shot%202018-07-25%20at%209.46.50%20AM.png" height=500>

flask_micro_blog is a microblog platform based on flask.

Basic Features:
- User can register, login, edit their profile, post microbblogs, explore new friends, follow other users, see microblogs post by their friends.
- Flask-bootstrap is used as front-end framework.

Advanced Features:
- User will have their own random Github-style default avatar generated using opencv-python.
 

## Getting Started
### Prerequisites
Pipenv is used to manage virtual env and packages.

Please refer to `Pipfile` for prerequistes.

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

- [on Linux](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
- [on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)
- [on Docker Container](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pipenv](https://docs.pipenv.org/) - Dependency Management


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

