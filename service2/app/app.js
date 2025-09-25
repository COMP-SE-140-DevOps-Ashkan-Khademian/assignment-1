const express = require("express");
const morgan = require("morgan");
const statusRoutes = require("./routes/statusRoutes");

const app = express();

morgan.token('pid', () => process.pid);
morgan.token('timestamp', () => new Date().toUTCString());

const customFormat = '[pid: :pid] :remote-addr (:remote-user) [:timestamp] :method :url => :status :res[content-length] bytes in :response-time ms (HTTP/:http-version)';

app.use(morgan(customFormat));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/", statusRoutes);

module.exports = app;

