from flask import Flask
import datetime
app = Flask(__name__)

class Blockchain:
   def __init__(self):
      self.chain=[]

   def create_block(self,proof,previous_hash):
      block={
            'index':len(self.chain)+1,
            'timestamp':str(datetime.datetime.now()),
            'proof':proof,
            'previous_hash':previous_hash
         }
      self.chain.append(block)

@app.route('/')
def hello_name():
   return "karun boka ho!"

if __name__ == '__main__':
   app.run()