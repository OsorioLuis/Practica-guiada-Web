const express = require('express');
const router = express.Router();

const Note = require('../models/Note');
//importamos la clase especifica
const { isAuthenticated } = require('../helpers/auth')

// para cada ruta nos aseguramos que el usuario este logeado
router.get('/notes/add', isAuthenticated, (req, res) => {
    res.render('notes/new-notes')
});

router.post('/notes/new-note', async (req, res) => {
    const { title, description } = req.body; //traemos el titulo y descripcion de la nota
    const errors = [];

    //validacion:
    //!title es operador logico de negacion, es decir si el booleano inverso
    //de title es verdadero entonces almacena el mensaje
    if(!title){
        errors.push({text: "Por favor inserta un titulo"});
    }
    if(!description){
        errors.push({text: "Por favor escribe una descripción"})
    }
    if(errors.length > 0){
        res.render('notes/new-notes', {
            errors,
            title,
            description
        });
    }else{
        // creamos un nuevo objeto para guardar en la base de datosen mongo
        const newNote = new Note({title, description}); // guardamos los datos instanciados
        newNote.user = req.user.id; // guardamos el id del usuario en el campo user de la collection users

        await newNote.save();
        req.flash('success_msg', 'Nota agregada satisfactoriamente'); //con el flash hacemos uso del renderizado de errores
        res.redirect('/notes');
    }
});

// vista para consultar los datos en la BBDD
router.get('/notes', isAuthenticated, async (req, res) => {
    // las notas se ordenan de manera descendente según la fecha de creación
    // mostrará las notas de los usuarios con sesión iniciada en especifico
    const notes = await Note.find({user: req.user.id}).sort({date: 'desc'})
    res.render('notes/all-notes', { notes }); // estas notas se enlistan en un bucle each en hbs
    //iterando cada nota en un arreglo
});

//ruta para editar notas
router.get('/notes/edit/:id', isAuthenticated, async (req, res ) => {
    const note = await Note.findById(req.params.id)
    res.render('notes/edit-notes', { note })
})

//metodo para actualizar notas
router.put('/notes/edit-note/:id', isAuthenticated, async (req, res) => {
    const { title, description } = req.body
    await Note.findByIdAndUpdate(req.params.id, {title, description});
    req.flash('success_msg', 'Nota actualizada satisfactoriamente');
    res.redirect('/notes');
});

// metodo para eliminar notas
router.delete('notes/delete/:id', isAuthenticated, async (req, res) => {
    await Note.findByIdAndDelete(req.params.id) // simplemente se elimina de la base de datos
    req.flash('success_msg', 'Nota eliminada satisfactoriamente');
    res.redirect('/notes');
    
});

module.exports = router;