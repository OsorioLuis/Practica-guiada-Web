// imports
const express = require('express')
const path = require('path')
const methodOverride = require('method-override')
const session = require('express-session')
const flash = require('connect-flash')
const { create } = require('express-handlebars')
const passport = require('passport')

// inicializacion
const app = express();
require('./database');
require('./config/passport');

// settings
app.set('port', process.env.PORT || 4000);
app.set('views', path.join(__dirname, 'views'));

// hbs 
const expHbs = create({
    defaultLayout: 'main',
    runtimeOptions: {
        allowProtoMethodsByDefault: true,
        allowProtoPropertiesByDefault: true
    },
    layoutsDir: path.join(app.get('views'), 'layouts'), //ubicacion del archivo layauts
    partialsDir: path.join(app.get('views'), 'partials'),
    extname: '.hbs'
});
// seteamos el engine de hbs
app.engine('hbs', expHbs.engine)
app.set('view engine', '.hbs'); //seteamos el motor

//use en concreto nos sirve para el uso de middlewares puede servir como iterador
// middlewares
app.use(express.urlencoded({extended: false})) // nos sirve para recepcion de datos
// urlencoded() es un body-parser analiza los request entrantes y codifica sus entradas
app.use(methodOverride('_method')); // para que se puedan enviar otro tipo de metodos

app.use(session({
    secret: 'mysecret',
    resave: true,
    saveUninitialized: true
}));
app.use(passport.initialize()); // iniciamos el protocolo
app.use(passport.session());
app.use(flash());

// global variables
app.use((req, res, next) => {
    //locals hacen referencia a variables locales
    res.locals.success_msg = req.flash('success_msg'),
    res.locals.error_msg = req.flash('error_msg'),
    res.locals.error = req.flash('error'),

    res.locals.user = req.user || null;
    next(); //para que imprima los mensajes de error iterandolos

});
// routes
app.use(require('./routes/index'));
app.use(require('./routes/notes'));
app.use(require('./routes/users'));

// static files
app.use(express.static(path.join(__dirname, 'public')));

// server listeners
app.listen(app.get('port'), () => {
    console.log("server en linea" + app.get('port'))
})