const axios = require("axios");

class StorageInterface {
  constructor() {
    this.baseUrl = process.env.STORAGE_URL || "http://storage:5000";
  }

  async appendLog(logEntry) {
    await axios.post(`${this.baseUrl}/log`, logEntry, {
      headers: { "Content-Type": "text/plain" },
    });
  }
}

module.exports = StorageInterface;
