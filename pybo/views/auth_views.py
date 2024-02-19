# Created by user at 2024-02-19

from flask import Blueprint,url_for,render_template,flash,request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm
from pybo.models import User

bp = Blueprint('auth',__name__,url_prefix='/auth')

#GET: 화면 등록 화면
#POST : 회원가입 저장
@bp.route('/signup',methods=('GET','POST'))
def signup():
    form = UserCreateForm()

    #회원가입 저장
    if request.method == 'POST' and form.validate_on_submit():
        #사용자가 존재 하는지 확인
        # email중복 체크
        user = User.query.filter_by(email=form.email.data).first()
        print('-' * 50)
        print(f'username:{form.username.data}')
        print(f'password1:{form.password1.data}')
        print(f'generate_password_hash:{generate_password_hash(form.password1.data)}')
        print(f'email:{form.email.data}')
        print('-' * 50)
        print(f'user:{user}')

        if not user:


            user=User(username=form.username.data,
                      password=generate_password_hash(form.password1.data),
                      email = form.email.data)
            #db저장, commit
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash(f'이미 존재하는 사용자 입니다.({user.username})')

    return render_template('auth/signup.html',form=form)