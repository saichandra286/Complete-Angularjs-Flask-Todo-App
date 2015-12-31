# Complete-Angularjs-Flask-Todo-App
A todo web-app using  AngularJS as Front-end and Flask as Back-end

## Installation

1. Create a virtualenv for the Flask app, `virtual-env flask-app`, and start it.

2. Inside the _ToDO_ directory, install Flask

3. Run app.py

## Summary
This project is using Flask to serve data, and AngularJS to control and view it.
<h6>Main features of this App</h6>
1. create a newtodo
2. update a selected todo
3. delete particular todo
4. delete multi todo
5. delete all todos
6. search for particluar todo and update or delete todo
7. not allowing duplicates while posting todo or updating todo

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
  <td>Delete multi Todos</td>
  <td>DELETE</td>
  <td>saitodo/api/v1.0/tasks/muldelet/:id</td>
</tr>
<tr>
  <td>Delete a todo</td>
  <td>DELETE</td>
  <td>saitodo/api/v1.0/tasks/:id</td>
</tr>
<tr>
  <td>Update a todo</td>
  <td>PUT</td>
  <td>saitodo/api/v1.0/tasks/:id</td>
</tr>
</table>
