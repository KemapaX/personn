from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/person_update', methods=['GET'])
def person_update():
    id = request.args.get("id")
    for i in model:
        if i.id_person == id:
            print(i.id_person, i.name, i.last_name)
            data = {
                'id': i.id_person,
                'name': i.name,
                'last': i.last_name
            }
    return render_template('person_update.html', value=data)


@app.route('/person_update', methods=['POST'])
def person_update_g():
    id_p = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    data = [i.id_person for i in model]
    print(data)
    for z in range(0, len(model)):
        if data[z] == id_p:
            pn = Person(id_person=id_p, name=first_name, last_name=last_name)
            model[z] = pn
            return render_template('person_detail.html', value=pn)


@app.route('/person_delete', methods=["GET"])
def delite():
    id = request.args.get("id")
    data = [i.id_person for i in model]

    for z in range(0, len(model)):
        if data[z] == id:
            del model[z]
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)