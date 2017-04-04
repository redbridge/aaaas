#!/usr/bin/python

import os

from flask import Flask, Response
app = Flask(__name__)

fonts = ["banner", "big", "block", "bubble", "digital", "ivrit", "lean", "mini", "mnemonic", "script", "shadow", "slant", "small", "smscript", "smshadow", "smslant", "standard", "term",
]

@app.route("/ascii/<text>")
def aaaas(text):
    res = os.popen("figlet %s" % text).read()
    return Response(res, mimetype='text/plain')



if __name__ == "__main__":
    app.run(host="0.0.0.0")




