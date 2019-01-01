% rebase('basepage.tpl', title='Вход')
<form action="/login" method="post"
      class="pt-1 needs-validation" novalidate>
    <div class="form-group">
        <label for="username">Имя пользователя</label>
        <input type="text" class="form-control"
               name="username" id="username" required/>
        <div class="invalid-feedback">
          Введите имя пользователя
        </div>
    </div>
    <div class="form-group">
        <label for="password">Пароль</label>
        <input type="password" class="form-control"
               name="password" id="password" required/>
        <div class="invalid-feedback">
          Введите пароль
        </div>
    </div>
    <button type="submit" class="btn btn-primary">Войти</button>
</form>
<script>
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
</script>