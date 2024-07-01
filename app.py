from flask import Flask, request, redirect, url_for, render_template, send_file, jsonify # type: ignore
import pandas as pd # type: ignore
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        json_path = convert_to_json(file_path)
        return send_file(json_path, as_attachment=True)

def convert_to_json(file_path):
    # Load the Excel data
    data = pd.read_excel(file_path)

    # Convert to JSON format
    data_json = data.to_json(orient='records')

    # Save JSON to a file
    json_filename = os.path.splitext(file_path)[0] + '.json'
    with open(json_filename, 'w') as f:
        f.write(data_json)
    
    return json_filename

@app.route('/clear', methods=['POST'])
def clear_files():
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"status": "All files cleared"}), 200

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
