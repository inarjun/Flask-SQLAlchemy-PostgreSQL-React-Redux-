//templates/login.html
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Login</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css">
 <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
 </head>
 <body style="background-color:#ccc;">
  <div class="login-box" >
  <div class="login-header">Login</div>
  <div class="login-body">
    <p>Please enter your username and password</p>
    <form class="form-group" action="{{ url_for('login') }}" method="post">
        <label>Username</label>
        <input type="text" class="form-control" name="username" placeholder="Username" id="username" required>
        <label>Password</label>
        <input type="password" class="form-control" name="password" placeholder="Password" id="password" required>
        <input type="checkbox" value="checked"><b>Remember</b>
        <input type="submit" value="Login" class="form-control btn btn-success " name="">
    </form>
    {% with messages = get_flashed_messages()  %}
    {% if messages %}
    {% for message in messages %}
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      {{ message }}
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">×</span>
      </button>
    </div>
    {% endfor %}
    {% endif %}
    {% endwith %}
    <p>No account <a href="{{ url_for('register') }}">Register</a></p>
  </div>
 </div>
 </body>
</html>
