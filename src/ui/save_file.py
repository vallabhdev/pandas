from flask import Blueprint, request

# from werkzeug import secure_filename


save_blueprint = Blueprint("save_blueprint", __name__)


@save_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        # f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
