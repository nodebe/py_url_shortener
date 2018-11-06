from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

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



if __name__ == '__main__':
    app.run(debug=True)
