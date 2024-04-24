const mongoose  = require('mongoose');
require('dotenv').config()

const uri = `mongodb+srv://root:<password>@cluster0.sbs4zl1.mongodb.net/?retryWrites=true&w=majority`

mongoose.connect(uri)
.then(() => console.log( `CONNECTION WITH DATABASE ESTABLISHED WITH SUCCESS`))
.catch(error => console.log("CONNECTION WITH DATABASE FAILED", error))