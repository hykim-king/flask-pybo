# Created by user at 2024-02-19
import os.path

from flask import Blueprint,url_for,render_template,flash,request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect


import matplotlib.pyplot as plt
from config import BASE_DIR
import uuid


bp = Blueprint('chart',__name__,url_prefix='/chart')
# UUID를 사용하여 고유한 파일 이름 생성
def generate_filename():
    unique_filename = str(uuid.uuid4())
    return unique_filename
@bp.route('/line',methods=('GET',))
def line():
    # 데이터 준비
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Matplotlib을 사용하여 차트 생성
    plt.plot(x, y)
    plt.xlabel('X축 라벨')
    plt.ylabel('Y축 라벨')
    plt.title('간단한 차트')

    print("-"*50)

    # 생성된 차트를 이미지 파일로 저장
    file_name = generate_filename()+'.png'
    STATIC_DIR = os.path.join(BASE_DIR, f'pybo\static\{file_name}')
    print(f' BASE_DIR:{BASE_DIR}')
    print(f' STATIC_DIR:{STATIC_DIR}')

    print("-" * 50)
    plt.savefig(STATIC_DIR)
    file_name = f'/static/{file_name}'
    plt.close()
    # 생성된 차트를 HTML 페이지에 출력
    return render_template('chart/line_chart.html',image_path=file_name)