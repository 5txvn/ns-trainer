const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors());

app.get('/addition/2-digit', (req, res) => {
    const a = Math.floor(Math.random() * 90 + 10);
    const b = Math.floor(Math.random() * 90 + 10);
    const answer = a + b;
    res.json({
        "input-one": a,
        "input-two": b,
        "answer": answer
    })
})

app.listen(3000)