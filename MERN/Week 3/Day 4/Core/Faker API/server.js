const express = require('express');
const Chance = require('chance');
const app = express();
const port = 8001;

const chance = new Chance();

function createUser() {
    return {
        password: chance.string(),
        email: chance.email(),
        phoneNumber: chance.phone(),
        lastName: chance.last(),
        firstName: chance.first(),
        _id: chance.guid(),
    };
}


function createCompany() {
    return {
        _id: chance.guid(),
        name: chance.company(),
        address: {
            street: chance.address(),
            city: chance.city(),
            state: chance.state(),
            zipCode: chance.zip(),
            country: chance.country(),
        },
    };
}

// Express route to handle new user creation
app.get('/api/users/new', (req, res) => {
    const newUser = createUser();
    res.json({ user: newUser });
});

// Express route to handle new company creation
app.get('/api/companies/new', (req, res) => {
    const newCompany = createCompany();
    res.json({ company: newCompany });
});

// Express route to handle both new user and new company creation
app.get('/api/user/company', (req, res) => {
    const newUser = createUser();
    const newCompany = createCompany();
    res.json({ user: newUser, company: newCompany });
});

// Start the Express server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
