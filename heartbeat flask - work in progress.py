
from typing import Tuple, Any
from flask import Flask, jsonify, request
from classes import Check, Schedule
import testDB, string, random, time, datetime, secrets, json


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def home():
    return "solution for KSI task:  "


@app.route("/check", methods=["GET", "POST"])
def check_create():
    id = "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(32)]
    )
    last_ping = datetime.datetime.now()
    last_ping = str(last_ping)

    new_check = Check(
        id,
        last_ping,
        last_ping_timestamp=round(time.time()),
        name=request.get_json()["name"],
        secret_key=secrets.token_urlsafe(16),
        status="ok",
    )
    def_per=5
    def_grace=10
    new_schedule=Schedule(new_check.id,def_per,def_grace,new_check.secret_key)
    testDB.create_check(new_check)
    testDB.add_to_schedule(new_schedule)

    return jsonify(new_check.__dict__)


@app.route("/check/<id>", methods=["GET", "DELETE"])
def get_check(id):
    secret_key=request.args.get('secret_key')
    if request.method == "GET":
        if testDB.get_check(id)!=[] and secret_key is None:
            data=testDB.get_check(id)
            json_data={
                "id":id,
                "last_ping":data[0][1],
                "last_ping_timestamp":data[0][2],
                "name":data[0][3],
                "status":data[0][4]

            }
            return jsonify(json_data)     
        else: 
            return 'some error has occured', 404

    if request.method == "DELETE":
        secret_key = request.args.get("secret_key")
        if secret_key is None:
            return "secret key is none", 401
        actual_secret=testDB.check_check_secret(id)
        if secret_key==actual_secret and secret_key !=None or actual_secret!=None:
            testDB.delete_check(id, secret_key)
            return 'check deleted successfully', 200

@app.route("/ping/<id>")
def change_ping(id):
    if testDB.get_check(id) != []:
        new_ping = datetime.datetime.now()
        new_ping = str(new_ping)
        testDB.ping(id, new_ping)
        return f"last_ping updated to:  {new_ping}"
    else:
        return "", 404
# 


@app.route('/schedule/<id>', methods=['GET', 'PUT'])
def check_schedule(id):
    secret_key=request.args.get('secret_key')
    actual_secret=str(testDB.check_schedule_key(id))
    actual_secret=actual_secret.translate(str.maketrans({"[": "", "]": "", "(": "", ")": "", "'": "", ",": ""}))
    if request.method=='GET':
        if secret_key == actual_secret:
            data=testDB.check_schedule(id, secret_key)
            json_data = {
                "id":id,
                "period":data[0][1],
                "grace":data[0][2]
            }
            return json_data
        elif secret_key == None:
            return "",401
        else:
            return "",404
    if request.method == 'PUT':
        if secret_key == actual_secret:
            testDB.put_schedule(id, secret_key,request.get_json()["period"], request.get_json()["grace"])
            return "Successful operation", 200

@app.route('/notification_settings/<id>', methods=['GET', 'PUT'])
def check_notification_settings(id):
    secret_key=request.args.get('secret_key')
    if request.method=='GET':

        if secret_key != None:
            emails=[]
            my_webhook='https://healthcheck_notifications.iamroot.eu/send_notification/'
            notification_data={
                "id":id,
                "webhook":my_webhook,
                "emails":emails
            }
            return notification_data
        if secret_key == None:
            return 'no secret key', 401
    if request.method == 'PUT':
        if secret_key == testDB.check_check_secret(id) and testDB.get_check(id)!=[]:
            return 
            

@app.route('/cron')
def call_cron():
    return "", 200


@app.route("/test")
def test():
    number = request.args.get("number")
    return f"just a test {number}"


if __name__ == "__main__":
    app.run(debug=True, port=5081)
