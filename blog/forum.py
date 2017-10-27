# -*- coding: utf-8 -*-

import time
from flask import render_template, redirect, request, session
from blog import app
from blog.link2db import *


@app.route('/forum')
def set_forum():
    try:
        if session['logged_in']:
            posts = get_posts_recently()
            return render_template('/forum/forum.html', posts=posts)
    except:
        return redirect('/login')


@app.route('/forum/post/<int:order>', methods=['GET', 'POST'])
def set_post(order):
    pass  # TODO: implement the multi-users page and comment as POST method


@app.route('/forum/posts/write', methods=['GET', 'POST'])
def write_post():
    if request.method == 'GET':
        try:
            if session['logged_in']:
                return render_template('/forum/postPaste.html')
        except:
            return redirect('/login')
    title, lz, theme, content, plate = request.form['title'], session['nickname'], request.form['theme'], request.form['content'], request.form['plate']
    username = session['username']
    time_post = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    post_id = add_post(title, lz, theme, content, time_post, plate, username)
    return redirect('/posts/' + str(post_id))


@app.route('/forum/plates/<name>')
def set_plate(name):
    pass  # TODO: implement it like set_articles