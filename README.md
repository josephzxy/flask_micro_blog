# flask_micro_blog

<img src="https://raw.githubusercontent.com/josephzxy/pic/master/Screen%20Shot%202018-07-25%20at%209.46.50%20AM.png" height=500>

flask_micro_blog is a microblog platform based on flask.

[Demo on AWS EC2](http://ec2-54-95-179-201.ap-northeast-1.compute.amazonaws.com:80)(Temporarily not accessbile due to Amazon free tier expiry)

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

## Running Test

All test cases are under `test/` and are based on [pytest](https://docs.pytest.org/en/latest/)

Test cases can be run by running `pytest` command at the root of project folder.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pipenv](https://docs.pipenv.org/) - Dependency Management


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

