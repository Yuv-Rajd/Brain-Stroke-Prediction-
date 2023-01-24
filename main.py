import pickle
from flask import Flask,request,render_template

app =Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    # get the model
    model = pickle.load(open('randomforest_stroke_analysis.pkl', 'rb'))

    if request.method=='POST':

        # convert data to float
        name=request.form['name']
        gender=float(request.form['gender'])
        age=float(request.form['age'])
        hyp=float(request.form['hyp'])
        hrt=float(request.form['hrt'])
        mrd=float(request.form['mrd'])
        wrk=float(request.form['wrk'])
        res=float(request.form['res'])
        glc=float(request.form['glc'])
        bmi=float(request.form['bmi'])
        smk=float(request.form['smk'])

        data_input=[[gender,age,hyp,hrt,mrd,wrk,res,glc,bmi,smk]]
        print(data_input)

        # predict the data
        res =model.predict(data_input)

        # find res
        if res[0]==0:
            msg=f"{name}! dont worry you are all right"
        else:
            msg=f"Hey {name}! please contact your Doctor!"
        print(res)
        # return res msg
        return render_template('home-index.html',msg=msg)

    return render_template('home-index.html')


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')