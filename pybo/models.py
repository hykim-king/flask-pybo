# Created by user at 2024-02-14


from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True) #숫자
    subject = db.Column(db.String(200),nullable=False) #문자
    contents = db.Column(db.Text(),nullable=False) #오라클 CLOB
    create_date = db.Column(db.DateTime(),nullable=False) #날짜

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #fk생성:
    # ondelete='CASCADE' ->sql수행시 적용
    #question = db.relationship('Question',backref=db.backref('answer_set', cascade='all, delete-orphan'))
    question_id = db.Column(db.Integer,db.ForeignKey('question.id',ondelete='CASCADE'))
    question = db.relationship('Question',backref=db.backref('answer_set'))
    contents = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
