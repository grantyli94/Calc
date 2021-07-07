# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

    

# @app.route("/add")
# def add():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     return f"""
#     <!DOCTYPE html>
#       <html lang="en">
#         <body>
#           <h1>{operations.add(a,b)}</h1>
#         </body>
#       </html>
#     """


@app.route("/<operation>")
def main(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    OPERATIONS = {
      "add": operations.add,
      "sub": operations.sub,
      "mult": operations.mult,
      "div": operations.div
    }

    if operation not in OPERATIONS:
        answer = "Please select a valid operation"
    else:
        answer = OPERATIONS[operation](a,b)
    
    return f"""
    <!DOCTYPE html>
      <html lang="en">
        <body>
          <h1>{answer}</h1>
        </body>
      </html>
    """
