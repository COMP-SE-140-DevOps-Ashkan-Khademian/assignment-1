const getStatus = (req, res) => {
  const statusMessage = "Service2 is running and healthy";

  res.set("Content-Type", "text/plain");
  res.status(200).send(statusMessage);
};

module.exports = {
  getStatus,
};
