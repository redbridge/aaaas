#!/usr/bin/python

import os

from redis import Redis

r = Redis(host="redis")

from flask import Flask, Response
app = Flask(__name__)

fonts = ["banner", "big", "block", "bubble", "digital", "ivrit", "lean", "mini", "mnemonic", "script", "shadow", "slant", "small", "smscript", "smshadow", "smslant", "standard", "term",
]

@app.route('/<secret>/<font>/<text>')
def fancy(secret, font, text):
    if not font in fonts:
        return "only these fonts are allowed: %s" % ", ".join(fonts)
    else:
        if r.get(secret):
            r[secret] = int(r[secret]) + 1
        else:
            r[secret] = 1
        res = os.popen("figlet -f %s %s" % (font, text)).read()
        return Response(res, mimetype='text/plain')

@app.route('/billing')
def billing():
    rows = ["%s: %d" %(x, int(r[x])) for x in r.keys()]
    res = "\n".join(rows)
    return Response(res, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0")




