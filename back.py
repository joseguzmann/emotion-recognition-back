from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas de la aplicación

@app.route('/backend/audio', methods=['POST'])
def receive_audio():
    audio = request.files['audio']
    print(audio)
    # Aquí puedes trabajar con el archivo de audio recibido, por ejemplo:
    # guardar el archivo en el disco duro
    # procesar el archivo de audio
    # devolver una respuesta al cliente, etc.
    
    # Por ejemplo, aquí devolvemos una respuesta simple indicando que se recibió el archivo de audio
    return 'Archivo de audio recibido'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
