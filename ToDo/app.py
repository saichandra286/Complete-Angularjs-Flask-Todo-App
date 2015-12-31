import sys
from flask import Flask, jsonify, json, abort, redirect, make_response, request, url_for, render_template, Response, Blueprint
from flask.ext.httpauth import HTTPBasicAuth
from exampletodo import tasks

app=Flask(__name__)

muld =[]

@app.route('/saitodo/api/v1.0/tasks', methods=['GET'])
def gettasks():
	del muld[:]
	return jsonify({'tasks':tasks}), 200


@app.route('/saitodo/api/v1.0/tasks/<int:taskid>', methods=['GET'])
def gettask(taskid):
	tsk = [x for x in tasks if x['id'] == taskid]
	if len(tsk) == 0:
		abort(404)
	return jsonify({'tasks':tsk[0]})

@app.errorhandler(404)
def notfound(error):
	return make_response(jsonify({'error':'Not Found'}), 404)

@app.route('/saitodo/api/v1.0/tasks', methods=['POST'])
def addnewtask():
	if not request.json or not 'title' in request.json:
		abort(404)
	for i in range(len(tasks)):
		if tasks[i]['title'] == request.json['title']:
			abort(400);
	if len(tasks)==0:
		tsk = {
			'id':1,
			'title':request.json['title'],
			'description':request.json.get('description', "")
		}
	if len(tasks)>0:	
		tsk = {
			'id':tasks[-1]['id']+1,
			'title':request.json['title'],
			'description':request.json.get('description', ""),
			'done':False
		}
	tasks.append(tsk)
	return jsonify({'tsk':tsk}), 201

@app.route('/saitodo/api/v1.0/tasks/<int:taskid>', methods=['PUT'])
def update(taskid):
	tsk = [x for x in tasks if x['id'] == taskid]
	'''if len(tsk) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)'''
	for i in range(len(tasks)):
		if tasks[i]['id'] != taskid:
			if tasks[i]['title'] == request.json['title']:
				abort(400);
	tsk[0]['title'] = request.json.get('title', tsk[0]['title'])
	tsk[0]['description'] = request.json.get('description', tsk[0]['description'])
	#tsk[0]['done'] = request.json.get('done', tsk[0]['done'])
	return jsonify({'tasks':tasks})


@app.route('/saitodo/api/v1.0/tasks/<int:id1>/<int:id2>', methods=['GET'])
def swapdwn(id1, id2):
	for x in range(len(tasks)):
		if tasks[x]['id'] == id1:
			a=x
		if tasks[x]['id'] == id2:
			b=x
	tasks[b],tasks[a] = tasks[a],tasks[b]
	return jsonify({'tasks':tasks})

@app.route('/saitodo/api/v1.0/tasks/<int:taskid>', methods=['DELETE'])
def dele(taskid):
	tsk = [x for x in tasks if x['id'] == taskid]
	if len(tsk) == 0:
		abort(404)
	tasks.remove(tsk[0])
	return jsonify({'tasks': tasks, 'tks':muld})


@app.route('/saitodo/api/v1.0/tasks/muldelet/<int:taskid>', methods=['DELETE'])
def muldel(taskid):
	for x in tasks:
		if x['id'] == taskid and x not in muld:
			muld.append(x)
	return jsonify({'tsk':muld})

@app.route('/saitodo/api/v1.0/tasks/muldelet', methods=['DELETE'])
def multdel():
	for x in muld:
		if x in tasks:
			tasks.remove(x)
	return jsonify({'tasks':tasks})

@app.route('/saitodo/api/v1.0/tasks/undo/<int:taskid>', methods=['DELETE'])
def undodele(taskid):
	tk = [x for x in muld if x['id'] == taskid]
	if len(tk) == 0:
		abort(404)
	muld.remove(tk[0])
	return jsonify({'tk':muld})

@app.route('/saitodo/api/v1.0/tasks/undo', methods=['DELETE'])
def undoall():
	del muld[:]
	return jsonify({'jk':muld})

@app.route('/saitodo/api/v1.0/tasks', methods=['DELETE'])
def delall():
	del tasks[:]
	return jsonify({'tasks':tasks})

def mkpublic(tsk):
	newtsk = {}
	for field in tsk:
		if field == 'id':
			newtsk['uri'] = url_for('gettasks', taskid=tsk['id'], _external=True)
		else:
			newtsk[field] = tsk[field]
	return newtsk



@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
