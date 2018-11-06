from flask import Flask, request, jsonify, render_template
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
        return f"links('{self.ids}','{self.title}','{self.long_link}',''{self.short_link}','{self.short_links}')"


# link2 = Links(title='Facebook',
#               long_link='https://www.jumia.com.ng/fashion-flat-tummy-waist-trainer-off-white-10298560.html',
#               short_link='kku.rl/12srted')
# db.session.add(link2)
# db.session.commit()

@app.route('/')
def index():

    return(render_template('index.html'))

@app.route('/shorten', methods=['POST'])
def shorten():
    rf = request.form
    for key in rf.keys():
        data = key
    data_dic = json.loads(data)
    info = data_dic["values"]
    title = info.title
    long_link = info.link
    short_link = short_url()
    server = 'http://127.0.0.1:5000/'
    add_link = Links(title=title, long_link=long_link, short_link=server+short_link)
    db.session.add(add_link)
    db.session.commit()

#function for creating random short link
def short_url():
    token = secrets.token_hex(16)[:6]
    new_token = ' '.join(token).split(' ')
    main_id = ''.join(random.sample(new_token, len(new_token)-1))
    return (main_id)

if __name__ == '__main__':
    app.run(debug=True)
