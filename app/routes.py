from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    send_from_directory,
    jsonify,
)
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        mbti_result = request.form.get("mbti_result")
        if mbti_result:
            if current_user.is_authenticated:
                current_user.mbti_type = mbti_result
                db.session.commit()
            flash("您的MBTI类型已保存成功", "success")
            return redirect(url_for("main.result"))
    return render_template("quiz.html")


@bp.route("/result")
def result():
    return render_template("result.html")


@bp.route("/characters")
def characters():
    return render_template("characters.html")


@bp.route("/relationships")
def relationships():
    return render_template("relationships.html")


@bp.route("/animals")
def animals():
    return render_template("animals.html")


@bp.route("/insights")
def insights():
    return render_template("insights.html")


@bp.route("/history")
@login_required
def history():
    return render_template("history.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/save_mbti", methods=["POST"])
def save_mbti():
    data = request.get_json()
    mbti_result = data.get("mbti_result")

    if not mbti_result:
        return jsonify({"success": False, "message": "Invalid MBTI result"})

    if current_user.is_authenticated:
        current_user.mbti_type = mbti_result
        db.session.commit()

    return jsonify({"success": True})


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory("static/mbti", "ISFP.ico")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(display_name=form.display_name.data, username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("恭喜，您已成功注册！")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("用户名或密码错误")
            return redirect(url_for("main.login"))
        login_user(user)
        return redirect(url_for("main.home"))
    return render_template("login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
