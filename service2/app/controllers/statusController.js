const StatusService = require('../services/status');
const StorageInterface = require('../interfaces/storageInterface');

const getStatus = async (req, res) => {
  const statusService = new StatusService();
  const statusMessage = statusService.getSystemStatus();
    
  const storage = new StorageInterface();
  await storage.appendLog(statusMessage);
  
  res.set("Content-Type", "text/plain");
  res.status(200).send(statusMessage);
};

module.exports = {
  getStatus,
};
