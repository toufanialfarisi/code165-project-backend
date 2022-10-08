# import library
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

# inisialisasi object flask 
app = Flask(__name__)
api = Api(app)
CORS(app)

# inisialisasi variabel data => data itu banyak / list / array
# data dummy
data = [
    {
        "judul":"cara produktif", # id = 0
        "konten":"cara sederhana menjadi produktif",
        "img":"https://cdn.ksprtj.net/wp/images/2022/08/Pengertian%20Produktif%20adalah.png"
    },
    {
        "judul":"cara sehat", # id = 1
        "konten":"cara sederhana menjadi sehat", 
        "img":"https://res.cloudinary.com/dk0z4ums3/image/upload/v1648555158/attached_image/saluran-cerna-sehat-untuk-daya-tahan-tubuh-optimal.jpg"
    },
    {
        "judul":"cara sukses", # id = 2
        "konten":"cara sederhana menjadi sukses", 
        "img":"https://www.tipspengembangandiri.com/wp-content/uploads/2016/05/Ilustrasi-menjadi-orang-sukses.jpg"
    },
]

# membuat class data untuk pembuatan endpoint
class GetAllData(Resource):
    def get(self):
        output = jsonify(data) #real
        return output


# membuat class data baru untuk menampilkan detail dari data
class GetDetailData(Resource):
    def get(self, id):
        index = id 
        chosenData = data[index]
        output = jsonify(chosenData)
        return output


# membuat endpoint / inisialisasi url endpoint
api.add_resource(GetAllData, "/api/data", methods=["GET"])
api.add_resource(GetDetailData, "/api/data/<int:id>", methods=["GET"])

# jalankan aplikasinya
if __name__ == "__main__":
    app.run(debug=True, port=5000)


