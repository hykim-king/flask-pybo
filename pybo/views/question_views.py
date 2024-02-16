# Created by user at 2024-02-15
from datetime import datetime

from flask import Blueprint, render_template,request,url_for
from werkzeug.utils import redirect

from pybo.models import Question
from pybo.forms import QuestionForm,AnswerForm
from .. import db

bp = Blueprint('question',__name__,url_prefix='/question')



@bp.route('/create',methods=('GET','POST'))
def create():
    form = QuestionForm()

    print(f'request:{request.method}')
    print(f'form.validate_on_submit:{form.validate_on_submit()}')
    #request method가 post이고 form이 submit()이면
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data,contents=form.contents.data,create_date=datetime.now())
        db.session.add(question)
        db.session.commit()

        print(f'main.index:{url_for('main.index')}')
        return redirect( url_for('main.index'))

    return render_template('question/question_form.html', form=form)

#/question/detail/1
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    print(f'question_id:{question_id}')
    #단건 조회
    question = Question.query.get_or_404(question_id)
    print(f'question:{question}')

    return render_template('question/question_detail.html',question=question, form=form)

#/question/list
#list는 파이썬 예약어
@bp.route('/list')
def _list():
    #질문 목록을 날짜 역순으로 출력
    #Question.create_date.asc()
    question_list=Question.query.order_by(Question.create_date.desc())

    #paging: http://127.0.0.1:5000/question/list?page=1
    page = request.args.get('page', type=int, default=1)
    print(f'page:{page}')

    question_list=question_list.paginate(page=page, per_page=10)


    '''
    question_list:SELECT question.id AS question_id, question.subject AS question_subject, question.contents AS question_contents, question.create_date AS question_create_date
    FROM question ORDER BY question.create_date DESC    
    '''

    print(f'question_list:{question_list}')

    #화면으로, question_list 데이터 전달
    return render_template('question/question_list.html',question_list=question_list)


