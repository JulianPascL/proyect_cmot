document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('pqrsdForm');
    const fields = {
        primerNombre: form.querySelector('input[name="primer_nombre"]'),
        primerApellido: form.querySelector('input[name="primer_apellido"]'),
        tipoIdentificacion: form.querySelector('select[name="tipo_identificacion"]'),
        numeroIdentificacion: form.querySelector('input[name="numero_identificacion"]'),
        fechaNacimiento: form.querySelector('input[name="fecha_nacimiento"]'),
        direccion: form.querySelector('input[name="direccion"]'),
        telefonoMovil: form.querySelector('input[name="telefono_movil"]'),
        email: form.querySelector('input[name="email"]'),
        emailConfirmacion: form.querySelector('input[name="email_confirmacion"]')
    };

    function showError(field, message) {
        const errorDiv = document.getElementById(field.name + '-error');
        field.classList.add('input-error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }

    function clearError(field) {
        const errorDiv = document.getElementById(field.name + '-error');
        field.classList.remove('input-error');
        errorDiv.textContent = '';
        errorDiv.style.display = 'none';
    }

    function validateField(field) {
        let isValid = true;
        let errorMessage = '';

        if (field.value.trim() === '') {
            isValid = false;
            errorMessage = 'Este campo es requerido';
        } else if (field.name === 'telefono_movil') {
            const telefonoRegex = /^3\d{9}$/;
            if (!telefonoRegex.test(field.value.trim())) {
                isValid = false;
                errorMessage = 'El teléfono móvil debe ser un número colombiano válido (10 dígitos comenzando con 3)';
            }
        } else if (field.name === 'fecha_nacimiento') {
            const hoy = new Date();
            const fechaNacimientoDate = new Date(field.value);
            const edad = hoy.getFullYear() - fechaNacimientoDate.getFullYear();
            const diferenciaMeses = hoy.getMonth() - fechaNacimientoDate.getMonth();
            const diferenciaDias = hoy.getDate() - fechaNacimientoDate.getDate();
            if (fechaNacimientoDate > hoy) {
                isValid = false;
                errorMessage = 'La fecha de nacimiento no puede ser una fecha futura';
            } else if (edad < 18 || (edad === 18 && (diferenciaMeses < 0 || (diferenciaMeses === 0 && diferenciaDias < 0)))) {
                isValid = false;
                errorMessage = 'Debes tener al menos 18 años';
            }
        } else if (field.name === 'numero_identificacion') {
            const tipo = fields.tipoIdentificacion.value;
            const numeroIdentificacionRegex = {
                cc: /^\d{6,10}$/,
                ti: /^\d{6,10}$/,
                ce: /^\d{6,10}$/,
                nit: /^\d{7,11}$/
            };
            if (!numeroIdentificacionRegex[tipo].test(field.value.trim())) {
                isValid = false;
                errorMessage = `El número de identificación no es válido para el tipo ${tipo.toUpperCase()}`;
            }
        } else if (field.name === 'email') {
            const emailRegex = /\S+@\S+\.\S+/;
            if (!emailRegex.test(field.value.trim())) {
                isValid = false;
                errorMessage = 'Por favor, introduce un email válido';
            }
        } else if (field.name === 'email_confirmacion') {
            if (field.value.trim() !== fields.email.value.trim()) {
                isValid = false;
                errorMessage = 'Los correos electrónicos no coinciden';
            }
        }

        if (!isValid) {
            showError(field, errorMessage);
        } else {
            clearError(field);
        }

        return isValid;
    }

    form.addEventListener('submit', function(event) {
        let isValid = true;

        for (const key in fields) {
            if (!validateField(fields[key])) {
                isValid = false;
            }
        }

        if (!isValid) {
            event.preventDefault();
            $('#notification').text('Por favor, corrige los errores en el formulario').removeClass('success').addClass('error').show().delay(3000).fadeOut();
        } else {
            // Aquí puedes enviar el formulario usando AJAX
            event.preventDefault(); // Previene el envío predeterminado

            const formData = new FormData(form);

            $.ajax({
                url: '/submit_pqrsd',
                method: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    $('#notification').text(response.message + ' a las ' + response.time).removeClass('error').addClass('success').show().delay(3000).fadeOut();
                    form.reset();
                    $('.error-message').text('').hide();
                    $('.input-error').removeClass('input-error');
                },
                error: function(xhr) {
                    const errorMessage = xhr.responseJSON ? xhr.responseJSON.error : 'Error al enviar el formulario';
                    $('#notification').text(errorMessage).removeClass('success').addClass('error').show().delay(3000).fadeOut();
                    console.log(xhr.responseJSON);
                }
            });
        }
    });

    for (const key in fields) {
        fields[key].addEventListener('blur', function() {
            validateField(fields[key]);
        });
    }
});
