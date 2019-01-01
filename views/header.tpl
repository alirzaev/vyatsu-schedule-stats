<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
          crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
            integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
            crossorigin="anonymous"></script>
</head>
<body>
<nav class="navbar navbar-expand-md navbar-dark bg-dark position-sticky"
     style="top: 0; z-index: 1020 !important;">
    <button class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="/">API</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/telegram">Telegram</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/viber">Viber</a>
            </li>
        </ul>
    </div>
    <form class="form-inline" action="/logout" method="post">
        <button class="btn btn-danger" type="submit">Выйти</button>
    </form>
</nav>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-12 col-md-6">