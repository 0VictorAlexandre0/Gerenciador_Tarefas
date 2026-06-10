from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        
        nova_tarefa = request.form.get('nova_tarefa')

        tarefa = {
            'titulo': nova_tarefa,
            'status': 'Pendente',
            'prioridade': 'Alta'
        }

        tarefas.append(tarefa)

    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)