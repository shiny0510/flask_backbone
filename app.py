# app.py
from flask import Flask, render_template
from flask import request

import pymysql

# DB 연동 
db_conn = pymysql.connect(
          host = 'localhost',
          port = 3306,
          user = 'root',
          passwd = '1234',
          db = 'test',
          charset= 'utf8'
)


#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/main') # 접속하는 url
def index():
  temp = request.args.get('uid')
  temp1 = request.args.get('cid')
  
  print(temp ,temp1)
  
  return render_template('index.html')



@app.route('/test')
def testget():

  return render_template('posttest.html')



@app.route('/test',methods=['POST'])
def testpost():
  value = request.form['input']

  print(value)

  return render_template('posttest.html')

@app.route('/sqltest')
def sqltest():
  # 커서 객체 생성
  cursor = db_conn.cursor()

  query = "select * from player"

  cursor.execute(query)

  result = [] 

  for i in cursor:   # i는 ('2012136', '오비나', 'K10', '', '', '', 'MF', 26, '', datetime.date(1990, 6, 3), '1', 169, 70) 들어옴
    temp = {'player_id':i[0],'player_name':i[1] }
    result.append(temp)

  return render_template('sqltest.html', result_table = result)


@app.route('/detail')
def detailtest():
  temp = request.args.get('id')
  temp1 = request.args.get('name')    

  cursor = db_conn.cursor()
                                                                          # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
  query = "select * from player where player_id = {} and player_name like '{}'".format(temp,temp1)

  cursor.execute(query)
  
  result = []
  for i in cursor:   # i는 ('2012136', '오비나', 'K10', '', '', '', 'MF', 26, '', datetime.date(1990, 6, 3), '1', 169, 70) 들어옴
    temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2],'weight':i[-1] }
    result.append(temp)

  return render_template('detail.html', result_table = result)

@app.route('/delete')
def deletetest():
  # 삭제 선언
  temp = request.args.get('id')
  temp1 = request.args.get('name')    

  cursor = db_conn.cursor()
                                                                      # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
  query = "delete from player where player_id = {} and player_name like '{}'".format(temp,temp1)

  cursor.execute(query)

  

  # 커서 객체 생성
  cursor = db_conn.cursor()

  query = "select * from player"

  cursor.execute(query)

  result = [] 

  for i in cursor:   # i는 ('2012136', '오비나', 'K10', '', '', '', 'MF', 26, '', datetime.date(1990, 6, 3), '1', 169, 70) 들어옴
    temp = {'player_id':i[0],'player_name':i[1] }
    result.append(temp)
    
  return render_template('sqltest.html', result_table = result)


import math

@app.route('/update',methods=['POST'])
def fileupload():
  temp = request.args.get('id')
  temp1 = request.args.get('name') 

  pname = request.form['pname']
  tname = request.form['tname']
  weight = request.form['weight']
  height = request.form['height']
  
  if pname != '':
    cursor = db_conn.cursor()                                                                  # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
    query = "update player set player_name = '{}' where player_id = {} and player_name like '{}' ".format(pname,temp,temp1)
    temp1 = pname
    cursor.execute(query)
  
  if tname != '':
        
    cursor = db_conn.cursor()                                                                  # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
    query = "update player set team_id = '{}' where player_id = {} and player_name like '{}' ".format(tname,temp,temp1)
    print(query)
    cursor.execute(query)
  
  if weight != '':
    cursor = db_conn.cursor()                                                                  # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
    query = "update player set weight = {} where player_id = {} and player_name like '{}' ".format(weight,temp,temp1)
    cursor.execute(query)
  
  if height != '':
    cursor = db_conn.cursor()                                                                  # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
    query = "update player set height = {} where player_id = {} and player_name like '{}' ".format(height,temp,temp1)
    cursor.execute(query)


  # 다시불러오기
  cursor = db_conn.cursor()
                                                                          # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
  query = "select * from player where player_id = {} and player_name like '{}'".format(temp,temp1)

  cursor.execute(query)
  
  result = []
  for i in cursor:   # i는 ('2012136', '오비나', 'K10', '', '', '', 'MF', 26, '', datetime.date(1990, 6, 3), '1', 169, 70) 들어옴
    temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2],'weight':i[-1] }
    result.append(temp)

  return render_template('detail.html', result_table = result)

if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)

