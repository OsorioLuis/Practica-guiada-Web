const passport = require('passport')

const User = require('../models/User');
const LocalStrategy = require('passport-local').Strategy; //para la forma de autenticacion local

passport.use(new LocalStrategy({
    usernameField: 'email'
}, async (email, password, done) => {
    //findone trae la primera coincidencia que encuentre al guscar el email
    const user = await User.findOne({email: email}); // guarda si el email es el mismo guardado en user
    if(!user){
        return done(null, false, {message: 'Usuario no encontrado'});
    }else{
        const match = await user.matchPassword(password);
        if(match){
            return done(null, user);
        }else{
            return done(null, false, {message: 'Contraseña incorrecta'})
        }
    }
}));

// sesion del usuario, si el usuario se loguea el se guarda su id
passport.serializeUser((user, done) => {
    done(null, user.id);
    // en caso de que el usuario ya esté iniciado ya no se pide inicio de sesion en
    // cada pagina que entre
})

// hace el proceso inverso, deserealiza el usuario para usar sus datos
passport.deserializeUser((id, done) => {
    // busca un usuario por id, si no está da el error, en caso de que este le pasa el user
    User.findById(id, (err, user) => {
        done(err, user);
    })
})