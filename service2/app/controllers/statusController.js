const statusService = require('../services/status');

const getStatus = (req, res) => {
  const statusMessage = statusService.getSystemStatus();

  res.set("Content-Type", "text/plain");
  res.status(200).send(statusMessage);
};

module.exports = {
  getStatus,
};
