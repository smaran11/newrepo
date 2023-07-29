 from flask import Flask
  2 
  3 app = Flask(__name__)
  4 
  5 
  6 @app.route("/", methods=["GET"])
  7 def root():
  8     return "welcome to ITIL exam"
  9 
 10 app.run(host="0.0.0.0", port=3000, debug=True)
