from flask_session import Session
from flask import Flask, render_template, redirect, request, session
from datetime import datetime
import sqlite3 as lite

app = Flask(__name__)
app.secret_key = 'Da_Sa_Bi_das'

app.config['SESSION_TYPE'] = 'filesystem'
app.config["SESSION_PERMANENT"] = False
Session(app)


@app.route("/")
def index():

    conn = lite.connect('mydatabase.db')
    db = conn.cursor()

    db.execute("SELECT * FROM professors ORDER BY name ASC")
    pros = db.fetchall()
    prosLen = len(pros)
    
    shoppingCart = []
    shopLen = 0
    totItems, total, display = 0, 0, 0
    if 'user' in session:
        db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])) )
        shoppingCart = db.fetchall()
        shopLen = len(shoppingCart)
        for i in shoppingCart:
            totItems += i[2]
            total += i[4]
        return render_template ("index.html", shoppingCart=shoppingCart, pros=pros, shopLen=shopLen, prosLen=prosLen, total=total, totItems=totItems, display=display, session=session )
    return render_template ( "index.html", shoppingCart=shoppingCart, pros=pros, shopLen=shopLen, prosLen=prosLen, total=total, totItems=totItems, display=display)


@app.route("/buy/")
def buy():

    conn = lite.connect('mydatabase.db')
    db = conn.cursor()

    qty = int(request.args.get('quantity'))
    if session:
        id = int(request.args.get('id'))
        db.execute("SELECT * FROM professors WHERE id ={}".format(id))
        goods = db.fetchall()
        if(goods[0][5] == 1):
            price = goods[0][6]
        else:
            price = goods[0][4]
        name = goods[0][1]
        image = goods[0][2]
        subtotal = qty * price
        db.execute(f"SELECT * FROM cart WHERE id = {id} and uid = {str(session['uid'])}")
        tmp = db.fetchall()
        if len(tmp) > 0:
            db.execute(f"UPDATE cart SET qty = qty + {qty} WHERE id = {id} and uid = {str(session['uid'])}")
            db.execute(f"UPDATE cart SET subtotal = subtotal + {subtotal} WHERE id = {id} and uid = {str(session['uid'])}")
        else:    
            db.execute("""INSERT INTO cart (id, qty, name, image, price, subtotal, uid) 
                                VALUES ({}, {}, '{}', '{}', {}, {}, '{}')""".format(id, qty, name, image, price, subtotal, str(session["uid"])))
        conn.commit()
        
        db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])))
        totItems, total, display = 0, 0, 0
        shoppingCart = db.fetchall()
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i][4]
            totItems += shoppingCart[i][2]
        db.execute("SELECT * FROM professors ORDER BY name ASC")
        pros = db.fetchall()
        prosLen = len(pros)
        return render_template ("index.html", shoppingCart=shoppingCart, pros=pros, shopLen=shopLen, prosLen=prosLen, total=total, totItems=totItems, display=display, session=session )


@app.route("/update/")
def update():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()
    
    qty = int(request.args.get('quantity'))
    if session:
        id = int(request.args.get('id'))
        db.execute("DELETE FROM cart WHERE id ={} and uid ={}".format(id, str(session["uid"])) )
        conn.commit()

        db.execute("SELECT * FROM professors WHERE id ={}".format(id))
        goods = db.fetchone()
        if(goods[5] == 1):
            price = goods[6]
        else:
            price = goods[4]
        name = goods[1]
        image = goods[2]
        subtotal = qty * price
        db.execute("""INSERT INTO cart (id, qty, name, image, price, subtotal, uid) 
                                VALUES ({}, {}, '{}', '{}', {}, {}, '{}')""".format(id, qty, name, image, price, subtotal, str(session["uid"])) )
        conn.commit()

        db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])) )
        totItems, total, display = 0, 0, 0
        shoppingCart = db.fetchall()
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i][4]
            totItems += shoppingCart[i][2]

        return render_template ("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems, display=display, session=session )


@app.route("/filter/")
def filter():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()
    if request.args.get('sale'):
        query = request.args.get('sale')
        db.execute("SELECT * FROM professors WHERE onsale = {} ORDER BY name ASC".format(query))
        pros = db.fetchall()
    if request.args.get('title'):
        query = request.args.get('title')
        db.execute("SELECT * FROM professors WHERE title = '{}' ORDER BY name ASC".format(query))
        pros = db.fetchall()
    if request.args.get('price'):
        query = request.args.get('price')
        db.execute("SELECT * FROM professors")
        pros = db.fetchall()
        tmp = []
        for i in pros:
            tmp.append(list(i))
        for i in tmp:
            if i[5] == 1:
                i = i.append(i[6])
            else:
                i = i.append(i[4])
        pros = sorted(tmp, key= lambda tmp:tmp[7])
    if request.args.get('id'):
        query = request.args.get('id')
        db.execute("SELECT * FROM professors WHERE id = {}".format(query))
        pros = db.fetchall()

    prosLen = len(pros)
    shoppingCart = []
    shopLen = 0
    totItems, total, display = 0, 0, 0
    if 'user' in session:
        db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])) )
        shoppingCart = db.fetchall()
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i][4]
            totItems += shoppingCart[i][2]
        return render_template ("index.html", shoppingCart=shoppingCart, pros=pros, shopLen=shopLen, prosLen=prosLen, total=total, totItems=totItems, display=display, session=session )
    return render_template ( "index.html", pros=pros, shoppingCart=shoppingCart, prosLen=prosLen, shopLen=shopLen, total=total, totItems=totItems, display=display)


@app.route("/checkout/")
def checkout():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()
    db.execute("SELECT * from cart WHERE uid={}".format(str(session["uid"])))
    order = db.fetchall()

    for item in order:
        db.execute("INSERT INTO purchases (uid, id, name, image, quantity) VALUES('{}', {}, '{}', '{}', {})".format(str(session["uid"]), item[5], item[1], item[0], item[2] ))
    conn.commit()

    db.execute("DELETE from cart WHERE uid={}".format(str(session["uid"])))
    conn.commit()

    return redirect('/')


@app.route("/remove/", methods=["GET", "POST"])
def remove():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()

    out = int(request.args.get("id"))
    db.execute("DELETE from cart WHERE id={}".format(out))
    conn.commit()

    
    db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])))
    totItems, total, display = 0, 0, 0
    shoppingCart = db.fetchall()
    shopLen = len(shoppingCart)
    for i in range(shopLen):
        total += shoppingCart[i][4]
        totItems += shoppingCart[i][2]
    display = 1
    return render_template ("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems, display=display, session=session )


@app.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/new/", methods=["GET"])
def new():
    return render_template("new.html")


@app.route("/logged/", methods=["POST"] )
def logged():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()
    user = request.form["username"].lower()
    pwd = request.form["password"]
    if user == "" or pwd == "":
        return render_template ( "login.html" )
    db.execute("SELECT * FROM users WHERE username = '{}' AND password = {}".format(user, pwd))
    rows = db.fetchone()
    if rows != None:
        session['user'] = user
        session['time'] = datetime.now()
        session['uid'] = str(rows[0])
    if 'user' in session:
        return redirect ( "/" )
    return render_template ( "login.html", msg="Wrong username or password." )


@app.route("/history/")
def history():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()

    totItems, total, display = 0, 0, 0
    db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])))
    shoppingCart = db.fetchall()
    shopLen = len(shoppingCart)
    for i in range(shopLen):
        total += shoppingCart[i][4]
        totItems += shoppingCart[i][2]
    db.execute("SELECT * FROM purchases WHERE uid={}".format(str(session["uid"])))
    pros = db.fetchall()
    prosLen = len(pros)
    return render_template("history.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems, display=display, session=session, pros=pros, prosLen=prosLen)


@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/")


@app.route("/register/", methods=["POST"] )
def registration():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()

    username = request.form["username"]
    password = request.form["password"]
    confirm = request.form["confirm"]
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    if password != confirm:
        return render_template("new.html", msg="Passwords did not match !!")
    db.execute( "SELECT * FROM users WHERE username = '{}' ".format( username ))
    rows = db.fetchall()
    if len( rows ) > 0:
        return render_template ( "new.html", msg="Username already exists!" )
    db.execute("select * from users")
    old = db.fetchall()
    db.execute ( "INSERT INTO users (id, username, password, fname, lname, email) VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(len(old)+1, username, password, fname, lname, email ))
    conn.commit()
    return render_template ( "login.html" )


@app.route("/cart/")
def cart():
    conn = lite.connect('mydatabase.db')
    db = conn.cursor()
    if 'user' in session:
        totItems, total, display = 0, 0, 0
        db.execute("SELECT * FROM cart WHERE uid={}".format(str(session["uid"])))
        shoppingCart = db.fetchall()
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i][4]
            totItems += shoppingCart[i][2]
    return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems, display=display, session=session)

@app.errorhandler(404)
def pageNotFound( e ):
    if 'user' in session:
        return render_template ( "404.html", session=session )
    return render_template ( "404.html" ), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
