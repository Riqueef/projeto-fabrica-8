from flask import Flask, render_template, url_for

app = Flask(__name__)

# Dados de pacientes
pacientes = [
    {
        "id": 1,
        "nome": "Gabriel Vasco",
        "idade": 16,
        "condicao": "Diabetes Tipo 1",
        "image": "https://media.licdn.com/dms/image/v2/C4E03AQF_LRKSwl9ePw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1655207311456?e=1763596800&v=beta&t=e5AJvHjkG53gBdJtdz63eUp_cD7HTsXInek6lwJrAO0"
    },
    {
        "id": 2,
        "nome": "Jorge amaro",
        "idade": 17,
        "condicao": "Diabetes Tipo 1",
        "image": "https://media.licdn.com/dms/image/v2/D4D03AQGXC5i4fHtkuw/profile-displayphoto-crop_800_800/B4DZl83dX7JUAQ-/0/1758736537532?e=1763596800&v=beta&t=hd36msCpHPyiI75MWUE04Ahy3OHpMsj6EErNUknBoio"
    },
    {
        "id": 3,
        "nome": "Pau Varelo",
        "idade": 75,
        "condicao": "Diabetes Tipo 1",
        "image": "https://videos.openai.com/az/vg-assets/task_01k97txd17ewsbdb7bpxyb1xpk%2F1762273556_img_0.webp?se=2025-11-04T18%3A00%3A00Z&sp=r&sv=2024-08-04&sr=b&skoid=5e5fc900-07cf-43e7-ab5b-314c0d877bb0&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-11-04T01%3A08%3A21Z&ske=2025-11-11T01%3A13%3A21Z&sks=b&skv=2024-08-04&sig=/YcjaeG5M3qP94J1JOGmUhmZDP41a%2BeH5UcQtLgc2Tc%3D&ac=oaivgprodscus2"
    }
]

# Dados de médicos
medicos = [
    {
        "id": 1,
        "nome": "Gabriel Vasco",
        "especialidade": "Endocrinologista",
        "anos_experiencia": 10,
        "image": "https://media.licdn.com/dms/image/v2/C4E03AQF_LRKSwl9ePw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1655207311456?e=1763596800&v=beta&t=e5AJvHjkG53gBdJtdz63eUp_cD7HTsXInek6lwJrAO0"
    },
    {
        "id": 2,
        "nome": "Gabriel Moia",
        "especialidade": "Endocrinologista",
        "anos_experiencia": 10,
        "image": "https://media.licdn.com/dms/image/v2/D4D03AQGXC5i4fHtkuw/profile-displayphoto-crop_800_800/B4DZl83dX7JUAQ-/0/1758736537532?e=1763596800&v=beta&t=hd36msCpHPyiI75MWUE04Ahy3OHpMsj6EErNUknBoio"
    },
    {
        "id": 3,
        "nome": "Paulo Varelo",
        "especialidade": "Anal",
        "anos_experiencia": 25,
        "image": "https://videos.openai.com/az/vg-assets/task_01k97tb6tmfta8w3ey7mtwna4t%2F1762272969_img_1.webp?se=2025-11-04T18%3A00%3A00Z&sp=r&sv=2024-08-04&sr=b&skoid=5e5fc900-07cf-43e7-ab5b-314c0d877bb0&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-11-04T01%3A08%3A21Z&ske=2025-11-11T01%3A13%3A21Z&sks=b&skv=2024-08-04&sig=otx1y05QVzOnlejzDMwGrDwyGorZ%2B6yUiFQ1ER%2B%2B5vc%3D&ac=oaivgprodscus2"
    }
]

@app.route("/")
def home():
    return render_template('index.html')

# Listar pacientes
@app.route("/pacientes")
def listar_pacientes():
    return render_template("listar_pacientes.html", pacientes=pacientes)

# Detalhes do paciente
@app.route("/pacientes/<int:paciente_id>")
def detalhes_paciente(paciente_id):
    for paciente in pacientes:
        if paciente["id"] == paciente_id:
            return render_template("detalhe_paciente.html", paciente=paciente)
    return "Paciente não encontrado", 404

# Listar médicos
@app.route("/medicos")
def listar_medicos():
    return render_template("listar_medicos.html", medicos=medicos)

# Detalhes do médico
@app.route("/medicos/<int:medico_id>")
def detalhe_medico(medico_id):
    for medico in medicos:
        if medico["id"] == medico_id:
            return render_template("detalhe_medico.html", medico=medico)
    return "Médico não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
