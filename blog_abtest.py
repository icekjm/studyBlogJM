from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
import os

# https 만을 지원하는 기능을 http 프로토콜에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'kjm_server'

#blog.py 파일에서 생성한 blueprint객체를 등록시킴
#blog.blog_abtest에서 blog는 blog.py를 의미하며, blog_abtest는 blog.py안에 존재하는 blog_abtest임
app.register_blueprint(blog.blog_abtest, url_prefix='/blog')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id): #user_id로 로그인하면 세션DB에서 사용자 정보를 찾아서 이를 객체로 리턴한다.
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401) #success=False는 딕셔너리 형태로 {'success' = 'False}써도 된다.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)