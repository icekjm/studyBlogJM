from flask import Flask, Blueprint, request, render_template

#blueprint 클래스에 의한 blueprint객체 생성
#바로 아래코드의 의미는, blogJM이라는 객체를 생성하여 이 객체를 blog_abtest에 할당함.
# 결국 blog_abtest도 객체임
blog_abtest = Blueprint('blogJM', __name__)

#여기서부터 라우트 함수 등록시킴
@blog_abtest.route('/test')
def test():
    # return render_template('JDK_JRE_JVM.html')
    return render_template('String_StringBuilder_Buffer.html')