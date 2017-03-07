'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request
from application import googlemap
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo
from flask_googlemaps import Map
from elasticsearch import Elasticsearch, RequestsHttpConnection
import random
import math

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'  
host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)




@application.route('/test', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EnterDBInfo(request.form) 
    form2 = RetrieveDBInfo(request.form) 
    
    if request.method == 'POST' and form1.validate():
        data_entered = Data(notes=form1.dbNotes.data)
        try:     
            db.session.add(data_entered)
            db.session.commit()        
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.data)
        
    if request.method == 'POST' and form2.validate():
        try:   
            num_return = int(form2.numRetrieve.data)
            query_db = Data.query.order_by(Data.id.desc()).limit(num_return)
            for q in query_db:
                print(q.notes)
            db.session.close()
        except:
            db.session.rollback()
        return render_template('results.html', results=query_db, num_return=num_return)                
    
    return render_template('index.html', form1=form1, form2=form2)


@application.route('/')
def map():
    # creating a map in the view
    number =1000
    locations = [
      [ -33.890542, 151.274856],
      [ -33.923036, 151.259052],
      [ -34.028249, 151.157507],
      [ -33.80010128657071, 151.28747820854187],
      [-33.950198, 151.259302]
    ];

    locations2 = [
        [42.503454, -92],
        [39.499633, -88]
    ];

    #tweet = es.get(index = 'twitter', doc_type = 'tweets', id = 1) 
    
    selected="sports"
    res = es.search(index="tweet", doc_type="tweetmap", q=selected)
    locationst=[]

        
    print("%d documents found" % res['hits']['total'])
    for doc in res['hits']['hits']:
            #print doc
        #print("%s) %s" % (doc['_id'], doc['_source']['text']))
        #print doc['_source']['coordinates']

        if doc['_source']['coordinates']:
            locationst.append(doc['_source']['coordinates'])



        # select a random coordinates    
        else:
            radius = 1113000.0                       #Choose your own radius
            radiusInDegrees=float(radius/111300)            
            r = radiusInDegrees
            
            #   UScenter = {lat: 40.461881, lng: -99.757229};
            x0 = 40.84
            y0 = -99.757229
         
            u = float(random.uniform(0.0,1.0))
            v = float(random.uniform(0.0,1.0))
            print u, v
            w = r * math.sqrt(u)
            t = 2 * math.pi * v
            print  w, t
            x = w * math.cos(t) 
            y = w * math.sin(t)
            print x, y
  
            xLat  = x + x0
            yLong = y + y0
            locationst.append((xLat, yLong))
    print locationst        
            
    
    

    return render_template('home.html', marker_list= locationst, count=number)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
