from flask import Flask, request, jsonify
import fdb

app = Flask(__name__)

HOST = "corporativomichelle.com"
DATABASE = "SISTEMA"
USER = "SYSDBA"
PASSWORD = "masterkey"
PORT = 3050

@app.route("/")
def home():
    return "API funcionando 🔥"

@app.route("/remision", methods=["GET"])
def remision():
    try:
        movtipo = request.args.get("movtipo")
        consecutivo = request.args.get("consecutivo")

        con = fdb.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            port=PORT
        )

        cur = con.cursor()

        query = f"""
        SELECT DOCR_CODIGO_DESCARGA
        FROM TDOC_REMISION
        WHERE DOCR_MOVTIPO = '{movtipo}'
        AND DOCR_CONSECUTIVO = '{consecutivo}'
        """

        cur.execute(query)
        row = cur.fetchone()

        con.close()

        if row:
            return jsonify({"codigo": row[0]})
        else:
            return jsonify({"codigo": None})

    except Exception as e:
        return jsonify({"error": str(e)})
