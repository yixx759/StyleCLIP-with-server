import PIL.Image
from flask import Flask, request,render_template, send_file
import Auto2



app = Flask(__name__)
start = False

@app.before_first_request
def before_first_request():
    global master
    master = Auto2.PlayInteractively()


def serve_pil_image(pil_img,saveto):
    print("here!!!!!!!!!!!!!!!")
    pil_img.save('./static/'+saveto+'.JPG', 'JPEG')
    img1 = PIL.Image.open('./data/ffhq/0.jpg')
    img1.save('./static/0.JPG', 'JPEG')

@app.route('/result')
def result():
    global master
    #master = Auto2.PlayInteractively()
    text = request.args.get('target')
    text2 = request.args.get('natural')
    num1 = request.args.get('strength')
    num2 = request.args.get('disentanglment')
    saveloc = request.args.get('save')
    print(text)
    master.text_n(text2)
    img2 = master.ChangeAlpha(num1)
    img2 = master.ChangeBeta(num2)
    img2 = master.text_t(text)
    print("22here!!!!!!!!!!!!!!!")
    serve_pil_image(img2, saveloc)
    master.SetInit()
    return render_template("hello.html")



# @app.route('/', methods=['GET','POST'])
# def index():
#     global start
#     global master
#
#
#     if request.method == 'POST':
#
#         text = request.form["text"]
#         text2 = request.form["neutral"]
#         num1 = request.form["Strength"]
#         num2 = request.form["Disentangle"]
#
#         print(text)
#         global img2
#
#         master.text_n(text2)
#         img2 = master.ChangeAlpha(num1)
#         img2 = master.ChangeBeta(num2)
#         img2 = master.text_t(text)
#         serve_pil_image(img2,1)
#         return render_template("hello.html")
#     if(start == False):
#         return render_template("hello.html")
#         start = True


# def serve_pil_image(pil_img):
#     img_io = BytesIO()
#     pil_img.save(img_io, 'JPEG', quality=70)
#     img_io.seek(0)
#     return send_file(img_io, mimetype='image/jpeg')
#
# @app.route('/')
# def index():
#     global master
#     img2 = master.text_t("blonde")
#     img2a = serve_pil_image(img2)
#     return img2a


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True, threaded=False)




