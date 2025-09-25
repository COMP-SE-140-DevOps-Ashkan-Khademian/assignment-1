const express = require("express");
const statusRoutes = require("./routes/statusRoutes");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/", statusRoutes);

module.exports = app;

