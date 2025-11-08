$("#togglePwd").on("click", async function () {
        if($('#password').attr('type') !== undefined) {
            // El atributo existe
            $('#password').removeAttr("type");
            $("#togglePwd").html(' <i class="bi bi-eye"></i>');
            
    } else {
            // El atributo no existe
            $('#password').attr("type", "password");
            $("#togglePwd").html('<i class="bi bi-eye-slash"></i>');
    }
})