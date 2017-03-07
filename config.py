# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:0138682812@flasktest.cmj2ykxs7wep.us-west-2.rds.amazonaws.com:3306/flaskdb'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'


GOOGLEMAPS_KEY= 'AIzaSyBgNb27RKUVI8RM5br4xOMDVAWA6tS7dTw' 

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '838110956660080641-HTzfzOvyVLfMNiMwMaAkn9xMBtQUEVk'
ACCESS_SECRET = 'euVN5HZsIBJttx5JgrxbiBcVKdm4KqdC12FSmEX2GOKSt'
CONSUMER_KEY = 'KMUioXv68EVY2hi4wsjbQhJ7n'
CONSUMER_SECRET = 'euVksyfB0hmm0Xc92GPoq8bH8ZHhYD4SPhh0FpettqCSpGHefi'