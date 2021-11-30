from flask import Blueprint, request, send_from_directory
from os import getcwd, path, remove
from responses.response_json import response_json

routes_files = Blueprint("routes_files", __name__)

PATH_FILES = getcwd() + "/files/"

@routes_files.post("/upload")
def upload_file():
    try:
        file = request.files['file']
        file.save(PATH_FILES + file.filename)
        return response_json("success")
    except FileNotFoundError:
        return response_json("Folder not found", 404)


@routes_files.route("/file/<string:name_file>")
def get_image(name_file):
    return send_from_directory(PATH_FILES, path=name_file, as_attachment=False)


@routes_files.get("/download/<string:name_file>")
def download_image(name_file):
    return send_from_directory(PATH_FILES, path=name_file, as_attachment=True)


@routes_files.delete('/delete')
def delete_file():
    filename = request.form['filename']

    # CHECK IF EXISTS FILE
    if path.isfile(PATH_FILES + filename) == False:
        return response_json("File does not exist", 404)
    else:
        try:
            remove(PATH_FILES + filename)
            return response_json("File deleted")
        except OSError:
            return response_json(OSError, 404)