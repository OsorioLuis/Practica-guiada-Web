const helpers = {};

//esta funcion esta hecha como middleware para la autenticacion del usuario, si no se 
//hace cualquier persona puede navegar por los paginas de usuario
helpers.isAuthenticated = (req, res, next) => {
    if(req.isAuthenticated()){
        return next(); // que continue con la siguiente funcion
    };
    req.flash('error_msg', 'No autorizado')
    res.redirect('/users/signin')
};

module.exports = helpers;