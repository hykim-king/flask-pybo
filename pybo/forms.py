# Created by user at 2024-02-16

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

#FlaskForm을 상속
class QuestionForm(FlaskForm):
    #StringField 글자수 제한이 있는 경우
    subject = StringField('제목', validators=[DataRequired('제목은 입력 필수 입니다.')])
    #TextAreaField 굴자수 제한이 없는 경우
    contents = TextAreaField('내용',validators=[DataRequired('내용은 필수 입력 항목 입니다.')])

#답변 등록 form
class AnswerForm(FlaskForm):
    contents = TextAreaField('내용',validators=[DataRequired('내용은 필수 입력 항목 입니다.')])