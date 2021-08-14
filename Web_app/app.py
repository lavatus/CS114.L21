from flask import Flask, render_template, request


import knn as clf



app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_word():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def predict_image():
    image_file=request.files["image_file"]
    image_path="./images/"+image_file.filename
    image_file.save(image_path)
    
    p=clf.prediction_Img(image_path)
    return render_template("show.html",prediction=p[0],hinhanh=p[3],location=p[1],para1=p[2][0],para2=p[2][1])



if __name__ =='__main__':
	app.run(debug = True)