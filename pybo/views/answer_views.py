# Created by user at 2024-02-15

from datetime import datetime
from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question,Answer

bp = Blueprint('answer',__name__,url_prefix='/answer')

@bp.route('/create/<int:question_id>',methods=('POST',))
def create(question_id):
    print('-'*50)
    print(f'question_id:{question_id}')
    print('-'*50)

    question = Question.query.get_or_404(question_id)

    #content
    #request : request객체는 플라스크 내장 객체, 브라우저 요청을 처리
    contents = request.form['contents']
    print(f'contents:{contents}')

    #답변등록
    answer=Answer(question=question, contents=contents, create_date=datetime.now())
    db.session.add(answer) #저장
    db.session.commit() #commit

    return redirect(url_for('question.detail',question_id=question_id))


