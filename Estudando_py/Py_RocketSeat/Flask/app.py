from flask import Flask, request
from models.task import Task

app = Flask(__name__)

task = []

@app.route('/tasks', methods= ['POST'])
def create_task():
  data = request.get_json()
  print = data
  return 'Test'


if __name__ == "__main__": #Trava de segurança
  app.run(debug=True)