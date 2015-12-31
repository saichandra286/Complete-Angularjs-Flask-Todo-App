# Complete-Angularjs-Flask-Todo-App
A todo web-app using  AngularJS as Front-end and Flask as Back-end

## Installation

1. Create a virtualenv for the Flask app, `virtual-env flask-app`, and start it.

2. Inside the _flask-app_ directory, install Flask: `pip install flask`.

3. Run `npm install` to get NodeJS and Grunt dependencies.

4. Additionally, run `bower install` to get Bower dependencies.

5. Build the files and start the server by running `grunt`. If you would like to only build the files, run `grunt build`. Start the server later with `grunt server`.

## Summary

This project is using Flask to serve data, and AngularJS to control and view it. Other tech used for the project: CoffeeScript, SASS, GruntJS, RequireJS, spritesmith, and Bower.

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
  <td>todoapp/api/todos</td>
</tr>
<tr>
  <td>Delete all todos</td>
  <td>DELETE</td>
  <td>todoapp/api/todos</td>
</tr>
<tr>
  <td>Create a new todo</td>
  <td>POST</td>
  <td>todoapp/api/todos</td>
</tr>
<tr>
  <td>Get a todo</td>
  <td>GET</td>
  <td>todoapp/api/todos/:id</td>
</tr>
<tr>
  <td>Delete a todo</td>
  <td>DELETE</td>
  <td>todoapp/api/todos/:id</td>
</tr>
<tr>
  <td>Update a todo</td>
  <td>PUT</td>
  <td>todoapp/api/todos/:id</td>
</tr>
</table>
