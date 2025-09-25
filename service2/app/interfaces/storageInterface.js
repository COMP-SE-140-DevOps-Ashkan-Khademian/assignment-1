const axios = require('axios');

class StorageInterface {
  constructor() {
    this.baseUrl = process.env.STORAGE_URL || 'http://storage:5000';
  }

  async appendLog(logEntry) {
    try {
      const response = await axios.post(`${this.baseUrl}/log/`, {
        log: logEntry
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to append log to storage: ${error.message}`);
    }
  }
}

module.exports = StorageInterface;
