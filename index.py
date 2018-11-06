from flask import Flask, request, jsonify, render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import json, secrets, random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbad458706654a1bf4c4248f15bdf135'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
db = SQLAlchemy(app)

class Links(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    long_link = db.Column(db.String(255), nullable=False)
    short_link = db.Column(db.String(20), nullable=False)
    clicks = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return f"Links('{self.ids}','{self.title}','{self.long_link}',''{self.short_link}','{self.clicks}')"


# link2 = Links(title='Facebook',
#               long_link='https://www.jumia.com.ng/fashion-flat-tummy-waist-trainer-off-white-10298560.html',
#               short_link='kku.rl/12srted')
# db.session.add(link2)
# db.session.commit()

@app.route('/')
def index():
    Link = Links()
    pass_through = []
    data = Link.query.all()
    for each in data:
        link = {'id':each.ids,'title':each.title,'url':each.short_link,'clicks':each.clicks}
        pass_through = [link] + pass_through

    return(render_template('index.html', contents=pass_through))

@app.route('/shorten', methods=['POST'])
def shorten():
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    info = data_dic["values"]
    title = info[0]
    long_link = info[1]
    short_link = short_url()
    server = 'http://127.0.0.1:5000/'
    add_link = Links(title=title, long_link=long_link, short_link=server+short_link)
    db.session.add(add_link)
    db.session.commit()
    resp = {'message':'Link created', 'link':server+short_link}
    response = jsonify(resp)
    response.headers['Access-Control-Allow-Origin']='*'
    return response

@app.route('/<string:url>')
def url_locator(url):
    Link = Links()
    links = []
    server = 'http://127.0.0.1:5000/'+url
    data = Link.query.filter_by(short_link = server).all()
    for each in data:
        linked = {'id': each.ids, 'title': each.title,'url': each.long_link, 'clicks': each.clicks}
        links.append(linked)
    return redirect(links[0]['url'])


#function for creating random short link
def short_url():
    token = secrets.token_hex(16)[:7]
    new_token = ' '.join(token).split(' ')
    main_id = ''.join(random.sample(new_token, len(new_token)-1))
    return (main_id)

if __name__ == '__main__':
    app.run(debug=True)
