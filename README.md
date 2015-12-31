# Complete-Angularjs-Flask-Todo-App
A todo web-app using  AngularJS as Front-end and Flask as Back-end

## Installation

1. Create a virtualenv for the Flask app, `virtual-env flask-app`, and start it.

2. Inside the _ToDO_ directory, install Flask

3. Run app.py

## Summary
This project is using Flask to serve data, and AngularJS to control and view it.
<h1>Main features of this App</h1>

## API Endpoints

<table>
<tr>
  <th>Description</th>
  <th>HTTP Method</th>
  <th>URL</th>
</tr>
<tr>
  <td>Get all todos</td>
  <td>GET</td>
  <td>saitodo/api/v1.0/tasks</td>
</tr>
<tr>
  <td>Delete all todos</td>
  <td>DELETE</td>
  <td>saitodo/api/v1.0/tasks</td>
</tr>
<tr>
  <td>Create a new todo</td>
  <td>POST</td>
  <td>saitodo/api/v1.0/tasks</td>
</tr>
<tr>
  <td>Delete mulipuli Todos</td>
  <td>DELETE</td>
  <td>todoapp/api/todos/muldelet/:id</td>
</tr>
<tr>
  <td>Delete a todo</td>
  <td>DELETE</td>
  <td>todoapp/api/todos/:id</td>
</tr>
<tr>
  <td>Update a todo</td>
  <td>PUT</td>
  <td>saitodo/api/v1.0/tasks/:id</td>
</tr>
</table>
