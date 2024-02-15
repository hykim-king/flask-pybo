# Created by user at 2024-02-15

from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('question',__name__,url_prefix='/question')

#/question/detail/1
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    print(f'question_id:{question_id}')
    #단건 조회
    question = Question.query.get_or_404(question_id)
    print(f'question:{question}')

    return render_template('question/question_detail.html',question=question)

#/question/list
#list는 파이썬 예약어
@bp.route('/list')
def _list():
    #질문 목록을 날짜 역순으로 출력
    #Question.create_date.asc()
    question_list=Question.query.order_by(Question.create_date.desc())
    '''
    question_list:SELECT question.id AS question_id, question.subject AS question_subject, question.contents AS question_contents, question.create_date AS question_create_date
    FROM question ORDER BY question.create_date DESC    
    '''

    print(f'question_list:{question_list}')

    #화면으로, question_list 데이터 전달
    return render_template('question/question_list.html',question_list=question_list)


