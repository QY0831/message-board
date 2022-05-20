from board import app, db
from models import Message
from forms import MessageForm
from flask import flash, redirect, url_for, render_template


@app.route('/', method=['GET', 'POST'])
def index():
    # load all messages from db
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        # if validate_on_submit() returns True,
        # means user submitted a valid form
        name = form.data.name
        body = form.data.body
        # generate Message obj
        new_message = Message(name=name, body=body)
        # write new message to db
        db.session.add(new_message)
        db.session.commit()
        # flash a message in website
        flash('Your message have been saved.')
        # redirect to index view
        return redirect(url_for('index'))
    # 未提交表格 -> 渲染含有所有message的主页
    return render_template('index.html', form=MessageForm, messages=messages)

