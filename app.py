import openai
from flask import Flask, request, render_template,jsonify
from llama_index import load_index_from_storage,StorageContext
openai.api_key = "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"
app = Flask(__name__)

context = StorageContext.from_defaults(persist_dir="vectorstoreindex")
index = load_index_from_storage(storage_context=context)
query_engine = index.as_query_engine()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Bot',methods=["GET"])
def Chatbot():
    return render_template('BOT.html')
@app.route('/predict', methods=['POST'])
def predict():
    prompt = request.form.get('user_input')

    prediction = query_engine.query(prompt)

    return jsonify({'prediction': str(prediction)})


if __name__ == "__main__":
    app.run(debug=True)




