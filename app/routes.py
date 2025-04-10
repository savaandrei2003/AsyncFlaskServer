from app import webserver
from flask import request, jsonify

import os
import json

from app.task_runner import Task

# Example endpoint definition
@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():
    if request.method == 'POST':
        # Assuming the request contains JSON data
        data = request.json
        print(f"got data in post {data}")

        # Process the received data
        # For demonstration purposes, just echoing back the received data
        response = {"message": "Received data successfully", "data": data}

        # Sending back a JSON response
        return jsonify(response)
    else:
        # Method Not Allowed
        return jsonify({"error": "Method not allowed"}), 405

@webserver.route('/api/get_results/<job_id>', methods=['GET'])
def get_response(job_id):
    print(f"JobID is {job_id}")
    # TODO
    # Check if job_id is valid

    # Check if job_id is done and return the result
    #    res = res_for(job_id)
    #    return jsonify({
    #        'status': 'done',
    #        'data': res
    #    })

    # If not, return running status
    return jsonify({'status': 'NotImplemented'})

@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/states_mean'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/state_mean'
    question = data['question']
    state = data['state']
    task_data = (endpoint, question, state)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201


@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    data = request.json
    
    webserver.job_counter += 1
    endpoint = '/api/best5'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)
    return jsonify({'job_id': webserver.job_counter}), 201


@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/worst5'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/global_mean'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    data = request.json
    
    webserver.job_counter += 1
    endpoint = '/api/diff_from_mean'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)
    return jsonify({'job_id': webserver.job_counter}), 201


@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/state_diff_from_mean'
    question = data['question']
    state = data['state']
    task_data = (endpoint, question, state)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/mean_by_category'
    question = data['question']
    task_data = (endpoint, question)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    data = request.json

    webserver.job_counter += 1
    endpoint = '/api/state_mean_by_category'
    question = data['question']
    state = data['state']
    task_data = (endpoint, question, state)
    task_to_enqueue = Task(webserver.job_counter, task_data)
    webserver.tasks_runner.add_task(task_to_enqueue)

    return jsonify({'job_id': webserver.job_counter}), 201

# You can check localhost in your browser to see what this displays
@webserver.route('/')
@webserver.route('/index')
def index():
    routes = get_defined_routes()
    msg = f"Hello, World!\n Interact with the webserver using one of the defined routes:\n"

    # Display each route as a separate HTML <p> tag
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"

    msg += paragraphs
    return msg

def get_defined_routes():
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f"Endpoint: \"{rule}\" Methods: \"{methods}\"")
    return routes
