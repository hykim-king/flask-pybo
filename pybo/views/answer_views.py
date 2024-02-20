# Created by user at 2024-02-15
import functools
from datetime import datetime
from flask import Blueprint, url_for, request,render_template,g
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question,Answer
from ..forms import AnswerForm

bp = Blueprint('answer',__name__,url_prefix='/answer')

#로그인 필수 처리 데코레이터 : @login_required
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        #login여부 check
        if g.user is None:
            _next =request.url if request.method == 'GET' else ''
            print(f'_next:{_next}')
            return redirect(url_for('auth.login',next=_next))

        return view(*args, **kwargs)

    return wrapped_view


@bp.route('/create/<int:question_id>',methods=('POST',))
@login_required
def create(question_id):
    print('-'*50)
    print(f'question_id:{question_id}')
    print('-'*50)

    form = AnswerForm()

    question = Question.query.get_or_404(question_id)

    #content
    #request : request객체는 플라스크 내장 객체, 브라우저 요청을 처리

    if form.validate_on_submit():
        contents = request.form['contents']
        print(f'contents:{contents}')

        #답변등록
        answer=Answer(question=question, contents=contents, create_date=datetime.now(),user=g.user)
        db.session.add(answer) #저장
        db.session.commit() #commit
        return redirect(url_for('question.detail',question_id=question_id))


    return render_template('question/question_detail.html',question=question, form=form)


