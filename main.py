 from flask import Flask 
from caesar import rotate_string
from vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
app = Flask(__name__)

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form id="cipher_caesar" method="POST">
      <textarea name="text" ></textarea>
        <input value="0" label = "Rotate by:" type="text" name="rot"  >
        </input>
         <button>Submit Query</button>
    </body>
</html>
@app.route('/')
def index(): Return form
    return render_template('form.html', ciphertext='', rot=0, key='', decrypt_hide=True)


@app.route('/', methods=['POST'])

def encrypt():

    try:
        decrypt_pressed = bool(request.form['decrypt'])
    except KeyError:
        decrypt_pressed = False
    text = request.form['plaintext']
    rot = int(request.form['rot'])
    key = request.form['key']
    method = request.form['encrypt-method']
    if not decrypt_pressed:
        cipher = caesar_encrypt(text, rot) if method == 'caesar' else vigenere_encrypt(text, key)
    else:
        cipher = caesar_encrypt(text, abs(26-rot)) if method == 'caesar' \
            else vigenere_decrypt(text, key)
    return render_template('form.html', ciphertext=cipher, rot=rot, key=key,
                           decrypt_hide=decrypt_pressed, last_method=method)

app.run(debug=True)